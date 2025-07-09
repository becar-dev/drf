# n63_course/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# Bu custom generatorni ishlatishda davom etishingiz mumkin
from course.utils.swagger import JWTSchemaGenerator
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Token, JWT va Session Auth bilan CRUD API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=JWTSchemaGenerator
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Barcha API yo'llari endi 'course' ilovasiga yo'naltiriladi
    path('api/', include('course.urls')),
    # Swagger uchun yo'l
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
