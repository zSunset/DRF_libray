from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory, APIClient, force_authenticate
from mixer.backend.django import mixer
from rest_framework import status
from TODO.views import ToDo_notesModelViewSet
from django.contrib.auth.models import User
from authors.models import CustomUser
import json


class CustomUserAPIClient(TestCase):

    def test_creat_custom_user(self):
        user = mixer.blend(CustomUser)
        client = APIClient()
        response = client.put(f'/appuser/{user.id}/', {'username': 'Fil'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ToDoNotesAPIRequestFactory(TestCase):

    def test_get_todo_notes(self):
        factory = APIRequestFactory()
        request = factory.get('/todonotes/', {'header': ''}, format='json')
        view = ToDo_notesModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class ProjectApiTestCase(APITestCase):
    
    def test_get_project(self):
        response = self.client.get('/project/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)