from rest_framework import serializers
from .models import *


class OnlineTestQuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = OnlineTestQuestion
		fields = ('question',)


class OnlineTestListSerializer(serializers.ModelSerializer):
	questions = OnlineTestQuestionSerializer(many = True)

	class Meta:
		model = OnlineTest
		fields = ('name', 'intro', 'part_num', 'version', 'duration', 'num_questions', 'language', 'questions')

class AnswerSerializer(serializers.Serializer):
	number = serializers.IntegerField()
	answer = serializers.IntegerField()

