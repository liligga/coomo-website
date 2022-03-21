from rest_framework import serializers
from .models import OnlineTestQuestion, OnlineTest, AnswerTest


class OnlineTestListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='get_name_display')
    lang = serializers.CharField(source='get_lang_display')

    class Meta:
        model = OnlineTest
        fields = ('id', 'name', 'intro', 'part_num', 'version', 'duration',
                  'num_questions', 'lang', 'eng_test')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerTest
        fields = ('question_number', 'correct_answer')


class QuestionSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    name = serializers.CharField(source='get_name_display')
    first = serializers.SerializerMethodField()

    def get_first(self, obj):
        return obj.questions.first().num_start

    def get_questions(self, obj):
        return obj.questions.all().values('question', 'num_start', 'num_end')

    class Meta:
        model = OnlineTest
        fields = ('id', 'name', 'part_num', 'version', 'duration',
                  'num_questions', 'num_answers', 'lang', 'first', 'questions', 'eng_test')
