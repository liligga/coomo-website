from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    slug = serializers.SlugField()
    excerpt = serializers.CharField()
    cover = serializers.ImageField(use_url=False)
    lang = serializers.CharField()
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    project = serializers.BooleanField()


class NewsDetailSerializer(serializers.ModelSerializer):
    # author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'slug', 'article', 'cover', 'created', 'updated', 'project')
