from django.contrib import admin
from .models import Gallery, GalleryImage
from django.utils.safestring import mark_safe


class GalleryImageInstanceAdmin(admin.TabularInline):
	model = GalleryImage
	readonly_fields=['get_image']

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.photo.url} width="300" height="200"')

	get_image.short_description = 'Изображение'

	fieldsets = (
		(None, {
			"fields": (("id", "photo", "get_image"),)
			}),
		)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'author']
	list_filter = ['id', 'title', 'author']
	save_as = True
	list_display_links = ['id', 'title']
	inlines = [GalleryImageInstanceAdmin]

