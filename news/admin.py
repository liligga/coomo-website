from django.contrib import admin
from django import forms
from .models import *
from django.utils.safestring import mark_safe


class NewsAdminForm(forms.ModelForm):
	text = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		model = News
		fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'title', 'important', 'created')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('title', 'created')

    fieldsets = [

        ('Новости на других языках', {
            'fields': ('parent',),
            'description': '<p>Укажите <strong>главную новость</strong>, если эта является ее переводом</p>'
        },),
        ('Создание новости', {
            'fields': ('title', 'article', 'important', 'language', 'cover')
        },),
        ('Другие возможности', {
            'fields': ('banners',),
            'description': '<strong>Использовать эту новость как баннер на главной</strong>'
        })]

class NewsAdmin(admin.ModelAdmin):
	list_display = ('id', 'slug', 'title', 'language', 'important', 'author', 'created', 'get_cover', 'banners', 'excerpt')
	list_display_links = ('id', 'title')
	search_fields = ('title',)
	list_filter = ('title', 'created')
	form = NewsAdminForm

	def get_cover(self, obj):
		return mark_safe(f'<img src={obj.cover.url} width="50" height="60">')


    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


    def get_cover(self, obj):
        if obj.cover:
            return mark_safe(f'<img src={obj.cover.url} width="50" height="60">')


    get_cover.short_description = 'Изображение'

admin.site.register(News, NewsAdmin)
