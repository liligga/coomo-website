from rest_framework import serializers

from news.models import News
from .models import MenuLink, FooterLink


class MenuSerializer(serializers.ModelSerializer):
    news_slug = serializers.SlugField(source='news.slug')
    class Meta:
        model = MenuLink
        fields = ('id', 'title', 'link', 'icon', 'lang', 'news_slug')


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterLink
        fields = ('id', 'title', 'link', 'lang')
