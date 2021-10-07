from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	list_display = ('id','title','language','important','author','created')
	list_display_links = ('id','title')
	search_fields = ('title',)
	list_filter = ('title','created')
	form = NewsAdminForm


admin.site.register(News, NewsAdmin)