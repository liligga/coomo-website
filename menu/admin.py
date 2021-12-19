from django.contrib import admin

from .forms import MenuLinkForm
from .models import MenuLink, FooterLink


@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
	list_display = ['title', 'is_active', 'lang']
	list_filter = ['is_active', 'lang', 'position']
	save_as = True
	form = MenuLinkForm

@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
	list_display = ['title', 'is_active', 'lang']
	list_filter = ['title', 'is_active', 'lang']
	save_as = True
