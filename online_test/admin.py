from django.contrib import admin
from .models import OnlineTest


@admin.register(OnlineTest)
class OnlineTestAdmin(admin.ModelAdmin):
	list_display = [
	'id',
	'name',
	'part_num',
	'version',
	'language',
	'is_active',
	]