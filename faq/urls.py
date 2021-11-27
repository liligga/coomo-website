from django.urls import path

from faq.views import FAQListView

urlpatterns = [
    path('api/faq', FAQListView.as_view(), name='faq_list'),
]