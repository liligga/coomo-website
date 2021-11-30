from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'slug', 'excerpt', 'cover', 'lang', 'created', 'updated')


class NewsDetailSerializer(serializers.ModelSerializer):
    # author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = News
        fields = ('title', 'slug', 'article', 'cover', 'created', 'updated')
