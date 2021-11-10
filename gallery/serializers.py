from rest_framework import serializers
from .models import Gallery, GalleryImage


class GalleryImagesSerializer(serializers.ModelSerializer):
	class Meta:
		model = GalleryImage
		read_only_fields = ('photo',)
		fields = ('id', 'photo')


class GalleryListSerializers(serializers.ModelSerializer):
	cover = serializers.SerializerMethodField()

	class Meta:
		model = Gallery
		fields = ['id', 'title', 'cover']

	def get_cover(self, obj):
		return GalleryImagesSerializer(obj.photos.first()).data


class GalleryDetailSerilizer(serializers.ModelSerializer):
	photos = GalleryImagesSerializer(read_only=True, many=True)

	class Meta:
		model = Gallery
		fields = ('id', 'title', 'description', 'photos')