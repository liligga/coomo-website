from rest_framework import serializers

from news.models import News
from .models import MenuLink, FooterLink


class MenuSerializer(serializers.ModelSerializer):
    page_slug = serializers.SlugField(source='page.slug', allow_null=True)

    class Meta:
        model = MenuLink
        fields = ('id', 'title', 'icon', 'lang', 'page_slug')


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterLink
        fields = ('id', 'title', 'link', 'lang')
