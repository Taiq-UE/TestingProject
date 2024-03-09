// Importujemy funkcję fetchPosts
const fetchPosts = require('./app');

// Tworzymy sztuczną implementację funkcji fetch, aby symulować zapytania do API
global.fetch = jest.fn(() =>
    Promise.resolve({
        json: () => Promise.resolve([{ id: 1, userId: 1, title: 'Test Post', body: 'This is a test post.' }])
    })
);

// Importujemy funkcję renderPosts, jeśli jest ona wykorzystywana w kodzie (niewidoczna w fragmencie kodu, który dostarczyłeś)
// const renderPosts = require('./ścieżka/do/renderPosts');

describe('fetchPosts function', () => {
    it('should fetch posts from the API with default minCharCount and maxCharCount', async () => {
        // Wywołujemy funkcję fetchPosts
        await fetchPosts();

        // Sprawdzamy, czy funkcja fetch została wywołana z odpowiednim adresem URL
        expect(fetch).toHaveBeenCalledWith('http://127.0.0.1:8080/posts/100');

        // Możemy również dodać inne asercje, aby sprawdzić inne aspekty funkcji fetchPosts
    });

    it('should fetch posts from the API with specified minCharCount and maxCharCount', async () => {
        // Wywołujemy funkcję fetchPosts z określonymi parametrami
        const minCharCount = 10;
        const maxCharCount = 100;
        await fetchPosts(minCharCount, maxCharCount);

        // Sprawdzamy, czy funkcja fetch została wywołana z odpowiednimi parametrami URL
        expect(fetch).toHaveBeenCalledWith(`http://127.0.0.1:8080/posts/100`);

        // Możemy również dodać inne asercje, aby sprawdzić inne aspekty funkcji fetchPosts
    });
});
