from django.db.models import Avg
from rest_framework import viewsets, generics, status
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

# drf_yasg importlari
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from .serializers import *
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


# 📘 Subject Views
class SubjectList(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [AllowAny]  # Hamma ko‘ra oladi

class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

# 📘 Course Views
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsEvenYear, IsSuperUserOnly]

    def get_queryset(self):
        user = self.request.user
        queryset = Course.objects.annotate(
            average_rating=Avg('comments__rating')
        )

        # Oddiy foydalanuvchilar uchun faqat bepul kurslar
        if not user.is_staff and not user.is_superuser:
            queryset = queryset.filter(is_premium=False)

        return queryset.order_by('-average_rating')

# 📘 Comment Views
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class RegisterView(APIView):
    """
    Foydalanuvchini 3 xil usulda ro'yxatdan o'tkazadi va tanlangan usulga mos
    ravishda token, jwt yoki sessiya qaytaradi.
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        manual_parameters=[auth_type_param],
        request_body=RegisterSerializer,
        operation_summary="1. Ro'yxatdan o'tish (3 xil usulda)",
        tags=['Authentication'],
        responses={
            201: openapi.Response('Muvaffaqiyatli ro\'yxatdan o\'tish', examples={
                'application/json': {
                    "token_auth_example": {
                        "auth_type": "token",
                        "token": "your_auth_token_string"
                    },
                    "jwt_auth_example": {
                        "auth_type": "jwt",
                        "refresh": "your_refresh_token",
                        "access": "your_access_token"
                    },
                    "session_auth_example": {
                        "auth_type": "session",
                        "message": "User registered and logged in with session"
                    }
                }
            }),
            400: "Validatsiya xatoligi"
        }
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
    """
    Foydalanuvchini 3 xil usulda tizimga kiritadi va tanlangan usulga mos
    ravishda token, jwt yoki sessiya qaytaradi.
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        manual_parameters=[auth_type_param],
        request_body=LoginSerializer,
        operation_summary="2. Tizimga kirish (3 xil usulda)",
        tags=['Authentication'],
        responses={
            200: openapi.Response('Muvaffaqiyatli tizimga kirish', examples={
                'application/json': {
                    "token_auth_example": {
                        "auth_type": "token",
                        "token": "your_auth_token_string"
                    },
                    "jwt_auth_example": {
                        "auth_type": "jwt",
                        "refresh": "your_refresh_token",
                        "access": "your_access_token"
                    },
                    "session_auth_example": {
                        "auth_type": "session",
                        "message": "Logged in with session"
                    }
                }
            }),
            401: "Login yoki parol xato"
        }
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
    """
    Foydalanuvchini 3 xil usulda tizimdan chiqaradi. `Authorization` sarlavhasi talab qilinadi.
    `auth_type='jwt'` uchun so'rov tanasida (`body`) `refresh` token yuborilishi shart.
    """
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        manual_parameters=[auth_type_param],
        request_body=LogoutJWTSerializer,
        operation_summary="3. Tizimdan chiqish (3 xil usulda)",
        tags=['Authentication'],
        operation_description="`auth_type='jwt'` tanlanganda, so'rov tanasida (`body`) `refresh` tokenini yuborish majburiy. " \
                              "Boshqa usullar uchun so'rov tanasi bo'sh bo'ladi.",
        responses={
            204: "Muvaffaqiyatli tizimdan chiqish (No Content)",
            400: "Xato so'rov (masalan, refresh token berilmagan)",
            401: "Autentifikatsiyadan o'tilmagan"
        }
    )
    def post(self, request):
        # ----- TEKSHIRISH UCHUN PRINT'LAR -----
        print("-------------------------")
        # a) So'rov sarlavhalarini (headers) tekshirish
        print("Headers:", request.headers)

        # b) Autentifikatsiyadan o'tgan foydalanuvchini tekshirish
        print("Foydalanuvchi (User):", request.user)

        # c) Qaysi token orqali kirganini tekshirish
        print("Autentifikatsiya tokeni (Auth):", request.auth)
        print("-------------------------")
        # ----- TEKSHIRISH TUGADI -----

        auth_type = request.query_params.get("auth_type", "jwt")

        try:
            if auth_type == "token":
                request.user.auth_token.delete()
                logout(request)  # Session ma'lumotlarini ham tozalaydi
                return Response(status=status.HTTP_204_NO_CONTENT)

            elif auth_type == "jwt":
                serializer = LogoutJWTSerializer(data=request.data)
                if serializer.is_valid():
                    refresh_token = serializer.validated_data["refresh"]
                    token = RefreshToken(refresh_token)
                    token.blacklist()
                    logout(request)  # Session ma'lumotlarini ham tozalaydi
                    return Response(status=status.HTTP_204_NO_CONTENT)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            elif auth_type == "session":
                logout(request)
                return Response(status=status.HTTP_204_NO_CONTENT)

            return Response({"error": "Invalid auth_type"}, status=status.HTTP_400_BAD_REQUEST)

        except (AttributeError, TokenError) as e:
            return Response({"error": "Invalid token or action."}, status=status.HTTP_400_BAD_REQUEST)


