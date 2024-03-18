document.addEventListener('DOMContentLoaded', () => {
  const postsContainer = document.getElementById('postsContainer');
  const postsButton = document.getElementById('postsButton');
  const albumsButton = document.getElementById('albumsButton');
  const filterInput = document.getElementById('filterInput');
  const minCharCountInput = document.getElementById('minCharCount');
  const maxCharCountInput = document.getElementById('maxCharCount');

  let minCharCount = 0;
  let maxCharCount = Number.MAX_SAFE_INTEGER;

  // Funkcja do pobierania postów z API z ograniczeniem liczby postów
    function fetchPosts(minCharCount = 0, maxCharCount = Number.MAX_SAFE_INTEGER) {
        const urlParams = new URLSearchParams(window.location.search);
        const limit = urlParams.has('limit') ? Number(urlParams.get('limit')) : 100;

        fetch('https://jsonplaceholder.typicode.com/users')
            .then(response => response.json())
            .then(users => {
                fetch(`https://jsonplaceholder.typicode.com/posts?_limit=${limit}`)
                    .then(response => response.json())
                    .then(posts => {

                        // Sprawdź, czy pola wprowadzania danych są puste
                        const minCharCountInputValue = minCharCountInput.value.trim();
                        const maxCharCountInputValue = maxCharCountInput.value.trim();

                        // Jeśli pole wprowadzania danych jest puste, użyj domyślnej wartości
                        minCharCount = minCharCountInputValue !== '' ? Number(minCharCountInputValue) : minCharCount;
                        maxCharCount = maxCharCountInputValue !== '' ? Number(maxCharCountInputValue) : maxCharCount;

                        console.log(`Min Char Count: ${minCharCount}, Max Char Count: ${maxCharCount}`);

                        posts = posts.filter(post => {
                            const postLength = post.body.length;
                            return postLength >= minCharCount && postLength <= maxCharCount;
                        });

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
                          `;
                          postsContainer.appendChild(postElement);

                          // Pobieranie i wyświetlanie komentarzy dla posta
                          fetch(`https://jsonplaceholder.typicode.com/posts/${post.id}/comments`)
                              .then(response => response.json())
                              .then(comments => {
                                  const commentsContainer = document.createElement('div');
                                  commentsContainer.classList.add('commentsContainer');
                                  commentsContainer.innerHTML = '<h4>Comments:</h4>';
                                  comments.forEach(comment => {
                                      const commentElement = document.createElement('div');
                                      commentElement.classList.add('comment');
                                      commentElement.innerHTML = `
                                          <h5>${comment.name} (${comment.email})</h5>
                                          <p>${comment.body}</p>
                                      `;
                                      commentsContainer.appendChild(commentElement);
                                  });
                                  postElement.appendChild(commentsContainer);
                              });
                      });
                  });
          })
          .catch(error => {
              console.error('Error fetching data:', error);
          });
  }

  // Funkcja do pobierania albumów z API z ograniczeniem liczby albumów
  function fetchAlbums(limit = 10) {
      fetch('https://jsonplaceholder.typicode.com/users')
          .then(response => response.json())
          .then(users => {
              fetch(`https://jsonplaceholder.typicode.com/albums?_limit=${limit}`)
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

  fetchPosts();

  postsButton.addEventListener('click', () => fetchPosts());
  albumsButton.addEventListener('click', () => fetchAlbums());

  // Nasłuchuj zdarzenia input dla pola filtrującego
  filterInput.addEventListener('input', () => {
      const filterValue = filterInput.value.trim();
      if (filterValue === '') {
          fetchPosts(); // Jeśli pole filtrujące jest puste, pobierz wszystkie posty
      } else {
          // W przeciwnym razie pobierz posty, których treść zawiera wprowadzony filtr
          fetchPosts().then(posts => {
              posts = posts.filter(post => post.body.includes(filterValue));
              renderPosts(posts);
          });
      }
  });

});
