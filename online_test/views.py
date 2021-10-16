from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from rest_framework import generics
from .serializers import OnlineTestListSerializer


class OnlineTestListView(generics.ListAPIView):
	queryset = OnlineTest.objects.all()
	serializer_class = OnlineTestListSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['language', 'part_num', 'version', 'num_questions', 'duration']