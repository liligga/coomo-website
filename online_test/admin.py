from django.contrib import admin
import pandas as pd
from .forms import ExcelForm, AnswerFormAdmin
from .models import OnlineTestQuestion, AnswerTest, OnlineTest
from django.utils.safestring import mark_safe


class QuestionInstanceAdmin(admin.TabularInline):
    model = OnlineTestQuestion
    readonly_fields = ["get_image"]

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.question.url} width="200" height="300"'
        )

    get_image.short_description = "Изображение"
    fieldsets = (
        (
            None,
            {
                "fields": (
                    (
                        "num_start",
                        "num_end",
                        "question",
                        "question_image",
                        "get_image",
                    ),
                )
            },
        ),
    )


class AnswerInstanceAdmin(admin.TabularInline):
    model = AnswerTest
    form = AnswerFormAdmin


@admin.register(OnlineTest)
class OnlineTestAdmin(admin.ModelAdmin):
    save_on_top = True
    excel = ExcelForm
    readonly_fields = ("excel",)
    list_display = [
        "id",
        "name",
        "part_num",
        "version",
        "lang",
        "is_active",
    ]
    list_display_links = ["id", "name"]
    inlines = [QuestionInstanceAdmin, AnswerInstanceAdmin]
    fieldsets = [
        (
            "ОНЛАЙН ТЕСТ",
            {
                "fields": (
                    "name",
                    "eng_test",
                    "part_num",
                    "version",
                    "duration",
                    "num_questions",
                    "num_answers",
                    "lang",
                    "is_active",
                    "intro",
                    "excel",
                )
            },
        ),
    ]

    def save_model(self, request, obj, form, change):
        file = request.FILES.get("excel_file")
        obj.save()
        if file:
            answers = pd.read_excel(file)
            for col_n, col_contents in answers.iteritems():
                if str(col_contents.values[0]).isdigit():
                    answers = AnswerTest.objects.create(
                        onlinetest=obj,
                        question_number=col_contents.values[0],
                        correct_answer=col_contents.values[1],
                    )
                    answers.save()


admin.site.site_title = "Панель администратора"
admin.site.site_header = "Панель администратора"
