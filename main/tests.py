from django.test import TestCase
from .models import Role
#
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
#
from django.contrib.auth.models import User


# Create your tests here.


class ModelTestCase(TestCase):
    """Defines the test suite for the ROLE model."""

    def setUp(self):
        user = User.objects.create(username='nerd')
        self.role_name = 'editor'
        self.role = Role(name=self.role_name)

    def test_model_can_create_a_role(self):
        old_count = Role.objects.count()
        self.role.save()
        new_count = Role.objects.count()
        self.assertEqual(new_count, old_count + 1)


class ViewTestCase(TestCase):
    """Test suite for the api views"""

    def setUp(self):
        user = User.objects.create(username='nerd')
        admin_user = User.objects.create_superuser(username='boss', email='boss@g.com', password='password')
        self.client = APIClient()
        self.client.force_authenticate(user=admin_user)

        self.role_data = {'name': 'reviewer'}
        self.response = self.client.post(
            reverse('role_create'),
            self.role_data,
            format='json'
        )

    def test_api_can_create_a_role(self):
        """Api can create a role"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Authorization is enforced"""
        new_client = APIClient()
        res = new_client.post('/roles/new/', {'name': 'loafers'}, format='json')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_a_role(self):
        """Api can get a role"""
        role = Role.objects.first()
        response = self.client.get(
            '/roles/',
            kwargs={'pk': role.id},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, role)

    def test_api_can_update_role(self):
        """"Api can update role"""
        role = Role.objects.first()
        res = self.client.put(
            reverse('role_details', kwargs={'pk': role.id}),
            {'name': 'Something_new'},
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(res.content, {'id': role.id, 'name': 'Something_new'})

    def test_api_can_delete_role(self):
        """Api can delete role"""
        role = Role.objects.get()
        response = self.client.delete(
            reverse('role_details', kwargs={'pk': role.id}),
            format='json',
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
