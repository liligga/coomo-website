from django.contrib import admin
from django import forms
from .models import *
from django.utils.safestring import mark_safe


class NewsAdmin(admin.ModelAdmin):
	list_display = ('id', 'language', 'title', 'important', 'created')
	list_display_links = ('id','title')
	search_fields = ('title',)
	list_filter = ('title','created')

	def save_model(self, request, obj, form, change):
		obj.author = request.user
		super().save_model(request, obj, form, change)

	def get_cover(self, obj):
		return mark_safe(f'<img src={obj.cover.url} width="50" height="60">')

	get_cover.short_description = 'Изображение'

	

admin.site.register(News, NewsAdmin)