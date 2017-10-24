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
        print('\n ==== Start User Tests ====')

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin_user)

    def test_07_api_can_login_a_user(self):
        """Api can log a user in and return a token"""
        res = self.client.post(
            reverse('login'),
            {'username': 'reg-user', 'password': 'password'},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        assert len(json.loads(res.content)['token']) > 0

    def test_08_api_can_create_a_user(self):
        """Api can create a user"""
        res = self.client.post(
            reverse('user_list_create'),
            {'username': 'user_one', 'email': 'aa@ga.co',
             'password': 'password'},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(res.content)['username'], 'user_one')

    def test_09_api_can_get_users(self):
        """Api can get a list of users"""
        res = self.client.get(reverse('user_list_create'))
        assert len(json.loads(res.content)['rows']) > 1

    def test_10_api_can_limit_the_number_of_users(self):
        """Api can limit the number of users returned"""
        res = self.client.get('/users?limit=1')
        assert len(json.loads(res.content)['rows']) == 1
        assert json.loads(res.content)['rows'][0]['username'] == 'admin-user'

    def test_11_api_can_offset_the_number_of_users(self):
        """Api supports offsets for users"""
        res = self.client.get('/users?offset=1')
        assert json.loads(res.content)['rows'][0]['username'] == 'reg-user'

    def test_12_api_can_get_a_user(self):
        """Api can get a particular user"""
        response = self.client.get(
            '/users',
            kwargs={'pk': 1},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, User.objects.get(pk=1))

    def test_13_api_can_update_user(self):
        """Api can update a particular user"""
        res = self.client.put(
            '/users/2',
            {'username': 'new_name', 'email': 'aa@ga.co',
             'password': 'password'},
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        assert json.loads(res.content)['username'] == 'new_name'

    def test_14_authorization_is_enforced(self):
        """Authorization is enforced"""
        new_user = User.objects.create(username='nice-guy',
                                       password='password')
        self.client.force_authenticate(user=new_user)
        res = self.client.put(
            '/users/2',
            {'username': 'another_name', 'email': 'aa@ga.co',
             'password': 'password'},
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_15_api_can_delete_user(self):
        """Api can delete a particular user"""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.delete(
            '/users/2',
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    @classmethod
    def tearDownClass(cls):
        call_command('flush', interactive=False)
