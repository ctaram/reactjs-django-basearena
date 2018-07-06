from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestTodoView(APITestCase):

    fixtures = ["note.json"]

    def test_todo_api(self):
        response = self.client.get(reverse('note-list'), format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_todo_archive(self):
        response = self.client.delete(reverse('note-archive', args={1}), format='json')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
