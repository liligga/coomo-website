from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .serializers import CoursesListSerializer, CourseDetailSerializer
from .models import Course, Video
from rest_framework.response import Response


class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['lang']

    def get(self, request, *args, **kwargs):
        courses = self.queryset.order_by('lang', '-id').values('name', 'id', 'lang')
        data = {}
        for item in courses:
            data.setdefault(item['name'], {})[item['lang']] = item
        return Response(data)


class CourseDetailView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
# def get_object(self, pk):
# 	try:
# 		return Video.objects.filter(course=pk)
# 	except Video.DoesNotExist:
# 		raise Http404

# def get(self, request, pk):
# 	videos = self.get_object(pk)
# 	course = Course.objects.get(pk=pk)
# 	data = [v for v in videos.values('name','video_link')]
# 	return Response({'name': course.name, 'videos': data})
