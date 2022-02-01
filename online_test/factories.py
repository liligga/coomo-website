import factory
import random
import faker
from django.contrib.auth.models import User
from .models import *

SCHOOL_SUBJECTS = [
            ('Math_ru', 'Математика'),
            ('Analogies_ru', 'Аналогии и дополнения предложений'),
            ('Reading_ru', 'Чтение и понимание'),
            ('Grammatic_practice_ru', 'Практическая грамматика русского языка'),
            ('History_ru', 'История'),
            ('Physics_ru', 'Физика'),
            ('Biology_ru', 'Биология'),
            ('Chemistry_ru', 'Химия'),
            ('Math_subj_ru', 'Математика предметная'),
            ('English_ru', 'Английский язык'),
            ('Math_kg', 'Математика'),
            ('Analogies_kg', 'Окшоштуктар жана сүйлөмдөрдү толуктоо'),
            ('Reading_kg', 'Текстти окуу жана түшүнүү'),
            ('Grammatic_practice_kg', 'Кыргыз тилинин практикалык грамматикасы'),
            ('History_kg', 'Тарых'),
            ('Physics_kg', 'Физика'),
            ('Biology_kg', 'Биология'),
            ('Chemistry_kg', 'Химия'),
            ('Math_subj_kg', 'Математика предметная'),
            ('English_kg', 'Англис тили'),
]


class TestQuestionFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = OnlineTestQuestion

	question = 'ort/images/question/test_image.jpg'
	num_start = faker.Faker().random_int(1, 15)
	num_end = faker.Faker().random_int(16, 30)
	onlinetest = factory.SubFactory('online_test.factories.OnlineTestFactory', onlinetestquestion=None)


class TestAnswerFactory(factory.django.DjangoModelFactory):
	# CORRECT_ANS_CHOICES = [
	# 	('А', 'А'),
	# 	('Б', 'Б'),
	# 	('В', 'В'),
	# 	('Г', 'Г'),
	# 	('Д', 'Д'),
	# 	('Е', 'Е'),
	# ]

	class Meta:
		model = AnswerTest

	question_number = 1
	correct_answer = "А"
	onlinetest = factory.SubFactory('online_test.factories.OnlineTestFactory', answertest=None)


class OnlineTestFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = OnlineTest

	questions = factory.RelatedFactory(
		TestQuestionFactory,
		factory_related_name='onlinetest',
		question='ort/images/question/test_image.jpg',
		num_start=faker.Faker().random_int(1, 15),
		num_end=faker.Faker().random_int(16, 30))	
	answers = factory.RelatedFactory(
		TestAnswerFactory,
		factory_related_name='onlinetest',
		question_number=1,
		correct_answer="А")
	name = random.choice(SCHOOL_SUBJECTS)
	part_num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
	version = faker.Faker().random_int(1, 5)
	duration = random.choice([30, 60])
	num_questions = faker.Faker().random_int()
	num_answers = faker.Faker().random_int(1, 6)
	lang = random.choice(['Ru', 'Kg'])
	is_active = True
	intro = faker.Faker().text()
