from rest_framework import serializers
from .models import *


class CoursesListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('name', 'description', 'lang_course')


class VideoSerializer(serializers.ModelSerializer):
	course = serializers.RelatedField(source='course.course',read_only=True)
	class Meta:
		model = Video
		read_only_fields = ('video_link',)
		fields = ('name', 'video_link', 'course')


class CourseDetailSerializer(serializers.ModelSerializer):
	videos = VideoSerializer(read_only=True, many=True)

	class Meta:
		model = Course
		fields = ('name', 'description', 'lang_course', 'videos')