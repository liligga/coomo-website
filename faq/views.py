from rest_framework.generics import ListAPIView

from faq.models import FAQ
from faq.serializers import FAQSerializer


class FAQListView(ListAPIView):
    # queryset = FAQ.objects.all().order_by('id')
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.META.get('HTTP_ACCEPT_LANGUAGE').capitalize()
        print(lang)
        queryset = FAQ.objects.filter(lang=lang).order_by('id')
        return queryset
