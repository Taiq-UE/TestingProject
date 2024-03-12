from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Dodajemy obsługę CORS

@app.route('/<int:limit>')
def get_posts(limit):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts?_limit={limit}')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'An error occurred while fetching posts'}), 500

if __name__ == '__main__':
    app.run(port=8080)