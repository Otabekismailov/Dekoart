from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static, serve
from django.conf.urls.i18n import i18n_patterns
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from drf_yasg.generators import OpenAPISchemaGenerator


class ForHttpsGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ['http', 'https']
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="Dekoart",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    generator_class=ForHttpsGenerator,
    # permission_classes=(permissions.AllowAny,),
)

swagger_patterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns = i18n_patterns(
    path('deko_admin/', admin.site.urls),
    path('api/v1/', include('apps.products.urls')),
    path('api/v1/dictionary/', include('apps.dictionary.urls')),
    path('api/v1/', include('apps.core.urls')),
    path('api/v1/', include('apps.authentication.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    prefix_default_language=False
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += swagger_patterns
