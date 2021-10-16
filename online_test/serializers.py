from rest_framework import serializers
from .models import *


class OnlineTestListSerializer(serializers.ModelSerializer):
	class Meta:
		model = OnlineTest
		fields = ('name', 'part_num', 'version', 'duration', 'num_questions', 'language')