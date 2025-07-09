from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    SubjectList,
    SubjectDetail,
    CourseViewSet,
    CommentViewSet,
    RegisterView,
    LoginView,
    LogoutView
)

# ViewSet'lar uchun router yaratamiz
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'comments', CommentViewSet, basename='comment')

# Asosiy URL manzillari
urlpatterns = [
    # Router tomonidan yaratilgan barcha URL'larni qo'shamiz
    # (masalan, /api/courses/, /api/courses/1/, /api/comments/ va hokazo)
    path('', include(router.urls)),

    # Fanlar (Subjects) uchun alohida yo'llar
    path('subjects/', SubjectList.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetail.as_view(), name='subject-detail'),

    # Autentifikatsiya yo'llari
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # JWT access token'ni yangilash uchun yo'l
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]