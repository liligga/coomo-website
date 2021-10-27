from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *
from django.utils.safestring import mark_safe


class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'slug', 'title', 'language', 'important', 'author', 'created', 'get_cover', 'banners', 'excerpt', 'parent')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('title', 'created')
    form = NewsAdminForm

    def get_cover(self, obj):
        if obj.cover:
            return mark_safe(f'<img src={obj.cover.url} width="50" height="60">')

    get_cover.short_description = 'Изображение'


admin.site.register(News, NewsAdmin)
