from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Dodajemy obsługę CORS

@app.route('/posts/<int:limit>')
def get_posts(limit):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts?_limit={limit}')
    if response.status_code != 200:
        return {'error': 'An error occurred while fetching posts'}, 500
    return response.json()

@app.route('/albums/<int:limit>')
def get_albums(limit):
    response = requests.get(f'https://jsonplaceholder.typicode.com/albums?_limit={limit}')
    if response.status_code != 200:
        return {'error': 'An error occurred while fetching albums'}, 500
    return response.json()

@app.route('/users')
def get_users():
    response = requests.get(f'https://jsonplaceholder.typicode.com/users')
    if response.status_code != 200:
        return {'error': 'An error occurred while fetching users'}, 500
    return response.json()

@app.route('/photos')
def get_photos():
    response = requests.get(f'https://jsonplaceholder.typicode.com/photos')
    if response.status_code != 200:
        return {'error': 'An error occurred while fetching photos'}, 500
    return response.json()

@app.route('/post/<int:post_id>/comments')
def get_post_comments(post_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments')
    if response.status_code != 200:
        return {'error': 'An error occurred while fetching comments'}, 500
    return response.json()


if __name__ == '__main__':
    app.run(port=8080)