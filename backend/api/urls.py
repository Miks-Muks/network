from rest_framework.routers import DefaultRouter

from .views import TopicKaifViewSet

router = DefaultRouter()

router.register(r'topic', TopicKaifViewSet, basename='topic')

urlpatterns = router.urls
