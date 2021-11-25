from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import OnlineTest
from rest_framework.views import APIView
from django.http import Http404
from .serializers import OnlineTestListSerializer, QuestionSerializer


class OnlineTestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OnlineTest.objects.all()
    serializer_class = OnlineTestListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'lang',
        'part_num',
        'version',
        'num_questions',
        'duration']


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
