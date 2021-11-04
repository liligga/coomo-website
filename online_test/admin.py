from django.contrib import admin
from .models import OnlineTestQuestion, AnswerTest, OnlineTest


class QuestionInstanceAdmin(admin.TabularInline):
	model = OnlineTestQuestion


class AnswerInstanceAdmin(admin.TabularInline):
	model = AnswerTest


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
	list_display_links = ['id', 'name']
	inlines = [QuestionInstanceAdmin, AnswerInstanceAdmin]
