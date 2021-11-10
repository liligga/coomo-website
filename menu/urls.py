from django.urls import path
from .views import MenuLinksView, FooterLinksView


urlpatterns = [
	path('api/menu', MenuLinksView.as_view(), name='menu_objects'),
	path('api/footer', FooterLinksView.as_view(), name='footer_objects')
]
