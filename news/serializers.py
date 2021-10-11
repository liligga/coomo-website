from rest_framework import serializers
from ckeditor_uploader.fields import RichTextUploadingField
from .models import News


class NewsLastestSerializer(serializers.Serializer):
	slug = serializers.SlugField()
	title = serializers.CharField(max_length=250)
	excerpt = serializers.CharField()
	created = serializers.DateTimeField()
	

class NewsImportantSerializer(serializers.Serializer):
	slug = serializers.SlugField()
	title = serializers.CharField(max_length=250)
	excerpt = serializers.CharField()
	important = serializers.BooleanField(read_only=True)
	created = serializers.DateTimeField()


class NewsBannerSerializer(serializers.Serializer):
	slug = serializers.SlugField()
	title = serializers.CharField(max_length=250)
	excerpt = serializers.CharField()
	cover = serializers.ImageField()
	banners = serializers.BooleanField()
	created = serializers.DateTimeField()
	


	




