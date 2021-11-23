from django.urls import path
from .views import ReportsView

urlpatterns = [
	path('api/reports/',ReportsView.as_view(), name="reports_list"),
]
