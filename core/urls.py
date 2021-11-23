from decorator_include import decorator_include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from authentication.views import check_otp, login_page

schema_view = get_schema_view(
    openapi.Info(
        title="ЦООМО",
        default_version='v1',
        description="",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include('videocourses.urls')),
    path('', include('news.urls')),
    path('', include('menu.urls')),
    path('', include('online_test.urls')),
    path('', include('reports.urls')),
    path('', include('gallery.urls')),
    path('', include('search.urls')),
    path('admin/', decorator_include(login_required, admin.site.urls), name='admin'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('login_page/', login_page, name='login_page'),
    path('check_otp/<str:email>', check_otp, name='check_otp'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
