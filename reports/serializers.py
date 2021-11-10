from rest_framework import serializers
from ckeditor_uploader.fields import RichTextUploadingField
from .models import Reports


class ReportsSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID')
    title = serializers.CharField(max_length=250)
    pdf = serializers.FileField()
    article = serializers.CharField()
