import unittest
import pytest
import requests


class TestMainContract(unittest.TestCase):

    BASE_URL = "http://127.0.0.1:8080"

    @pytest.mark.contract
    def test_get_single_post_contract(self):
        post_id = 1
        expected_post_data = [{
            "userId": 1,
            "id": post_id,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        }]

        response = requests.get(f"{self.BASE_URL}/posts/{post_id}")

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.headers["Content-Type"].startswith("application/json"))

        post_data = response.json()
        self.assertEqual(post_data, expected_post_data)

    @pytest.mark.contract
    def test_get_albums_contract(self):
        album_id = 1
        expected_album_data = [{
            "userId": 1,
            "id": album_id,
            "title": "quidem molestiae enim"
        }]

        response = requests.get(f"{self.BASE_URL}/albums/{album_id}")

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.headers["Content-Type"].startswith("application/json"))

        album_data = response.json()
        self.assertEqual(album_data, expected_album_data)

    @pytest.mark.contract
    def test_get_users_contract(self):
        expected_user_data = [
            {"id": 1, "name": "Leanne Graham"},
            {"id": 2, "name": "Ervin Howell"},
            {"id": 3, "name": "Clementine Bauch"},
            {"id": 4, "name": "Patricia Lebsack"},
            {"id": 5, "name": "Chelsey Dietrich"},
            {"id": 6, "name": "Mrs. Dennis Schulist"},
            {"id": 7, "name": "Kurtis Weissnat"},
            {"id": 8, "name": "Nicholas Runolfsdottir V"},
            {"id": 9, "name": "Glenna Reichert"},
            {"id": 10, "name": "Clementina DuBuque"}
        ]

        response = requests.get(f"{self.BASE_URL}/users")

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.headers["Content-Type"].startswith("application/json"))

        user_data = response.json()
        user_data_simplified = [{"id": user["id"], "name": user["name"]} for user in user_data]
        self.assertEqual(user_data_simplified, expected_user_data)

    @pytest.mark.contract
    def test_get_photos_contract(self):
        response = requests.get(f"{self.BASE_URL}/photos")

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.headers["Content-Type"].startswith("application/json"))

        photos_data = response.json()

        self.assertIsInstance(photos_data, list)

        for photo in photos_data:
            self.assertIsInstance(photo, dict)
            self.assertIn('albumId', photo)
            self.assertIn('id', photo)
            self.assertIn('title', photo)
            self.assertIn('url', photo)
            self.assertIn('thumbnailUrl', photo)

    @pytest.mark.contract
    def test_get_post_comments_contract(self):
        post_id = 1

        response = requests.get(f"{self.BASE_URL}/posts/{post_id}/comments")

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.headers["Content-Type"].startswith("application/json"))

        comments_data = response.json()

        self.assertIsInstance(comments_data, list)

        for comment in comments_data:
            self.assertIsInstance(comment, dict)
            self.assertIn('postId', comment)
            self.assertIn('id', comment)
            self.assertIn('name', comment)
            self.assertIn('email', comment)
            self.assertIn('body', comment)

if __name__ == '__main__':
    unittest.main()
