import os
import json
import django
from django.apps import apps
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

# Create your tests here.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


class SubjectViewSetTests(TestCase):

    def setUp(self):
        self.subject_model = apps.get_model('education_process', 'Subject')
        self.subject_data_1 = {
            'name': 'Math'
        }
        self.subject_data_2 = {
            'name': 'History',
        }
        self.subject_1 = self.subject_model.objects.create(**self.subject_data_1)
        self.subject_2 = self.subject_model.objects.create(**self.subject_data_2)

    def test_list_subject(self):
        print(3 * '______________________test_list_')
        response = self.client.get(path=reverse('subject-list'))
        subjects = response.data
        print(subjects)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertTrue(isinstance(subjects, list))

        self.assertEqual(len(subjects), 2)

        self.assertEqual(subjects[0]['id'], self.subject_1.id)
        self.assertEqual(subjects[0]['name'], self.subject_1.name)

        self.assertEqual(subjects[1]['id'], self.subject_2.id)
        self.assertEqual(subjects[1]['name'], self.subject_2.name)

    def test_create_subject(self):
        print(3 * '______________________test_create_')
        subject_data = {
            'name': 'Biology',
        }
        response = self.client.post(reverse('subject-list'), subject_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        subject = self.subject_model.objects.get(name=subject_data['name'])
        print(subject)

        self.assertEqual(subject.name, subject_data['name'])

    def test_retrieve_subject(self):
        print(3 * '______________________test_retrieve_')
        response = self.client.get(path=reverse('subject-detail', args=[self.subject_1.id]))
        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.subject_1.name)

    def test_update_subject(self):
        print(3 * '______________________test_update_')
        updated_data = {
            'name': 'English'
        }
        response = self.client.patch(
            reverse('subject-detail', args=[self.subject_1.id]),
            data=json.dumps(updated_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(updated_data['name'], response.data['name'])

        updated_subject = self.subject_model.objects.get(id=self.subject_1.id)
        print(response.data)

        self.assertEqual(updated_data['name'], updated_subject.name)

        self.assertTrue(self.subject_1.name != updated_subject.name)

    def test_delete_subject(self):
        print(3 * '______________________test_delete_')
        response = self.client.delete(reverse('subject-detail', args=[self.subject_1.id]))
        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(ObjectDoesNotExist):
            deleted_subject = self.subject_model.objects.get(id=self.subject_1.id)
