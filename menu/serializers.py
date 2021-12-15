from rest_framework import serializers
from .models import MenuLink, FooterLink


class MenuSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    icon = serializers.CharField()
    lang = serializers.CharField()
    page_slug = serializers.SlugField(source='page.slug', allow_null=True)
    position = serializers.CharField()
    link = serializers.CharField()


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterLink
        fields = ('id', 'title', 'link', 'lang')
