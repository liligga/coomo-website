from django.contrib import admin
from .models import *


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
        'excel_file'
    ]
    inlines = [QuestionInstanceAdmin, AnswerInstanceAdmin]
