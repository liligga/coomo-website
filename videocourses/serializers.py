from rest_framework import serializers
from .models import *


class CoursesListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('name', 'description', 'lang_course')


class CourseDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('name', 'description', 'lang_course')