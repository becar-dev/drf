# n63_course/urls.py
from django.contrib import admin
from django.urls import path, include
from course.views import RegisterView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from course.utils.swagger import JWTSchemaGenerator

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="TokenAuth bilan CRUD API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=JWTSchemaGenerator
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('course.urls')),

    path('api/login/', obtain_auth_token),
    path('api/register/', RegisterView.as_view()),
    path('api/logout/', LogoutView.as_view()),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]



