from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from rest_framework import viewsets, generics
from .serializers import OnlineTestListSerializer


class OnlineTestViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = OnlineTest.objects.all()
	serializer_class = OnlineTestListSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['language', 'part_num', 'version', 'num_questions', 'duration']
