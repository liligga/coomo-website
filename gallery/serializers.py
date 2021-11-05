from rest_framework import serializers
from .models import Gallery, GalleryImage


class GalleryImagesSerializer(serializers.ModelSerializer):
	photos = serializers.RelatedField(read_only=True, source='gallery.gallery_id')

	class Meta:
		model = GalleryImage
		read_only_fields = ('photo',)
		fields = ('id', 'photo', 'photos')




# class GalleryListSerializers(serializers.ModelSerializer):

# 	class Meta:
# 		model = Gallery
# 		fields = ['id', 'title']


class GalleryDetailSerilizer(serializers.ModelSerializer):
	photos = GalleryImagesSerializer(read_only=True, many=True)

	class Meta:
		model = Gallery
		fields = ('id', 'title', 'description', 'photos')