from rest_framework import serializers
from .models import OnlineTestQuestion, OnlineTest


class OnlineTestQuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = OnlineTestQuestion
		fields = ('question',)


class OnlineTestListSerializer(serializers.ModelSerializer):

	class Meta:
		model = OnlineTest
		fields = (
			'id',
			'name',
			'part_num',
			'version',
			'duration',
			'num_questions',
			'language')


class OnlineTestDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = OnlineTest
		fields = (
			'id',
			'name',
			'part_num',
			'version',
			'intro',
			'num_questions',
			'duration',
			'language',
			'questions')


class OnlineTestDetailAndAnswSerializer(serializers.ModelSerializer):
	class Meta:
		model = OnlineTest
		fields = (
			'name',
			'intro',
			'part_num',
			'version',
			'duration',
			'num_questions',
			'language',
			'questions')


class AnswerSerializer(serializers.Serializer):
	number = serializers.IntegerField()
	answer = serializers.IntegerField()
