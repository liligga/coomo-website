Склонировать. Установить глобально pipenv

Создать окружение и сразу запустить `pipenv shell`

Запустить окружение и установить зависимости
```
pipenv shell
pipenv install
```
Установить пакет `pipenv install package-name`

Удалить какой-либо пакет `pipenv uninstall package-name`

Деактивировать окружение `exit`

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
