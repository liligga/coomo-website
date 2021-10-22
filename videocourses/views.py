from django_filters.rest_framework import DjangoFilterBackend
from .models import Course
from rest_framework import generics
from .serializers import CoursesListSerializer, CourseDetailSerializer


class CourseListView(generics.ListAPIView):
	queryset = Course.objects.all()
	serializer_class = CoursesListSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['lang_course']
	'''http://*?lang_course=En должно быть после всей ссылки,
	course_list?lang_course=En'''


class CourseDetailView(generics.RetrieveAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseDetailSerializer
