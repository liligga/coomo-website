from rest_framework import serializers
from .models import *


class OnlineTestListSerializer(serializers.ModelSerializer):
	class Meta:
		model = OnlineTest
		fields = ('id', 'name', 'part_num', 'version', 'duration', 'num_questions', 'language')


class OnlineTestDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = OnlineTest
		fields = ('id', 'name', 'part_num', 'version', 'intro', 'num_questions', 'duration', 'language', 'questions')


class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = AnswerTest
		fields = ('id', 'question_number', 'correct_answer')


class OnlineTestDetailAndAnswSerializer(serializers.ModelSerializer):
	class Meta:
		model = OnlineTest
		fields = ('id', 'questions', 'answers')

