document.getElementById('search-btn').addEventListener('click', async () => {
    const query = document.getElementById('search-input').value;
    const response = await fetch(`/search/?title=${query}`);
    const books = await response.json();
    const bookList = document.getElementById('book-list');
    bookList.innerHTML = ''; // Clear previous results

    books.forEach(book => {
        const author = `${book.author_first} ${book.author_last}`;
        const fictionStatus = book.fiction ? "Fiction" : "Non-Fiction";
        const conditionMap = {
            N: "New",
            VG: "Very Good",
            G: "Good",
            U: "Used",
            NR: "Needs Repair",
        };
        const condition = conditionMap[book.condition];
        const readBy = book.assunta_read && book.lucian_read
            ? "Assunta, Lucian"
            : book.assunta_read
            ? "Assunta"
            : book.lucian_read
            ? "Lucian"
            : "No one";

        bookList.innerHTML += `
            <tr>
                <td>${book.title}</td>
                <td>${author}</td>
                <td>${fictionStatus}</td>
                <td>${condition}</td>
                <td>${readBy}</td>
                <td>
                    <button class="btn btn-danger btn-sm delete-btn" data-id="${book.id}">Delete</button>
                </td>
            </tr>`;
    });
});

document.getElementById('add-book-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const title = document.getElementById('title').value;
    const authorFirst = document.getElementById('author-first').value;
    const authorLast = document.getElementById('author-last').value;
    const fiction = document.getElementById('fiction').value === "true";
    const condition = document.getElementById('condition').value;
    const assuntaRead = document.getElementById('assunta-read').checked;
    const lucianRead = document.getElementById('lucian-read').checked;

    const response = await fetch('/books/add/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            title,
            author_first: authorFirst,
            author_last: authorLast,
            fiction,
            condition,
            assunta_read: assuntaRead,
            lucian_read: lucianRead,
        }),
    });

    if (response.ok) {
        alert('Book added successfully!');
        document.getElementById('add-book-modal').click(); // Close modal
        document.getElementById('search-btn').click(); // Refresh the table
    } else {
        alert('Failed to add book.');
    }
});

document.addEventListener('click', async (event) => {
    if (event.target.classList.contains('delete-btn')) {
        const bookId = event.target.dataset.id;
        if (confirm('Are you sure you want to delete this book?')) {
            const response = await fetch(`/books/delete/${bookId}/`, {
                method: 'DELETE',
            });

            if (response.ok) {
                alert('Book deleted successfully!');
                event.target.closest('tr').remove(); // Remove row from table
            } else {
                alert('Failed to delete book.');
            }
        }
    }
});
