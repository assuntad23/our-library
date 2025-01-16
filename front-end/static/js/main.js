async function fetchBooks(query = "") {
  try {
    const response = await fetch(`/search/?title=${query}`);
    if (!response.ok) {
      throw new Error("Failed to fetch books.");
    }
    return await response.json();
  } catch (error) {
    console.error(error);
    alert("An error occurred while fetching books.");
  }
}

function updateBookTable(books) {
  const bookList = document.getElementById("book-list");
  bookList.innerHTML = "";
  const conditionMap = {
    N: "New",
    VG: "Very Good",
    G: "Good",
    U: "Used",
    NR: "Needs Repair",
  };
  books.forEach((book) => {
    const author = `${book.author_first} ${book.author_last}`;
    const fictionStatus = book.fiction ? "Fiction" : "Non-Fiction";

    const readBy =
      book.assunta_read && book.lucian_read
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
                <td>${conditionMap[book.condition]}</td>
                <td>${readBy}</td>
                ${
                  isAuthenticated
                    ? `
                <td>
                  <button class="btn btn-danger btn-sm delete-btn" data-id="${book.id}">Delete</button>
                </td>
                `
                    : ""
                }
            </tr>`;
  });
}

document.getElementById("search-btn").addEventListener("click", async () => {
  const query = document.getElementById("search-input").value;
  const books = await fetchBooks(query);
  if (books) updateBookTable(books);
});

document
  .getElementById("add-book-form")
  .addEventListener("submit", async (event) => {
    event.preventDefault();

    const title = document.getElementById("title").value;
    const authorFirst = document.getElementById("author-first").value;
    const authorLast = document.getElementById("author-last").value;
    const fiction = document.getElementById("fiction").value === "true";
    const condition = document.getElementById("condition").value;
    const assuntaRead = document.getElementById("assunta-read").checked;
    const lucianRead = document.getElementById("lucian-read").checked;
    const csrftoken = getCookie("csrftoken");

    const response = await fetch("/books/add/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
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
      alert("Book added successfully!");
      document.getElementById("add-book-modal").click();
      document.getElementById("search-btn").click();
    } else {
      alert("Failed to add book.");
    }
  });

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

document.addEventListener("click", async (event) => {
  const csrftoken = getCookie("csrftoken");
  if (event.target.classList.contains("delete-btn")) {
    const bookId = event.target.dataset.id;
    if (confirm("Are you sure you want to delete this book?")) {
      const response = await fetch(`/books/${bookId}`, {
        method: "DELETE",
        headers: {
          "X-CSRFToken": csrftoken,
          "Content-Type": "application/json",
        },
      });

      if (response.ok) {
        alert("Book deleted successfully!");
        event.target.closest("tr").remove();
      } else {
        alert("Failed to delete book.");
      }
    }
  }
});
