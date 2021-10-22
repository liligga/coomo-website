from rest_framework import serializers
from .models import MenuLink, FooterLink


class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = MenuLink
		fields = ('id', 'title', 'link', 'icon', 'lang_menu_link')


class FooterSerializer(serializers.ModelSerializer):
	class Meta:
		model = FooterLink
		fields = ('id', 'title', 'link', 'lang_footer_link')
