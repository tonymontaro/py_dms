from django.test import TestCase
from main.models import Role, User

from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

import json
from django.core.management import call_command


class ViewTestCase(TestCase):
    """Test suite for the api views"""

    @classmethod
    def setUpClass(cls):
        admin = Role.objects.get(name='admin')
        regular = Role.objects.get(name='regular')

        cls.admin_user = User.objects.create_superuser(
            username='admin-user',
            email='boss@g.com',
            password='password',
            role_id=admin
        )
        cls.regular_user = User.objects.create(
            username='reg-user',
            email='boss@g.com',
            password='password',
            role_id=regular
        )
        print('\n ==== Start Role Tests ====')

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin_user)

    def test_01_api_can_create_a_role(self):
        """Api can create a role"""
        res = self.client.post(
            reverse('role_list_create'),
            {'name': 'editor'},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(res.content)['name'], 'editor')

    def test_02_authorization_is_enforced(self):
        """Authorization is enforced"""
        self.client.force_authenticate(user=self.regular_user)
        res = self.client.post('/roles', {'name': 'loafers'}, format='json')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_03_should_fail_if_role_exists(self):
        res = self.client.post('/roles', {'name': 'regular'}, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(res.content)['name'][0],
                         'role with this name already exists.')

    def test_04_api_can_get_a_role(self):
        """Api can get a role"""
        response = self.client.get(
            '/roles/',
            kwargs={'pk': 1},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, Role.objects.get(name='admin'))

    def test_05_api_can_update_role(self):
        """"Api can update role"""
        res = self.client.put(
            reverse('role_details', kwargs={'pk': 2}),
            {'name': 'new_role'},
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(res.content, {'id': 2, 'name': 'new_role'})

    def test_06_api_can_delete_role(self):
        """Api can delete role"""
        response = self.client.delete(
            reverse('role_details', kwargs={'pk': 2}),
            format='json',
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    @classmethod
    def tearDownClass(cls):
        call_command('flush', interactive=False)

