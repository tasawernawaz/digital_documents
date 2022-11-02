from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APITestCase

from api.models import Document
from tests.factories import DocumentFactory, FolderFactory, TopicFactory


class DocumentViewSetTests(APITestCase):
    list_path = reverse("documents-list")
    detail_path = "documents-detail"

    def setUp(self):
        """Create a document."""
        super().setUp()
        self.folder = FolderFactory()
        self.topics = [TopicFactory.create(), TopicFactory.create()]
        self.document = DocumentFactory.create(folder=self.folder)
        self.document.topics.set(self.topics)

    def test_list_documents(self):
        """Verify list api of documents."""

        response = self.client.get(self.list_path)
        self.assertEqual(response.status_code, 200)
        docs_in_db = Document.objects.count()
        self.assertEqual(docs_in_db, 1)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], self.document.id)

    def test_delete_document(self):
        """Verify that delete API deletes a document."""
        # TODO check if files also deleted
        path = reverse(self.detail_path, kwargs={"pk": self.document.id})
        response = self.client.delete(path)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Document.objects.filter(id=self.document.id).count(), 0)

    def test_create_document(self):
        """Verify that users can create a document."""

        upload_file = SimpleUploadedFile("/file.txt", b"abc", content_type="text/plain")
        post_data = {
            "document": upload_file,
            "short_description": "test short description",
            "long_description": "test long description",
            "folder": self.folder.id,
            "topics": [self.topics[0].id],
        }
        response = self.client.post(
            reverse("documents-list"), data=post_data, format="multipart"
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Document.objects.get(pk=response.data["id"]))

    def test_update_document(self):
        """Verify that user can update document."""
        new_upload_file = SimpleUploadedFile(
            "/file.txt", b"abc", content_type="text/plain"
        )
        post_data = {
            "document": new_upload_file,
            "short_description": "updated - test short description",
            "long_description": "updated - test long description",
            "folder": self.folder.id,
            "topics": [self.topics[0].id],
        }
        response = self.client.put(
            reverse("documents-detail", args=(self.document.id,)),
            data=post_data,
            format="multipart",
        )
        self.assertEqual(response.status_code, 200)
        doc_in_db = Document.objects.get(pk=self.document.id)
        self.assertEqual(doc_in_db.short_description, post_data["short_description"])
