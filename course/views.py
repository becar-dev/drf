from django.db.models import Avg, Count
from rest_framework import viewsets, status
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

# drf_yasg importlari
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Serializers va Permission'larni import qilish
from .serializers import (
    SubjectSerializer,
    CourseListSerializer,
    CourseDetailSerializer,
    ModuleSerializer,
    CommentSerializer,
    RegisterSerializer,
    LoginSerializer,
    LogoutJWTSerializer
)
from .models import Subject, Course, Module, Comment
from .permission import IsEvenYear, IsSuperUserOnly


auth_type_param = openapi.Parameter(
    'auth_type',
    openapi.IN_QUERY,
    description="Autentifikatsiya turi. Tanlovlar: 'token', 'jwt', 'session'",
    type=openapi.TYPE_STRING,
    enum=['token', 'jwt', 'session'],
    default='jwt',
    required=True
)


# 📘 Subject Views (Optimizallashtirildi va ViewSet'ga o'tkazildi)
class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Fanlar uchun ViewSet. Faqat o'qish uchun (List va Retrieve).
    """
    serializer_class = SubjectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        OPTIMIZATSIYA: Har bir fan uchun kurslar sonini bitta so'rovda hisoblash (`annotate`)
        va bog'liq kurslarni oldindan yuklash (`prefetch_related`) uchun optimallashtirildi.
        """
        return Subject.objects.prefetch_related('courses').annotate(
            course_count=Count('courses')
        )

# 📘 Course Views (Optimizallashtirilgan)
class CourseViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated, IsEvenYear, IsSuperUserOnly]
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        """
        Action'ga qarab kerakli serializerni tanlaydi.
        'list' uchun -> CourseListSerializer (yengil)
        'retrieve' va boshqalar uchun -> CourseDetailSerializer (to'liq)
        """
        if self.action == 'list':
            return CourseListSerializer
        return CourseDetailSerializer

    def get_queryset(self):
        """
        OPTIMIZATSIYA: Barcha bog'liq modellar bitta so'rovda olinadi.
        - `prefetch_related`: 'modules' va 'comments' uchun N+1 muammosini hal qiladi.
        - `select_related`: 'subject' uchun JOIN ishlatadi.
        - `annotate`: kerakli hisob-kitoblarni (reyting, soni) bazada bajaradi.
        """
        user = self.request.user

        queryset = Course.objects.select_related('subject').prefetch_related(
            'modules',
            'comments'
        ).annotate(
            average_rating=Avg('comments__rating'),
            modules_count=Count('modules', distinct=True),
            comments_count=Count('comments', distinct=True)
        )

        # Oddiy foydalanuvchilar uchun faqat bepul kurslar
        if not user.is_staff and not user.is_superuser:
            queryset = queryset.filter(is_premium=False)

        return queryset.order_by('-average_rating')

    def perform_create(self, serializer):
        """Yangi kurs yaratilganda avtomatik tarzda egasini (owner) belgilaydi."""
        serializer.save(owner=self.request.user)


# 📘 Module Views (Optimizallashtirilgan)
class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        OPTIMIZATSIYA: `select_related('course')` har bir modul uchun uning kurs
        ma'lumotlarini alohida so'rovsiz, bitta JOIN orqali olishni ta'minlaydi.
        """
        return Module.objects.select_related('course').all()

# 📘 Comment Views (Optimizallashtirilgan)
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        OPTIMIZATSIYA: Har bir izoh uchun uning egasi (owner) va kursi (course)
        ma'lumotlarini bitta so'rovda olish uchun `select_related` qo'shildi.
        """
        return Comment.objects.select_related('owner', 'course').all()

    def perform_create(self, serializer):
        """Yangi izoh yaratilganda avtomatik tarzda egasini (owner) belgilaydi."""
        serializer.save(owner=self.request.user)


# ===============================================================
# AUTENTIFIKATSIYA VIEW'LARI (O'zgarishsiz)
# ===============================================================

class RegisterView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        manual_parameters=[auth_type_param],
        request_body=RegisterSerializer,
        operation_summary="1. Ro'yxatdan o'tish (3 xil usulda)",
        tags=['Authentication'],
        # ... (swagger qismi o'zgarishsiz)
    )
    def post(self, request):
        auth_type = request.query_params.get("auth_type", "jwt")
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if auth_type == "token":
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'auth_type': 'token', 'token': token.key}, status=status.HTTP_201_CREATED)
            elif auth_type == "jwt":
                refresh = RefreshToken.for_user(user)
                return Response({
                    'auth_type': 'jwt',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }, status=status.HTTP_201_CREATED)
            elif auth_type == "session":
                login(request, user)
                return Response({'auth_type': 'session', 'message': 'User registered and logged in with session'},
                                status=status.HTTP_201_CREATED)
            return Response({'error': 'Invalid auth_type'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        manual_parameters=[auth_type_param],
        request_body=LoginSerializer,
        operation_summary="2. Tizimga kirish (3 xil usulda)",
        tags=['Authentication'],
        # ... (swagger qismi o'zgarishsiz)
    )
    def post(self, request):
        auth_type = request.query_params.get("auth_type", "jwt")
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if not user:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        if auth_type == "token":
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'auth_type': 'token', 'token': token.key}, status=status.HTTP_200_OK)
        elif auth_type == "jwt":
            refresh = RefreshToken.for_user(user)
            return Response({
                'auth_type': 'jwt',
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        elif auth_type == "session":
            login(request, user)
            return Response({'auth_type': 'session', 'message': 'Logged in with session'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid auth_type'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        manual_parameters=[auth_type_param],
        request_body=LogoutJWTSerializer,
        operation_summary="3. Tizimdan chiqish (3 xil usulda)",
        tags=['Authentication'],
        # ... (swagger qismi o'zgarishsiz)
    )
    def post(self, request):
        auth_type = request.query_params.get("auth_type", "jwt")
        try:
            if auth_type == "token":
                request.user.auth_token.delete()
                logout(request)
                return Response(status=status.HTTP_204_NO_CONTENT)
            elif auth_type == "jwt":
                serializer = LogoutJWTSerializer(data=request.data)
                if serializer.is_valid():
                    refresh_token = serializer.validated_data["refresh"]
                    token = RefreshToken(refresh_token)
                    token.blacklist()
                    logout(request)
                    return Response(status=status.HTTP_204_NO_CONTENT)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif auth_type == "session":
                logout(request)
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response({"error": "Invalid auth_type"}, status=status.HTTP_400_BAD_REQUEST)
        except (AttributeError, TokenError) :
            return Response({"error": "Invalid token or action."}, status=status.HTTP_400_BAD_REQUEST)
