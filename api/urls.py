from django.urls import include, path
from rest_framework import routers

from .views import DocumentViewSet, FolderViewSet, TopicViewSet

router = routers.DefaultRouter()

router.register("topics", TopicViewSet, basename="topics")
router.register("folders", FolderViewSet, basename="folders")
router.register("documents", DocumentViewSet, basename="documents")

urlpatterns = [path("", include(router.urls))]
