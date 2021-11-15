from django.contrib import admin
import pandas as pd
from .forms import ExcelForm
from .models import OnlineTestQuestion, AnswerTest, OnlineTest
from django.utils.safestring import mark_safe


class QuestionInstanceAdmin(admin.TabularInline):
    model = OnlineTestQuestion
    readonly_fields = ['get_image']

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
    list_display_links = ['id', 'name']


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


admin.site.site_title = "Панель админисратора"
admin.site.site_header = "Панель админисратора"
