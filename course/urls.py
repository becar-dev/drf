from django.urls import path
from .views import *

urlpatterns = [
    path('subjects/', SubjectList.as_view(), name='subject-list'),
    path('subjects/create/', SubjectCreate.as_view(), name='subject-create'),
    path('subjects/<int:pk>/', SubjectDetail.as_view(), name='subject-detail'),
    path('subjects/<int:pk>/update/', SubjectUpdate.as_view(), name='subject-update'),
    path('subjects/<int:pk>/delete/', SubjectDelete.as_view(), name='subject-delete'),
    path('courses/', CourseList.as_view(), name='course-list'),
    path('courses/create/', CourseCreate.as_view(), name='course-create'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('courses/<int:pk>/update/', CourseUpdate.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', CourseDelete.as_view(), name='course-delete'),
]
