from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectList, SubjectDetail, CourseViewSet, CommentViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('subjects/', SubjectList.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetail.as_view(), name='subject-detail'),
    path('', include(router.urls)),
]
# 📂 MEDIA fayllar faqat DEBUG holatda xizmat qiladi
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
