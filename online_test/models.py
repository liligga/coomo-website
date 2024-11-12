from ckeditor.fields import RichTextField
from django.db import models

LANGUAGE_CHOICES = [
    (None, "Выберите язык"),
    ("Ru", "Русский"),
    ("Kg", "Кыргызский"),
]


SCHOOL_SUBJECTS = [
    (
        "На русском",
        (
            ("Math_ru", "Математика"),
            ("Analogies_ru", "Аналогии и дополнения предложений"),
            ("Reading_ru", "Чтение и понимание"),
            (
                "Grammatic_practice_ru",
                "Практическая грамматика русского языка",
            ),
            ("History_ru", "История"),
            ("Physics_ru", "Физика"),
            ("Biology_ru", "Биология"),
            ("Chemistry_ru", "Химия"),
            ("Math_subj_ru", "Математика предметная"),
            ("English_ru", "Английский язык"),
            ("Language_ru", "Русский язык и литература"),
        ),
    ),
    (
        "Кыргызча",
        (
            ("Math_kg", "Математика"),
            ("Analogies_kg", "Окшоштуктар жана сүйлөмдөрдү толуктоо"),
            ("Reading_kg", "Текстти окуу жана түшүнүү"),
            (
                "Grammatic_practice_kg",
                "Кыргыз тилинин практикалык грамматикасы",
            ),
            ("History_kg", "Тарых"),
            ("Physics_kg", "Физика"),
            ("Biology_kg", "Биология"),
            ("Chemistry_kg", "Химия"),
            ("Math_subj_kg", "Математика предметная"),
            ("English_kg", "Англис тили"),
            ("Language_kg", "Кыргыз тили жана адабияты"),
        ),
    ),
]


class OnlineTest(models.Model):
    PART_NUMBERS = [
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (6, "VI"),
        (7, "VII"),
        (8, "VIII"),
        (9, "IX"),
        (10, "X"),
    ]
    name = models.CharField(
        max_length=100,
        choices=SCHOOL_SUBJECTS,
        verbose_name="Предмет",
        db_index=True,
    )
    part_num = models.IntegerField(
        verbose_name="Часть", choices=PART_NUMBERS, blank=True, null=True
    )
    version = models.IntegerField(default=1, verbose_name="Вариант")
    duration = models.IntegerField(verbose_name="Время (в минутах)")
    num_questions = models.IntegerField(verbose_name="Количество вопросов")
    num_answers = models.IntegerField(
        verbose_name="Количество вариантов ответа"
    )
    lang = models.CharField(
        max_length=15,
        default="Ru",
        choices=LANGUAGE_CHOICES,
        verbose_name="Язык теста",
    )
    eng_test = models.BooleanField(
        default=False,
        help_text="Включить только для теста по английскому языку",
        verbose_name="Тест по английскому языку",
    )
    is_active = models.BooleanField(default=True, verbose_name="Опубликован")
    intro = RichTextField(verbose_name="Приветственный текст")
    order_number = models.PositiveIntegerField(
        verbose_name="Порядковый номер",
        default=1,
    )

    class Meta:
        verbose_name = "Онлайн тест"
        verbose_name_plural = "Онлайн тесты"
        ordering = ["order_number"]

    def __str__(self):
        return self.get_name_display()


class OnlineTestQuestion(models.Model):
    ACTION_CREATE = "CREATE"
    onlinetest = models.ForeignKey(
        OnlineTest, on_delete=models.CASCADE, related_name="questions"
    )
    question = models.ImageField(
        upload_to="ort/images/question/", verbose_name="Картинка с вопросами"
    )
    num_start = models.IntegerField(
        verbose_name="С какого вопроса начинается тест на картинке(номер)"
    )
    num_end = models.IntegerField(
        verbose_name="На каком вопросе заканчивается тест на картинке(номер)"
    )
    question_image = models.BooleanField(
        default=False, verbose_name="Экран с картинкой вопроса"
    )

    class Meta:
        verbose_name = "Вопрос к тесту"
        verbose_name_plural = "Вопросы к тесту"

    def __str__(self):
        return ""


CORRECT_ANS_CHOICES = [
    ("А", "А"),
    ("Б", "Б"),
    ("В", "В"),
    ("Г", "Г"),
    ("Д", "Д"),
    ("Е", "Е"),
]


class AnswerTest(models.Model):
    ACTION_CREATE = "CREATE"
    onlinetest = models.ForeignKey(
        OnlineTest, on_delete=models.CASCADE, related_name="answers"
    )
    question_number = models.IntegerField(
        verbose_name="Номер вопроса", blank=True
    )
    correct_answer = models.CharField(
        default="А",
        choices=CORRECT_ANS_CHOICES,
        verbose_name="Правильный ответ",
        max_length=2,
        blank=True,
    )

    class Meta:
        verbose_name = "Ответ к тесту"
        verbose_name_plural = "Ответы к тесту"

    def __str__(self):
        return self.onlinetest.name
