let books = []; // Initialize an empty array for the book list

  // Function to fetch books from the server
  async function fetchBooks() {
    try {
      const response = await fetch('/api/books');
      books = await response.json();
      displayBooks(books);
    } catch (error) {
      console.error("Error fetching books:", error);
    }
  }

  // Function to search books
  function searchBooks() {
    const searchValue = document.getElementById('searchBox').value.toLowerCase();
    const filteredBooks = books.filter(book => book.toLowerCase().includes(searchValue));
    displayBooks(filteredBooks);
  }

  // Function to display books
//   function displayBooks(bookArray) {
//     const bookList = document.getElementById('bookList');
//     bookList.innerHTML = '';
//     bookArray.forEach(book => {
//       const li = document.createElement('li');
//       li.className = 'bg-gray-200 p-2';

//       // Create link for each book
//       const link = document.createElement('a');
//       link.href = `/uploads/${book}`;
//       link.textContent = book;
//       link.target = '_blank';

//       li.appendChild(link);
//       bookList.appendChild(li);
//     });
//   }
 // Function to fetch books from the server
 async function fetchBooks() {
    try {
      const response = await fetch('/api/books');
      books = await response.json();
      displayBooks(books);
    } catch (error) {
      console.error("Error fetching books:", error);
    }
  }

//   // Function to search books
//   function searchBooks() {
//     const searchValue = document.getElementById('searchBox').value.toLowerCase();
//     const filteredBooks = books.filter(book => book.toLowerCase().includes(searchValue));
//     displayBooks(filteredBooks);
//   }

  // Function to display books
  function displayBooks(bookArray) {
    const bookList = document.getElementById('bookList');
    bookList.innerHTML = '';
    bookArray.forEach(book => {
      const li = document.createElement('li');
      li.className = 'bg-gray-200 p-2';

      // Create link for each book with click event to load PDF in viewer
      const link = document.createElement('a');
      link.href = '#';
      link.textContent = book;
      link.onclick = function () {
        loadPdf(`/uploads/${book}`);
        return false; // Prevent default link behavior
      };

      li.appendChild(link);
      bookList.appendChild(li);
    });
  }

  // Function to load PDF in the embedded viewer
  function loadPdf(pdfUrl) {
    const pdfViewer = document.getElementById('pdfViewer');
    pdfViewer.src = pdfUrl; // Set the src attribute to the selected PDF's URL
  }


//uploading the nbooks part 
async function uploadFile() {
    const fileInput = document.getElementById('fileUpload');
    const file = fileInput.files[0];

    if (!file) {
      alert("Please select a file to upload.");
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('/upload', {
        method: 'POST',
        body: formData
      });
      if (response.ok) {
        alert("File uploaded successfully!");
        fileInput.value = ''; // Clear the file input
        fetchBooks(); // Refresh the list of uploaded files
      } else {
        alert("Failed to upload file.");
      }
    } catch (error) {
      console.error("Error uploading file:", error);
    }
  }

  // Fetch and display books on page load
// window.onload = fetchBooks;

// async function fetchBooks() {
//   try {
//     const response = await fetch('/api/books');
//     books = await response.json();
//     displayBooks(books);
//   } catch (error) {
//     console.error("Error fetching books:", error);
//   }
// }
  // Fetch and display books on page load
//   window.onload = fetchBooks;
  // Fetch and display books on page load
  window.onload = fetchBooks;