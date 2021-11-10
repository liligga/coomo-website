from .serializers import MenuSerializer, FooterSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import MenuLink, FooterLink


class MenuLinksView(generics.ListAPIView):
	queryset = MenuLink.active_objects.all()
	serializer_class = MenuSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['lang_menu_link']


class FooterLinksView(generics.ListAPIView):
	queryset = FooterLink.active_objects.all()
	serializer_class = FooterSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['lang_footer_link']
