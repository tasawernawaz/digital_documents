from rest_framework import serializers

from .models import Document, Folder, Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    folder = FolderSerializer()
    topics = TopicSerializer(many=True)

    class Meta:
        model = Document
        fields = "__all__"
