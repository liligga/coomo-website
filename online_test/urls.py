from django.urls import path, include
from .views import OnlineTestViewSet, CheckTestAnswersView, TestQuestionsView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tests', OnlineTestViewSet)


urlpatterns = [
<<<<<<< Updated upstream
	path('api/', include(router.urls)),
=======
    path('api/', include(router.urls)),
    # path('api/tests', OnlineTestListView.as_view(), name="online_tests"),
    path('api/tests/<int:pk>/questions', TestQuestionsView.as_view(), name="online_tests-questions"),
    path('api/tests/<int:pk>/answers', CheckTestAnswersView.as_view(), name="online_tests-answers"),
>>>>>>> Stashed changes
]
