from django.contrib import admin
from .models import *

@admin.register(MenuObject)
class MenuObjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'is_active', 'lang_menu_object']
	list_filter = ['title', 'is_active', 'lang_menu_object']
	save_as = True

@admin.register(FooterObject)
class FooterObjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'is_active', 'lang_footer_object']
	list_filter = ['title', 'is_active', 'lang_footer_object']
	save_as = True