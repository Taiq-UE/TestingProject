document.addEventListener('DOMContentLoaded', () => {
  const postsContainer = document.getElementById('posts');

  // Pobieranie postów z API
  fetch('https://jsonplaceholder.typicode.com/posts')
      .then(response => response.json())
      .then(posts => {
          posts.forEach(post => {
              // Tworzenie elementu div dla posta
              const postElement = document.createElement('div');
              postElement.className = 'post';
              postElement.dataset.postId = post.id;

              // Tworzenie nagłówka dla tytułu posta
              const titleElement = document.createElement('h2');
              titleElement.textContent = post.title;

              // Tworzenie paragrafu dla treści posta
              const bodyElement = document.createElement('p');
              bodyElement.textContent = post.body;

              // Tworzenie formularza do dodawania komentarzy
              const commentForm = document.createElement('form');
              commentForm.innerHTML = `
                  <input type="text" name="name" placeholder="Your name" required><br>
                  <input type="email" name="email" placeholder="Your email" required><br>
                  <textarea name="body" placeholder="Your comment" required></textarea><br>
                  <button type="submit">Add Comment</button>
              `;
              commentForm.addEventListener('submit', event => {
                  event.preventDefault();
                  const formData = new FormData(commentForm);
                  const commentData = Object.fromEntries(formData.entries());
                  addComment(post.id, commentData);
              });

              // Dodawanie elementów do posta
              postElement.appendChild(titleElement);
              postElement.appendChild(bodyElement);
              postElement.appendChild(commentForm);

              // Dodawanie posta do kontenera
              postsContainer.appendChild(postElement);
          });
      })
      .catch(error => {
          console.error('Error fetching posts:', error);
      });

  // Funkcja do dodawania komentarza
  function addComment(postId, commentData) {
      fetch(`https://jsonplaceholder.typicode.com/posts/${postId}/comments`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(commentData)
      })
      .then(response => response.json())
      .then(comment => {
          const postElement = document.querySelector(`.post[data-post-id="${postId}"]`);
          const commentsContainer = document.createElement('div');
          commentsContainer.className = 'comments';
          const commentElement = document.createElement('div');
          commentElement.className = 'comment';
          commentElement.innerHTML = `
              <strong>${comment.name}</strong> (${comment.email})<br>
              ${comment.body}
          `;
          commentsContainer.appendChild(commentElement);
          postElement.appendChild(commentsContainer);
      })
      .catch(error => {
          console.error('Error adding comment:', error);
      });
  }
});
