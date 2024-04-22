import unittest
import requests
from unittest.mock import patch

class TestJSONPlaceholderContract(unittest.TestCase):

    def test_get_single_post_contract(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json())
        self.assertIn('title', response.json())
        self.assertIn('body', response.json())
        self.assertIn('userId', response.json())

    def test_get_all_posts_contract(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_post_contract(self):
        data = {
            'title': 'foo',
            'body': 'bar',
            'userId': 1
        }
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json())

    def test_update_post_contract(self):
        data = {
            'id': 1,
            'title': 'foo',
            'body': 'bar',
            'userId': 1
        }
        response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], 'foo')

    def test_patch_post_contract(self):
        data = {
            'title': 'foo'
        }
        response = requests.patch('https://jsonplaceholder.typicode.com/posts/1', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], 'foo')

    def test_delete_post_contract(self):
        response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
