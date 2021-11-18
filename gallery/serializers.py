from rest_framework import serializers
from .models import Gallery, GalleryImage
# from .views import GalleryDetailView


class GalleryImagesSerializer(serializers.Serializer):
	photo = serializers.ImageField(use_url=False)


class GalleryListSerializers(serializers.ModelSerializer):
	cover = serializers.SerializerMethodField()

	class Meta:
		model = Gallery
		fields = ('id', 'title', 'cover')

	def get_cover(self, obj):
		return GalleryImagesSerializer(obj.photos.first()).data


class GalleryDetailSerilizer(serializers.Serializer):
	title = serializers.CharField()
	description = serializers.CharField()
	photos_gallery = GalleryImagesSerializer(source='photos', many=True)