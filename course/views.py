from django.db.models import Avg
from rest_framework import viewsets, generics
from .models import Subject, Course, Comment
from .serializers import SubjectSerializer, CourseSerializer, CommentSerializer

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

    def get_queryset(self):
        return Course.objects.annotate(
            average_rating=Avg('comments__rating')
        ).order_by('-average_rating')

# Comments
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
