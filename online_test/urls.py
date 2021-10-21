from django.urls import path
from .views import *
from . import views



urlpatterns = [
	path('api/tests', views.OnlineTestListView.as_view(), name="tests_list"),
	path('api/tests/<int:pk>/', views.OnlineTestDetailView.as_view(), name = 'test_detail'),
	path('api/test/<int:pk>', views.CheckAnswerTestView.as_view(), name = 'answerstest'),
]