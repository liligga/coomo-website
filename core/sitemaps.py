from django.contrib.sitemaps import Sitemap

from news.models import News
from online_test.models import OnlineTest
from pages.models import Page
from reports.models import Reports


class NewsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return News.objects.all()

    def lastmod(self, obj):
        return obj.created

    def location(self, item):
        return f'/api/news/{item.slug}'


class OnlineTestSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return OnlineTest.objects.all().order_by('id')

    def location(self, item):
        return f'/api/tests/{item.id}'


class ReportsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Reports.objects.all().order_by('id')

    def location(self, item):
        return f'/api/reports/{item.slug}'


class PagesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Page.objects.all().order_by('id')

    def location(self, item):
        return f'/api/pages/{item.slug}'
