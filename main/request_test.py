"""
Run this test with: pytest -vs request_test.py
-v means: verbose
-s means: print custom messages to the console
"""

import unittest
import requests
from requests.auth import HTTPBasicAuth

url = 'http://localhost:8000'
token = ''
role_id = None


class TestRoleApi(unittest.TestCase):
    def test_01_post_role(self):
        global role_id
        req = {'name': 'test-role'}
        res = requests.post(url + '/roles/new', json=req,
                            auth=HTTPBasicAuth('montaro', 'anthonidas')).json()
        role_id = res['id']
        assert res['name'] == 'test-role'

    def test_02_put_role(self):
        global role_id
        req = {'name': 'test-role2'}
        res = requests.put('{}/roles/{}'.format(url, role_id), json=req,
                           auth=HTTPBasicAuth('montaro', 'anthonidas')).json()
        assert res['name'] == 'test-role2'
        assert res['id'] == role_id

    def test_03_get_role(self):
        res = requests.get('{}/roles/{}'.format(url, role_id),
                           auth=HTTPBasicAuth('montaro', 'anthonidas')).json()
        assert res['name'] == 'test-role2'
        assert res['id'] == role_id

    def test_08_get_roles(self):
        res = requests.get(url + '/roles').json()
        assert len(res) > 0

    def test_05_delete_role(self):
        res = requests.delete('{}/roles/{}'.format(url, role_id),
                              auth=HTTPBasicAuth('montaro', 'anthonidas'))
        assert res.status_code == 204

