from .serializers import MenuSerializer, FooterSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import *



class MenuObjectsView(generics.ListAPIView):
	queryset = MenuObject.active_objects.all()
	serializer_class = MenuSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['lang_menu_object']


class FooterObjectsView(generics.ListAPIView):
	queryset = FooterObject.active_objects.all()
	serializer_class = FooterSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['lang_footer_object']