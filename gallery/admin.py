from django.contrib import admin
from .models import Gallery, GalleryImage

class GalleryImageInstanceAdmin(admin.TabularInline):
	model = GalleryImage


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'author']
	list_filter = ['id', 'title', 'author']
	save_as = True
	list_display_links = ['id', 'title']
	inlines = [GalleryImageInstanceAdmin]
