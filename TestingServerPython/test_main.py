import unittest
from unittest.mock import patch
from main import get_posts

class TestMain(unittest.TestCase):

    @patch('main.requests.get')
    def test_get_posts(self, mock_get):
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
        response = get_posts(1)

        # Sprawdzamy, czy funkcja zwraca oczekiwane dane
        self.assertEqual(response, mock_get.return_value.json.return_value)

    @patch('main.requests.get')
    def test_get_posts_status_code_not_200(self, mock_get):
        # Ustawiamy mocka dla funkcji requests.get
        mock_get.return_value.status_code = 500

        # Wywołujemy funkcję, którą testujemy
        response = get_posts(1)

        # Sprawdzamy, czy funkcja zwraca odpowiednią odpowiedź
        self.assertEqual(response, ({'error': 'An error occurred while fetching posts'}, 500))

    @patch('main.requests.get')
    def test_get_posts_empty_json(self, mock_get):
        # Ustawiamy mocka dla funkcji requests.get
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = []

        # Wywołujemy funkcję, którą testujemy
        response = get_posts(1)

        # Sprawdzamy, czy funkcja zwraca pustą listę
        self.assertEqual(response, [])

    @patch('main.requests.get')
    def test_get_posts_invalid_json(self, mock_get):
        # Ustawiamy mocka dla funkcji requests.get
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'message': 'Invalid JSON'}

        # Wywołujemy funkcję, którą testujemy
        response = get_posts(1)

        # Sprawdzamy, czy funkcja zwraca odpowiednią odpowiedź
        self.assertEqual(response, {'message': 'Invalid JSON'})

if __name__ == '__main__':
    unittest.main()