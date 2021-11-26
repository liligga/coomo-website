from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class ReportsView(APIView):
    def get(self, request):
        reports = Reports.objects.all()
        serializer = ReportsSerializer(reports, many=True)
        context = {"reports": serializer.data}
        return Response(context)