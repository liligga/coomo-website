from rest_framework import serializers
from .models import *




class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = MenuLink
		fields = ('title', 'link', 'icon', 'lang_menu_link')


class FooterSerializer(serializers.ModelSerializer):
	class Meta:
		model = FooterLink
		fields = ('title', 'link', 'lang_footer_link')