from django.urls import path
from .views import ReportsView, ReportsDetailView

urlpatterns = [
	path('api/reports/',ReportsView.as_view(), name="reports_list"),
	path('api/reports/{id}',ReportsDetailView.as_view(), name="reports_detail"),
]
