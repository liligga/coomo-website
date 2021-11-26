from django.db.models import Q
from django.http import JsonResponse
from rest_framework.views import APIView
from menu.models import MenuLink
from news.models import News
from online_test.models import OnlineTest
from reports.models import Reports
from search.serializers import SearchNewsSerializer, OnlineTestSearchSerializer, ReportsSearchSerializer, \
    CourseSearchSerializer, MenuSearchSerializer
from videocourses.models import Course


class GlobalSearchList(APIView):
    """
    Принимает GET-запрос с параметром 'query'
    например '/api/search/?query=запрос'
    """

    def get(self, request):
        query = request.GET.get('query')
        news = News.objects.all()
        tests = OnlineTest.objects.all()
        reports = Reports.objects.all()
        courses = Course.objects.all()
        links = MenuLink.objects.all()

        if query:
            news = news.filter(Q(title__icontains=query) | Q(article__icontains=query))
            tests = tests.filter(Q(name__icontains=query))
            reports = reports.filter(Q(title__icontains=query) | Q(article__icontains=query))
            courses = courses.filter(Q(name__icontains=query))
            links = links.filter(Q(title__icontains=query))

        return JsonResponse({'news': SearchNewsSerializer(instance=news, many=True).data,
                             'tests': OnlineTestSearchSerializer(instance=tests, many=True).data,
                             'reports': ReportsSearchSerializer(instance=reports, many=True).data,
                             'courses': CourseSearchSerializer(instance=courses, many=True).data,
                             'links': MenuSearchSerializer(instance=links, many=True).data,
                             })