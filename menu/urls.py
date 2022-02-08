from django.urls import path
from .views import MenuLinksView, FooterLinksView, About

urlpatterns = [
	path('api/menu', MenuLinksView.as_view(), name='menu_objects'),
	path('api/footer', FooterLinksView.as_view(), name='footer_objects'),
	path('api/about', About.as_view(), name='about')
]
