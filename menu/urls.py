from django.urls import path
from .views import *
from . import views


urlpatterns = [
	path('api/menu', views.MenuLinksView.as_view(), name='menu_objects'),
	path('api/footer', views.FooterLinksView.as_view(), name='footer_objects')
]