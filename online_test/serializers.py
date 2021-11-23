from rest_framework import serializers
from .models import OnlineTestQuestion, OnlineTest, AnswerTest


class OnlineTestListSerializer(serializers.ModelSerializer):
    #  questions = OnlineTestQuestionSerializer(many = True)

    class Meta:
        model = OnlineTest
        fields = ('id', 'name', 'intro', 'part_num', 'version', 'duration',
                  'num_questions', 'language')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerTest
        fields = ('question_number', 'correct_answer')


class QuestionSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    def get_questions(self, obj):
        return obj.questions.all().values_list('question', flat=True)

    class Meta:
        model = OnlineTest
        fields = ('id', 'name', 'part_num', 'version', 'duration',
                  'num_questions', 'language', 'questions')
