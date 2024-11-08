from rest_framework import serializers
from .models import Course, Video


class CoursesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'lang')


class VideoSerializer(serializers.ModelSerializer):
    course = serializers.RelatedField(source='course.course', read_only=True)

    class Meta:
        model = Video
        read_only_fields = ('video_link',)
        fields = ('id', 'name', 'video_link', 'course')


class CourseDetailSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ('name', 'lang', 'videos')
