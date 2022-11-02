import factory
from factory import Faker

from api.models import Document, Folder, Topic


class TopicFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Topic

    name = Faker("word")


class FolderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Folder

    name = Faker("word")


class DocumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Document

    document = factory.django.FileField(filename="test_file.pdf")
    short_description = Faker("text")
    long_description = Faker("text")
