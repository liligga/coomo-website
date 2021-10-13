from rest_framework import serializers
# from django.utils.text import slugify
from .models import News


class NewsListSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = News
		fields = ['title','slug','important', 'created']




class NewsDetailSerializer(serializers.ModelSerializer):
	author = serializers.SlugRelatedField('username', read_only=True)
	#related_news = ['title','slug','important']
	

	class Meta:
		model = News
		fields = '__all__'

