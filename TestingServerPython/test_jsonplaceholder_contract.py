import unittest
import pytest
import requests


class TestJSONPlaceholderContract(unittest.TestCase):

    BASE_URL = "https://jsonplaceholder.typicode.com"
    @pytest.mark.contract
    def test_get_single_post_contract(self):
        post_id = 1
        expected_post_data = {
            "userId": 1,
            "id": post_id,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        }

        response = requests.get(f"{self.BASE_URL}/posts/{post_id}")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.headers["Content-Type"], "application/json; charset=utf-8")

        post_data = response.json()
        self.assertEqual(post_data, expected_post_data)

    @pytest.mark.contract
    def test_get_all_posts_contract(self):
        response = requests.get(f'{self.BASE_URL}/posts')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    @pytest.mark.contract
    def test_create_post_contract(self):
        data = {
            'title': 'foo',
            'body': 'bar',
            'userId': 1
        }
        response = requests.post(f'{self.BASE_URL}/posts', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json())

    @pytest.mark.contract
    def test_update_post_contract(self):
        data = {
            'id': 1,
            'title': 'foo',
            'body': 'bar',
            'userId': 1
        }
        response = requests.put(f'{self.BASE_URL}/posts/1', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], 'foo')

    @pytest.mark.contract
    def test_patch_post_contract(self):
        data = {
            'title': 'foo'
        }
        response = requests.patch(f'{self.BASE_URL}/posts/1', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], 'foo')

    @pytest.mark.contract
    def test_delete_post_contract(self):
        response = requests.delete(f'{self.BASE_URL}/posts/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
