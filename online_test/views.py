from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import OnlineTest
from rest_framework.views import APIView
from django.http import Http404
from .serializers import OnlineTestListSerializer, AnswerSerializer



class OnlineTestViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = OnlineTest.objects.all()
	serializer_class = OnlineTestListSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = [
		'language',
		'part_num',
		'version',
		'num_questions',
		'duration']

	# @action(detail=True)
	# def check_answers(self, request, pk=None):
	# 	"""ендпоинт для проверки ответов на вопросы"""
	# 	answers = OnlineTest.objects.get(pk=pk).answers.all()
	# 	serializer = AnswerSerializer(data=request.data, many=True)
	# 	total = 0
	# 	if serializer.is_valid():
	# 		for a in serializer.validated_data:
	# 			current = answers.filter(question_number=a.get('number'))[0]
	# 			if current.correct_answer == a.get('answer'):
	# 				total += 1
	# 	return Response({'status': 'OK', 'number_of_correct_answers': total, 'errors': serializer.errors})


# class OnlineTestListView(ListAPIView):
# 	queryset = OnlineTest.objects.all()
# 	serializer_class = OnlineTestListSerializer
# 	filter_backends = [DjangoFilterBackend]
# 	filterset_fields = ['language', 'part_num', 'version', 'num_questions', 'duration']


class TestQuestionsView(APIView):
	def get(self, request, pk):
		online_test = OnlineTest.objects.get(pk=pk)
		serializer = QuestionSerializer(online_test)
		return Response(serializer.data)


class CheckTestAnswersView(APIView):
	def get(self, request, pk):
		online_test = OnlineTest.objects.get(pk=pk)
		test = OnlineTestListSerializer(online_test)
		answers = online_test.answers.all()
		data = {a.question_number: a.correct_answer for a in answers}
		return Response({'test': test.data, 'answers': data})

