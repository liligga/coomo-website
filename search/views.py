from django.db.models import Q
from django.http import JsonResponse
from rest_framework.views import APIView
from news.models import News
from online_test.models import OnlineTest
from pages.models import Page
from reports.models import Reports
from search.serializers import SearchNewsSerializer, OnlineTestSearchSerializer, ReportsSearchSerializer, \
    CourseSearchSerializer, PageSearchSerializer
from videocourses.models import Course


class GlobalSearchList(APIView):
    """
    Принимает GET-запрос с параметром 'query'
    например '/api/search/?query=запрос'
    """

    def get(self, request):
        query = request.GET.get('query')

        if query:
            news = News.objects.filter(Q(title__icontains=query) | Q(article__icontains=query))
            tests = OnlineTest.objects.filter(Q(name__icontains=query))
            reports = Reports.objects.filter(Q(title__icontains=query))
            courses = Course.objects.filter(Q(name__icontains=query))
            # pages = Page.objects.filter(Q(title__icontains=query))
            return JsonResponse({'news': SearchNewsSerializer(instance=news, many=True).data,
                                 'tests': OnlineTestSearchSerializer(instance=tests, many=True).data,
                                 'reports': ReportsSearchSerializer(instance=reports, many=True).data,
                                 'courses': CourseSearchSerializer(instance=courses, many=True).data,
                                 # 'pages': PageSearchSerializer(instance=pages, many=True).data,
                                 })

        return JsonResponse(status=404, data={'message': 'Ничего не найдено'})
