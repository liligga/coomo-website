from .serializers import MenuSerializer, FooterSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import MenuLink, FooterLink


class MenuLinksView(generics.ListAPIView):
	serializer_class = MenuSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['lang_menu_link']

	def get_queryset(self):
		query = self.request.query_params.get('lang_menu_link')
		if query:
			queryset = MenuLink.active_objects.filter(lang_menu_link=query)
		else:
			queryset = MenuLink.active_objects.filter(lang_menu_link='Ru')

		return queryset


class FooterLinksView(generics.ListAPIView):
	serializer_class = FooterSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['lang_footer_link']

	def get_queryset(self):
		query = self.request.query_params.get('lang_footer_link')
		if query:
			queryset = FooterLink.active_objects.filter(lang_footer_link=query)
		else:
			queryset = FooterLink.active_objects.filter(lang_footer_link='Ru')\

		return queryset