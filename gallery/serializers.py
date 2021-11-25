from rest_framework import serializers
from .models import Gallery, GalleryImage


class GalleryImagesSerializer(serializers.Serializer):
	photo = serializers.ImageField(use_url=False)


class GalleryListSerializers(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField()
	cover = serializers.SerializerMethodField()

	def get_cover(self, obj):
		return GalleryImagesSerializer(obj.photos.first()).data['photo']


class GalleryDetailSerilizer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField()
	photos_gallery = GalleryImagesSerializer(source='photos', many=True)
