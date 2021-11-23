from rest_framework import serializers
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from .models import News


class NewsSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID')
    title = serializers.CharField(max_length=250)
    slug = serializers.SlugField()
    excerpt = serializers.CharField()
    created = serializers.DateTimeField()
    cover = serializers.ImageField()


class NewsDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = News
        fields = '__all__'
