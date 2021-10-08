from rest_framework import serializers
from .models import *




class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = MenuObject
		fields = ('title', 'link', 'is_active', 'icon', 'lang_menu_object')


class FooterSerializer(serializers.ModelSerializer):
	class Meta:
		model = FooterObject
		fields = ('title', 'link', 'is_active', 'lang_footer_object')