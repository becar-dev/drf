from django.db.models import Avg
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .models import Subject, Course, Comment
from .serializers import SubjectSerializer, CourseSerializer, CommentSerializer
from .permission import *

# Subjects
class SubjectList(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

# Courses
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminOrReadOnlyPremium,
        IsEvenYear,
        IsSuperUserOnly,
        AllowOnlyPutAndPatch,]

    def get_queryset(self):
        user = self.request.user

        # Barcha kurslar (admin uchun)
        queryset = Course.objects.annotate(
            average_rating=Avg('comments__rating')
        )

        # Agar foydalanuvchi oddiy bo‘lsa, faqat is_premium=False kurslar
        if not user.is_staff and not user.is_superuser:
            queryset = queryset.filter(is_premium=False)

        # Baholar bo‘yicha kamayish tartibida saralash
        return queryset.order_by('-average_rating')

# Comments
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
