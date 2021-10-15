from django.urls import path
from .views import *
from . import views



urlpatterns = [
	path('api/tests', views.OnlineTestListView.as_view(), name="tests_list"),

]