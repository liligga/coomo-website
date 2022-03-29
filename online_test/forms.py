from django import forms

from online_test.models import AnswerTest


class ExcelForm(forms.Form):
    excel_file = forms.FileField(label='Таблица с ответами')

    def __init__(self, *args, **kwargs):
        super(ExcelForm, self).__init__(*args, **kwargs)
        self.fields['excel_file'].required = False


class AnswerFormAdmin(forms.ModelForm):
    class Meta:
        model = AnswerTest
        fields = ('question_number', 'correct_answer')
        help_texts = {
            'question_number': 'Заполнять номер вопроса с цифры 1 (один).'
        }
        labels = {
            'question_number': 'Заполнять номер вопроса с цифры 1 (один).'
        }
