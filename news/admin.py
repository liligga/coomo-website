from django.contrib import admin
from django import forms
from .models import *
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'lang', 'important', 'created')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('lang', 'created', 'banners', 'important', 'project')
    readonly_fields = ['get_cover']

    def get_cover(self, obj):
        if obj.cover:
            return mark_safe(f'<img src={obj.cover.url} width="890" height="479">')

    fieldsets = [
        ('Новости на других языках', {
            'fields': ('parent',),
            'description': '<p>Укажите <strong>главную новость</strong>, если эта является ее переводом</p>'
        },),
        ('Создание новости', {
            'fields': ('title', 'article', 'important', 'lang', 'cover', 'get_cover')
        },),
        ('Другие возможности', {
            'fields': ('banners', 'project'),
            'description': '<strong>Использовать эту новость как баннер на главной</strong>'
        })]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    get_cover.short_description = 'Изображение'
