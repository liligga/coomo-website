from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import News

# @receiver(pre_save, sender=News)
def news_pre_save(sender, instance, *args, **kwargs):
    if instance.important:
        try:
            important_news = News.objects.get(important=True)
            if instance != important_news:
                important_news.important = False
                important_news.save()
        except News.DoesNotExist:
            pass


# @receiver(post_save, sender=News)
def news_save(sender, instance, created, **kwargs):
    if created:
        if not instance.parent:
            instance.parent = instance
            instance.save()

pre_save.connect(news_pre_save, sender=News)
post_save.connect(news_save, sender=News)
