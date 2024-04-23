from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    host = "http://127.0.0.1:8080"
    wait_time = between(1, 2.5)

    # Zadanie do pobierania postów z określonym limitem
    @task
    def get_posts(self):
        self.client.get("/posts/10")

    # Zadanie do pobierania albumów z określonym limitem
    @task
    def get_albums(self):
        self.client.get("/albums/10")

    # Zadanie do pobierania informacji o użytkownikach
    @task
    def get_users(self):
        self.client.get("/users")

    # Zadanie do pobierania zdjęć
    @task
    def get_photos(self):
        self.client.get("/photos")
    # Zadanie do pobierania komentarzy do określonego posta
    @task
    def get_post_comments(self):
        self.client.get("/posts/1/comments")