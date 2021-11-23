from django.contrib import admin
from .models import Course, Video


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'lang_course']
	list_filter = ['name', 'lang_course']
	save_as = True


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
	list_display = ['name', 'lang_video']
	list_filter = ['name', 'lang_video']
	save_as = True
