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
        path = reverse(self.detail_path, kwargs={"pk": self.document.id})
        response = self.client.delete(path)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Document.objects.filter(id=self.document.id).count(), 0)

    def test_create_document(self):
        """Verify that users can create a document."""

        # Create a sample test file on the fly
        fpath = "testfile.txt"
        test_file = open(fpath, "w")
        test_file.write("Hello World!, this is a testing file.")
        test_file.close()
        test_file = open(fpath, "r")
        post_data = {
            "document": test_file,
            "short_description": "test short description",
            "long_description": "test long description",
            "folder": self.folder.id,
            "topics": self.topics[0].id,
        }

        response = self.client.post(
            reverse("documents-list"), data=post_data, format="json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Document.objects.get(pk=response.data["id"]))

    def test_update_document(self):
        """Verify that user can update document."""
        pass
