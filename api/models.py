from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Folder(models.Model):
    name = models.CharField(max_length=100)
    parent_folder = models.ForeignKey(
        "self", blank=True, null=True, related_name="subfolders"
    )

    def __str__(self):
        return self.name


class Document(models.Model):
    document = models.FileField()
    short_description = models.CharField(max_length=100)
    long_description = models.TextField()
    topics = models.ManyToManyField(Topic, related_name="documents")

    def __str__(self):
        return self.document.file.name
