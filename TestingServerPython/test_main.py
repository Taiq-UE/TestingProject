import unittest
from unittest.mock import patch
from main import get_albums, get_users, get_photos, get_post_comments, get_posts

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

    @patch('main.requests.get')
    def test_get_albums(self, mock_get):
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
        response = get_albums(1)

        # Sprawdzamy, czy funkcja zwraca oczekiwane dane
        self.assertEqual(response, mock_get.return_value.json.return_value)

    @patch('main.requests.get')
    def test_get_albums_status_code_not_200(self, mock_get):
        # Ustawiamy mocka dla funkcji requests.get
        mock_get.return_value.status_code = 500

        # Wywołujemy funkcję, którą testujemy
        response = get_albums(1)

        # Sprawdzamy, czy funkcja zwraca odpowiednią odpowiedź
        self.assertEqual(response, ({'error': 'An error occurred while fetching albums'}, 500))

    @patch('main.requests.get')
    def test_get_users(self, mock_get):
        # Ustawiamy mocka dla funkcji requests.get
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {
                "id": 1,
                "name": "Leanne Graham"
            }
        ]

        # Wywołujemy funkcję, którą testujemy
        response = get_users()

        # Sprawdzamy, czy funkcja zwraca oczekiwane dane
        self.assertEqual(response, mock_get.return_value.json.return_value)

    @patch('main.requests.get')
    def test_get_users_status_code_not_200(self, mock_get):
        # Ustawiamy mocka dla funkcji requests.get
        mock_get.return_value.status_code = 500

        # Wywołujemy funkcję, którą testujemy
        response = get_users()

        # Sprawdzamy, czy funkcja zwraca odpowiednią odpowiedź
        self.assertEqual(response, ({'error': 'An error occurred while fetching users'}, 500))

    @patch('main.requests.get')
    def test_get_photos(self, mock_get):
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
        response = get_photos()

        # Sprawdzamy, czy funkcja zwraca oczekiwane dane
        self.assertEqual(response, mock_get.return_value.json.return_value)

    @patch('main.requests.get')
    def test_get_photos_status_code_not_200(self, mock_get):
        # Ustawiamy mocka dla funkcji requests.get
        mock_get.return_value.status_code = 500

        # Wywołujemy funkcję, którą testujemy
        response = get_photos()

        # Sprawdzamy, czy funkcja zwraca odpowiednią odpowiedź
        self.assertEqual(response, ({'error': 'An error occurred while fetching photos'}, 500))

    @patch('main.requests.get')
    def test_get_post_comments(self, mock_get):
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
        response = get_post_comments(1)

        # Sprawdzamy, czy funkcja zwraca oczekiwane dane
        self.assertEqual(response, mock_get.return_value.json.return_value)

    @patch('main.requests.get')
    def test_get_post_comments_status_code_not_200(self, mock_get):
        # Ustawiamy mocka dla funkcji requests.get
        mock_get.return_value.status_code = 500

        # Wywołujemy funkcję, którą testujemy
        response = get_post_comments(1)

        # Sprawdzamy, czy funkcja zwraca odpowiednią odpowiedź
        self.assertEqual(response, ({'error': 'An error occurred while fetching photos'}, 500))

if __name__ == '__main__':
    unittest.main()
