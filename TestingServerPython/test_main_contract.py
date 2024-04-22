import unittest
from unittest.mock import patch
import sys
sys.path.append('E:/TestingProject/TestingProject/TestingServerPython')
import main





class TestMainContract(unittest.TestCase):

    @patch('main.requests.get')
    def test_get_posts_contract(self, mock_get):
        # Ustawiamy mocka dla funkcji requests.get
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {
                "userId": 1,
                "id": 1,
                "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
            }
        ]

        # Wywołujemy funkcję, którą testujemy
        response = main.get_posts(1)

        # Sprawdzamy, czy funkcja zwraca oczekiwane dane
        self.assertEqual(response, mock_get.return_value.json.return_value)

    @patch('main.requests.get')
    def test_get_albums_contract(self, mock_get):
        # Ustawiamy mocka dla funkcji requests.get
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {
                "userId": 1,
                "id": 1,
                "title": "quidem molestiae enim"
            }
        ]

        # Wywołujemy funkcję, którą testujemy
        response = main.get_albums(1)

        # Sprawdzamy, czy funkcja zwraca oczekiwane dane
        self.assertEqual(response, mock_get.return_value.json.return_value)

    @patch('main.requests.get')
    def test_get_users_contract(self, mock_get):
        # Ustawiamy mocka dla funkcji requests.get
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {
                "id": 1,
                "name": "Leanne Graham"
            }
        ]

        # Wywołujemy funkcję, którą testujemy
        response = main.get_users()

        # Sprawdzamy, czy funkcja zwraca oczekiwane dane
        self.assertEqual(response, mock_get.return_value.json.return_value)

    @patch('main.requests.get')
    def test_get_photos_contract(self, mock_get):
        # Ustawiamy mocka dla funkcji requests.get
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {
                "albumId": 1,
                "id": 1,
                "title": "accusamus beatae ad facilis cum similique qui sunt",
                "url": "https://via.placeholder.com/600/92c952",
                "thumbnailUrl": "https://via.placeholder.com/150/92c952"
            }
        ]

        # Wywołujemy funkcję, którą testujemy
        response = main.get_photos()

        # Sprawdzamy, czy funkcja zwraca oczekiwane dane
        self.assertEqual(response, mock_get.return_value.json.return_value)

    @patch('main.requests.get')
    def test_get_post_comments_contract(self, mock_get):
        # Ustawiamy mocka dla funkcji requests.get
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {
                "postId": 1,
                "id": 1,
                "name": "id labore ex et quam laborum",
                "email": "Eliseo@gardner.biz",
                "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
            }
        ]

        # Wywołujemy funkcję, którą testujemy
        response = main.get_post_comments(1)

        # Sprawdzamy, czy funkcja zwraca oczekiwane dane
        self.assertEqual(response, mock_get.return_value.json.return_value)

if __name__ == '__main__':
    unittest.main()
