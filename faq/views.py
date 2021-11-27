from rest_framework.generics import ListAPIView

from faq.models import FAQ
from faq.serializers import FAQSerializer


class FAQListView(ListAPIView):
    queryset = FAQ.objects.all().order_by('id')
    serializer_class = FAQSerializer
