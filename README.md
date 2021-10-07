Склонировать.

Создать окружение `python -m venv venv`

Запустить окружение и установить зависимости
`pip install -r requirements.txt`

Заполнить свой **.env** файл используя пример **.env_example**

Прогнать миграции и создать суперпользователя

Пушить на свои ветки, `main` и `deploy` не трогать

Чтобы использовать WYSIWYG редактор:

```python
from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    content = RichTextField()
```

Для поддержки загрузки файлов юзать `RichTextUploadingField` импорт из  `ckeditor_uploader.fields`