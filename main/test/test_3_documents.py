from django.test import TestCase, SimpleTestCase
from main.models import Role, User, Document

from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

import json
from django.core.management import call_command


class ViewTestCase(SimpleTestCase):
    """Test suite for the api views"""

    @classmethod
    def setUpClass(cls):
        admin = Role.objects.create(name='admin')
        regular = Role.objects.create(name='regular')

        cls.admin_user = User.objects.create_superuser(
            username='admin-user',
            email='boss@g.com',
            password='password',
            role_id=admin,
        )
        cls.regular_user = User(
            username='reg-user',
            email='boss@g.com',
            role_id=regular)
        cls.regular_user.set_password('password')
        cls.regular_user.save()
        print('\n ==== Start Document Tests ====')

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin_user)

    def test_16_api_can_create_a_document(self):
        """Api can create a document"""
        res = self.client.post(
            reverse('document_list_create'),
            {'title': 'test title', 'content': 'test content'},
            format='json',
        )
        data = json.loads(res.content)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data['title'], 'test title')
        for key in ['id', 'user', 'content', 'access', 'createdAt']:
            assert key in data

    def test_17_api_can_get_documents(self):
        """Api can get a document"""
        self.client.post(
            reverse('document_list_create'),
            {'title': 'test title2', 'content': 'test content'},
            format='json',
        )
        res = self.client.get(reverse('document_list_create'))
        assert len(json.loads(res.content)['rows']) > 1

    def test_18_api_can_limit_the_number_of_documents(self):
        """Api can limit the number of documents returned"""
        res = self.client.get('/documents?limit=1')
        data = json.loads(res.content)
        assert len(data['rows']) == 1
        assert data['rows'][0]['id'] == 2

    def test_19_api_can_offset_the_number_of_documents(self):
        """Api supports offsets for documents"""
        res = self.client.get('/documents?offset=1')
        assert json.loads(res.content)['rows'][0]['id'] == 1

    def test_20_api_can_get_a_document(self):
        """Api can get a particular document"""
        res = self.client.get(
            '/documents/1',
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        assert json.loads(res.content)['id'] == 1

    def test_21_api_can_update_document(self):
        """Api can update a particular document"""
        res = self.client.put(
            '/documents/2',
            {'title': 'new_name'},
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        assert json.loads(res.content)['title'] == 'new_name'

    def test_22_authorization_is_enforced(self):
        """Authorization is enforced"""
        new_user = User.objects.create(username='nice-guy',
                                       password='password')
        self.client.force_authenticate(user=new_user)
        res = self.client.put(
            '/documents/2',
            {'title': 'kenpachi'},
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_23_api_can_delete_user(self):
        """Api can delete a particular document"""
        response = self.client.delete(
            '/documents/2',
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    @classmethod
    def tearDownClass(cls):
        call_command('flush', interactive=False)
