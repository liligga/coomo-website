from rest_framework import serializers
from .models import


class NewsListSerializer(serializers.ModelSerializer):
	class Meta:
		model = News
		fields = ['id', 'title','important', 'created']
