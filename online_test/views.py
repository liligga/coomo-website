from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response


class OnlineTestListView(generics.ListAPIView):
	queryset = OnlineTest.objects.all()
	serializer_class = OnlineTestListSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['language', 'part_num', 'version', 'num_questions', 'duration']


class OnlineTestDetailView(APIView):
	queryset = OnlineTest.objects.all()
	serializer_class = OnlineTestDetailSerializer


class CheckAnswerTestView(APIView):
	def get_object(self, pk):
		try:
			return OnlineTest.objects.get(pk=pk)
		except OnlineTest.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		test = self.get_object(pk)
		serializer = OnlineTestDetailAndAnswSerializer(test)
		answers = request.data
		print(answers)
		print(serializer.data)
		print(request.query_params)
		return Response(serializer.data)
