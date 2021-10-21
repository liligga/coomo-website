from django.urls import path, include
from .views import OnlineTestViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tests', OnlineTestViewSet)


urlpatterns = [
	path('api/', include(router.urls)),

]