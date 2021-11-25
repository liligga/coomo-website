from django.contrib import admin
from .models import Course, Video


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'lang']
	list_filter = ['name', 'lang']
	save_as = True


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
	list_display = ['course', 'name', 'lang']
	list_filter = ['name', 'lang']
	save_as = True
