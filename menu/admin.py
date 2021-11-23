from django.contrib import admin
from .models import MenuLink, FooterLink


@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
	list_display = ['title', 'is_active', 'lang_menu_link']
	list_filter = ['title', 'is_active', 'lang_menu_link']
	save_as = True


@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
	list_display = ['title', 'is_active', 'lang_footer_link']
	list_filter = ['title', 'is_active', 'lang_footer_link']
	save_as = True
