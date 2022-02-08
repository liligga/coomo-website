from rest_framework.response import Response
from rest_framework.views import APIView
from pages.serializers import PageSerializer
from .serializers import MenuSerializer, FooterSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from .models import MenuLink, FooterLink


class MenuLinksView(generics.ListAPIView):
    serializer_class = MenuSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['lang']

    def get_queryset(self):
        query = self.request.META.get('HTTP_ACCEPT_LANGUAGE', 'Ru').capitalize()
        if query:
            queryset = MenuLink.active_objects.filter(lang=query)
        else:
            queryset = MenuLink.active_objects.filter(lang='Ru')

        return queryset


class FooterLinksView(generics.ListAPIView):
    serializer_class = FooterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['lang']

    def get_queryset(self):
        query = self.request.META.get('HTTP_ACCEPT_LANGUAGE', 'Ru').capitalize()
        if query:
            queryset = FooterLink.active_objects.filter(lang=query)
        else:
            queryset = FooterLink.active_objects.filter(lang='Ru')

        return queryset


class About(APIView):
    serializer_class = PageSerializer
    filter_backends = [DjangoFilterBackend]

    def get(self, request, *args, **kwargs):
        query = request.META.get('HTTP_ACCEPT_LANGUAGE', 'Ru').capitalize()
        try:
            menu_page = MenuLink.objects.filter(position='about', lang=query).first().page
        except:
            return Response(PageSerializer(None).data, status=status.HTTP_404_NOT_FOUND)
        page = PageSerializer(menu_page)
        return Response(page.data)
