from .serializers import MenuSerializer, FooterSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import MenuLink, FooterLink


class MenuLinksView(generics.ListAPIView):
	serializer_class = MenuSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['lang']

	def get_queryset(self):
		query = self.request.query_params.get('lang')
		if query:
			queryset = MenuLink.active_objects.filter(lang=query)
		else:
			queryset = MenuLink.active_objects.filter(lang='Ru')

		return queryset


class FooterLinksView(generics.ListAPIView):
	serializer_class = FooterSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['lang']

	def get_queryset(self):
		query = self.request.query_params.get('lang')
		if query:
			queryset = FooterLink.active_objects.filter(lang=query)
		else:
			queryset = FooterLink.active_objects.filter(lang='Ru')\

		return queryset