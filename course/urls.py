from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

# ViewSet'lar va APIView'larni import qilish
from .views import (
    SubjectViewSet,      # O'zgartirildi: Endi ViewSet ishlatiladi
    CourseViewSet,
    ModuleViewSet,       # Qo'shildi: Modullar uchun ViewSet
    CommentViewSet,
    RegisterView,
    LoginView,
    LogoutView
)

# ViewSet'lar uchun router yaratamiz
router = DefaultRouter()
# Barcha ViewSet'larni router'ga ro'yxatdan o'tkazamiz
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'modules', ModuleViewSet, basename='module')
router.register(r'comments', CommentViewSet, basename='comment')

# Asosiy URL manzillari
urlpatterns = [
    # Router tomonidan avtomatik yaratilgan barcha URL'larni qo'shamiz
    # Masalan: /subjects/, /subjects/1/, /courses/, /courses/1/ va hokazo.
    path('', include(router.urls)),

    # Autentifikatsiya yo'llarini tartiblash uchun 'auth/' prefiksi ostiga olamiz
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),

    # JWT access token'ni yangilash uchun yo'l
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Eslatma: Fanlar (Subjects) uchun alohida yo'llar olib tashlandi,
    # chunki endi ular router tomonidan to'liq boshqariladi.
]
