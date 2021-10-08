from django.urls import path
from .views import *
from . import views


urlpatterns = [
	path('api/menu', views.MenuObjectsView.as_view(), name='menu_objects'),
	path('api/footer', views.FooterObjectsView.as_view(), name='footer_objects')
]