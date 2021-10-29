from django.contrib import admin
from .models import OnlineTestQuestion, AnswerTest, OnlineTest
from django.utils.safestring import mark_safe


class QuestionInstanceAdmin(admin.TabularInline):
	model = OnlineTestQuestion
	readonly_fields=['get_image']

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.question.url} width="200" height="300"')

	get_image.short_description = 'Изображение'

	fieldsets = (
		(None, {
			"fields": (("num_start", "num_end", "question", "get_image"),)
			}),
		)


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
		'is_active'
	]
	list_display_links = ['id', 'name']
	inlines = [QuestionInstanceAdmin, AnswerInstanceAdmin]
	fieldsets = (
		(None, {
			"fields": (("name", "part_num", "version"),)
			}),)

admin.site.site_title="Панель админисратора"
admin.site.site_header="Панель админисратора"