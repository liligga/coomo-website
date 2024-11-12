from django.db.models.signals import post_save, pre_save

from .models import News


def news_pre_save(sender, instance, *args, **kwargs):
    if instance.important:
        try:
            lang = instance.lang
            important_news = News.objects.get(important=True, lang=lang)
            if instance != important_news:
                important_news.important = False
                important_news.save()
        except News.DoesNotExist:
            pass


def news_save(sender, instance, created, **kwargs):
    if created:
        if not instance.parent:
            instance.parent = instance
            instance.save()


pre_save.connect(news_pre_save, sender=News)
post_save.connect(news_save, sender=News)
