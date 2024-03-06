// app.js
window.onload = function() {
  const postsContainer = document.getElementById('posts');

  fetch('https://jsonplaceholder.typicode.com/posts')
    .then(response => response.json())
    .then(posts => {
      posts.forEach(post => {
        const postDiv = document.createElement('div');
        const title = document.createElement('h2');
        const body = document.createElement('p');

        title.textContent = 'Title: ' + post.title;
        body.textContent = 'Body: ' + post.body;

        postDiv.appendChild(title);
        postDiv.appendChild(body);

        // Pobierz komentarze dla tego posta
        fetch(`https://jsonplaceholder.typicode.com/comments?postId=${post.id}`)
          .then(response => response.json())
          .then(comments => {
            comments.forEach(comment => {
              const commentDiv = document.createElement('div');
              const name = document.createElement('h3');
              const email = document.createElement('p');
              const commentBody = document.createElement('p');

              name.textContent = 'Name: ' + comment.name;
              email.textContent = 'Email: ' + comment.email;
              commentBody.textContent = 'Comment: ' + comment.body;

              commentDiv.appendChild(name);
              commentDiv.appendChild(email);
              commentDiv.appendChild(commentBody);

              postDiv.appendChild(commentDiv);
            });
          })
          .catch(error => console.error('Error:', error));

        postsContainer.appendChild(postDiv);
      });
    })
    .catch(error => console.error('Error:', error));
};