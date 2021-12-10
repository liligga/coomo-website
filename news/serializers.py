from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    slug = serializers.SlugField()
    excerpt = serializers.CharField()
    cover = serializers.ImageField()
    lang = serializers.CharField()
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    project = serializers.BooleanField()

    def to_representation(self, instance):
        response = super(NewsSerializer, self).to_representation(instance)
        if instance.cover:
            response['cover'] = instance.cover.url
        return response


class NewsDetailSerializer(serializers.ModelSerializer):
    # author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'slug', 'article', 'cover', 'created', 'updated', 'project')
