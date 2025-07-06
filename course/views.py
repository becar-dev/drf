from django.db.models import Avg
from django.contrib.auth import logout
from django.contrib.auth.models import User

from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Subject, Course, Comment
from .serializers import (
    SubjectSerializer, CourseSerializer,
    CommentSerializer, RegisterSerializer
)
from .permission import IsEvenYear, IsSuperUserOnly

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

# ✅ Register API
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Logout API
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)

