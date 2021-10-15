"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from decorator_include import decorator_include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from authentication.views import check_otp, login_page

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include('videocourses.urls')),
    path('', include('news.urls')),
    path('', include('menu.urls')),
    path('', include('online_test.urls')),
    path('admin/', decorator_include(login_required, admin.site.urls), name='admin'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('login_page/', login_page, name='login_page'),
    path('check_otp/<str:email>', check_otp, name='check_otp')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
