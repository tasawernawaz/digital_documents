from rest_framework import viewsets

from .models import Document, Folder, Topic
from .serializers import (DocumentReadSerializer, DocumentSerializer,
                          FolderSerializer, TopicSerializer)


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all().prefetch_related("topics")
    serializer_class = DocumentSerializer

    def get_serializer_class(self):
        if self.request.method in ["GET", "LIST"]:
            return DocumentReadSerializer

        return DocumentSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned documents to given folder and topics,
        by filtering against a `folder` and `topics` query parameter in the URL.
        """
        query_params = self.request.query_params
        folder = query_params.get("folder")
        topics = query_params.get("topics")

        if folder:
            self.queryset = self.queryset.filter(folder__name=folder)

        if topics:
            self.queryset = self.queryset.filter(
                topics__name__in=topics.split(",")
            ).distinct()

        return self.queryset
