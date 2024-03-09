document.addEventListener('DOMContentLoaded', () => {
  const postsContainer = document.getElementById('postsContainer');
  const postsButton = document.getElementById('postsButton');
  const albumsButton = document.getElementById('albumsButton');

  // Funkcja do pobierania postów z API
  function fetchPosts() {
      fetch('https://jsonplaceholder.typicode.com/users')
          .then(response => response.json())
          .then(users => {
              fetch('https://jsonplaceholder.typicode.com/posts')
                  .then(response => response.json())
                  .then(posts => {
                      postsContainer.innerHTML = ''; // Czyszczenie kontenera przed dodaniem nowych danych
                      posts.forEach(post => {
                          const postElement = document.createElement('div');
                          postElement.classList.add('post');
                          postElement.id = `post${post.id}`; // Dodanie identyfikatora dla elementu postu
                          const user = users.find(user => user.id === post.userId);
                          postElement.innerHTML = `
                              <h2>User: ${user ? user.name : 'Unknown'}</h2>
                              <h3>${post.title}</h3>
                              <p>${post.body}</p>
                              <div class="commentsContainer">
                                  <h4>Comments:</h4>
                                  <div id="comments${post.id}" class="comments"></div> <!-- Dodane id oraz klasa -->
                                  <form id="commentForm${post.id}" class="commentForm"> <!-- Dodany formularz z id -->
                                      <input type="text" id="commentName${post.id}" placeholder="Name">
                                      <input type="text" id="commentEmail${post.id}" placeholder="Email">
                                      <input type="text" id="commentBody${post.id}" placeholder="Comment">
                                      <button type="submit">Add Comment</button> <!-- Zmieniony button na submit -->
                                  </form>
                              </div>
                          `;
                          postsContainer.appendChild(postElement);

                          // Dodanie obsługi formularza komentarza dla danego postu
                          const commentForm = document.getElementById(`commentForm${post.id}`);
                          commentForm.addEventListener('submit', event => {
                              event.preventDefault(); // Zapobieganie domyślnej akcji formularza
                              const nameInput = document.getElementById(`commentName${post.id}`).value;
                              const emailInput = document.getElementById(`commentEmail${post.id}`).value;
                              const bodyInput = document.getElementById(`commentBody${post.id}`).value;
                              const commentData = {
                                  name: nameInput,
                                  email: emailInput,
                                  body: bodyInput
                              };
                              addComment(post.id, commentData); // Dodawanie komentarza
                          });

                          // Pobranie i wyświetlenie komentarzy dla danego postu
                          fetchComments(post.id);
                      });
                  })
                  .catch(error => {
                      console.error('Error fetching posts:', error);
                  });
          })
          .catch(error => {
              console.error('Error fetching users:', error);
          });
  }



  // Funkcja do pobierania albumów z API
  function fetchAlbums() {
    fetch('https://jsonplaceholder.typicode.com/users')
        .then(response => response.json())
        .then(users => {
            fetch('https://jsonplaceholder.typicode.com/albums')
                .then(response => response.json())
                .then(albums => {
                    fetch('https://jsonplaceholder.typicode.com/photos')
                        .then(response => response.json())
                        .then(photos => {
                            const postsContainer = document.getElementById('postsContainer');
                            postsContainer.innerHTML = ''; // Czyszczenie kontenera przed dodaniem nowych danych
                            albums.forEach(album => {
                                const albumElement = document.createElement('div');
                                albumElement.classList.add('album');
                                const user = users.find(user => user.id === album.userId);
                                albumElement.innerHTML = `
                                    <h2>${album.title}</h2>
                                    <p>User: ${user ? user.name : 'Unknown'}</p>
                                    <p>Album ID: ${album.id}</p>
                                    <div class="photosContainer"></div>
                                `;
                                const photosContainer = albumElement.querySelector('.photosContainer');
                                const albumPhotos = photos.filter(photo => photo.albumId === album.id);
                                albumPhotos.forEach(photo => {
                                    const photoElement = document.createElement('img');
                                    photoElement.src = photo.thumbnailUrl;
                                    photosContainer.appendChild(photoElement);
                                });
                                postsContainer.appendChild(albumElement);
                            });
                        })
                        .catch(error => {
                            console.error('Error fetching photos:', error);
                        });
                })
                .catch(error => {
                    console.error('Error fetching albums:', error);
                });
        })
        .catch(error => {
            console.error('Error fetching users:', error);
        });
}

function fetchComments(postId) {
  fetch(`https://jsonplaceholder.typicode.com/posts/${postId}/comments`)
      .then(response => response.json())
      .then(comments => {
          const postElement = document.getElementById(`post${postId}`); // Znajdowanie elementu postu
          const commentsContainer = postElement.querySelector('.commentsContainer'); // Znajdowanie kontenera komentarzy w danym poście
          commentsContainer.innerHTML = ''; // Czyszczenie kontenera przed dodaniem nowych danych
          comments.forEach(comment => {
              const commentElement = document.createElement('div');
              commentElement.classList.add('comment');
              commentElement.innerHTML = `
                  <strong>${comment.name}</strong> (${comment.email})<br>
                  ${comment.body}
              `;
              commentsContainer.appendChild(commentElement);
          });
      })
      .catch(error => {
          console.error(`Error fetching comments for post ${postId}:`, error);
      });
}

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
        const commentsContainer = postElement.querySelector('.comments');
        const commentElement = document.createElement('div');
        commentElement.className = 'comment';
        commentElement.innerHTML = `
            <strong>${comment.name}</strong> (${comment.email})<br>
            ${comment.body}
        `;
        commentsContainer.appendChild(commentElement);
    })
    .catch(error => {
        console.error('Error adding comment:', error);
    });
}



  // Nasłuchuj przycisków nawigacyjnych
  postsButton.addEventListener('click', fetchPosts);
  albumsButton.addEventListener('click', fetchAlbums);
});