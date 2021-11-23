from rest_framework import serializers

from menu.models import MenuLink
from news.models import News
from online_test.models import OnlineTest
from reports.models import Reports
from videocourses.models import Course


class OnlineTestSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineTest
        fields = '__all__'


class SearchNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class ReportsSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'


class MenuSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuLink
        fields = '__all__'


class CourseSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
