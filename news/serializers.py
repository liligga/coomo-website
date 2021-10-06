from rest_framework import serializers
from .models import News


class NewsListSerializer(serializers.ModelSerializer):
	class Meta:
		model = News
		fields = ['title','impotant', 'created']


class NewsDetailSerializer(serializers.ModelSerializer):
	author = serializers.SlugRelatedField('username', read_only=True)
	

	class Meta:
		model = News
		fields = '__all__'

