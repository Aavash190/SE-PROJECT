from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task


class TaskAPITests(APITestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="Finish SE Project",
            description="Complete the simple Task API implementation",
            due_date="2026-08-31",
            status="in_progress",
            priority="high",
        )
        self.list_url = reverse("task-list")

    # Test to check if listing tasks works and returns HTTP 200
    def test_list_tasks(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # Test to check if creating a new task works and increments count
    def test_create_task(self):
        payload = {
            "title": "Clean Code Reading",
            "description": "Read Chapter 1",
            "due_date": "2026-09-05",
            "status": "pending",
            "priority": "low",
        }
        response = self.client.post(self.list_url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    # Test to check if retrieving a single task detail works
    def test_retrieve_task(self):
        url = reverse("task-detail", args=[self.task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Finish SE Project")

    # Test to check if updating a task field works correctly
    def test_update_task(self):
        url = reverse("task-detail", args=[self.task.id])
        response = self.client.patch(url, {"status": "completed"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.status, "completed")

    # Test to check if deleting a task works and database is updated
    def test_delete_task(self):
        url = reverse("task-detail", args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    # Test to verify validation fails and returns bad request if due_date is missing
    def test_create_task_missing_due_date_fails(self):
        payload = {
            "title": "Invalid Task",
            "status": "pending",
        }
        response = self.client.post(self.list_url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test to check the string representation (__str__) of Task model
    def test_task_str(self):
        task = Task.objects.create(
            title="Test Task",
            due_date="2026-08-23",
        )
        self.assertEqual(str(task), "Test Task")
