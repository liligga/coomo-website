import factory
import random
import faker
from django.contrib.auth.models import User
from .models import *
from . import signals
# from django.db.models import signals

factory.Faker._DEFAULT_LOCALE = 'ru_RU'

class UserFactory(factory.django.DjangoModelFactory):

    username = factory.Sequence('testuser{}'.format)
    email = factory.Sequence('testuser{}@company.com'.format)

    class Meta:
        model = User



@factory.django.mute_signals(signals.post_save, signals.pre_save)
class NewsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = News

    title = factory.LazyAttribute(lambda _: faker.Faker().sentence())
    article = faker.Faker().text()
    important = True
    lang = 'Ru'
    author = factory.SubFactory(UserFactory)
