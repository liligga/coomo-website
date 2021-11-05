from django.contrib import admin
import pandas as pd
from .forms import ExcelForm
from .models import *


class QuestionInstanceAdmin(admin.TabularInline):
    model = OnlineTestQuestion


class AnswerInstanceAdmin(admin.TabularInline):
    model = AnswerTest


@admin.register(OnlineTest)
class OnlineTestAdmin(admin.ModelAdmin):
    excel = ExcelForm
    readonly_fields = ('excel',)
    list_display = [
        'id',
        'name',
        'part_num',
        'version',
        'language',
        'is_active',
    ]
    inlines = [QuestionInstanceAdmin, AnswerInstanceAdmin]
    fieldsets = [
        ('ОНЛАЙН ТЕСТ', {
            'fields': (
                'name', 'part_num', 'version', 'duration', 'num_questions', 'num_answers', 'language', 'is_active',
                'intro', 'excel',)
        }
         ),
    ]

    def save_model(self, request, obj, form, change):
        file = request.FILES.get('excel_file')
        obj.save()
        if file:
            answers = pd.read_excel(file)
            for col_n, col_contents in answers.iteritems():
                if str(col_contents.values[0]).isdigit():
                    answers = AnswerTest.objects.create(onlinetest=obj, question_number=col_contents.values[0],
                                                        correct_answer=col_contents.values[1])
                    answers.save()
