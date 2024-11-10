 // Initialize with a system message
 document.addEventListener('DOMContentLoaded', function() {
  const chatContent = document.getElementById('chat-content');
  const initialMessage = document.createElement('div');
  initialMessage.classList.add('bg-gray-200', 'p-2', 'rounded', 'self-start');
  initialMessage.innerText = 'System: Hi there! How can I help you today?';
  chatContent.appendChild(initialMessage);
});

async function askQuestion() {
  const questionInput = document.getElementById("questionInput");
  const question = questionInput.value.trim();
  const chatContent = document.getElementById('chat-content');

  if (!question) {
    const errorMessage = document.createElement('div');
    errorMessage.classList.add('bg-red-200', 'p-2', 'rounded', 'self-start');
    errorMessage.innerText = "Please enter a question before asking.";
    chatContent.appendChild(errorMessage);
    return;
  }

  // Add user question to chat
  const userMessage = document.createElement('div');
  userMessage.classList.add('bg-blue-100', 'p-2', 'rounded', 'self-end');
  userMessage.innerText = `You: ${question}`;
  chatContent.appendChild(userMessage);

  // Scroll to bottom to show the new message
  chatContent.scrollTop = chatContent.scrollHeight;

  try {
    // Send the question to the server and get a response
    const response = await fetch("/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })
    });

    const data = await response.json();

    const botResponse = document.createElement('div');
    botResponse.classList.add('bg-gray-200', 'p-2', 'rounded', 'self-start');
    botResponse.innerText = `Bot: ${data.response || "No response received."}`;
    chatContent.appendChild(botResponse);

    // Scroll to bottom to show the new message
    chatContent.scrollTop = chatContent.scrollHeight;

  } catch (error) {
    const botResponse = document.createElement('div');
    botResponse.classList.add('bg-gray-200', 'p-2', 'rounded', 'self-start');
    botResponse.innerText = "An error occurred while asking the question. Please try again.";
    chatContent.appendChild(botResponse);
    console.error("Error during question handling:", error);
  }

  // Clear the input field
  questionInput.value = '';
}

function toggleChatbot() {
  const chatbot = document.getElementById("chatbot");
  chatbot.style.display = (chatbot.style.display === "none" || chatbot.style.display === "") ? "block" : "none";
}


    // Toggle Menu
    function toggleMenu() {
      var linkItems = document.getElementById("linkItems");
      if (linkItems.classList.contains("hidden")) {
        linkItems.classList.remove("hidden");
      } else {
        linkItems.classList.add("hidden");
      }
    }

    // Toggle Chatbot
    function toggleChatbot() {
      var chatbot = document.getElementById("chatbot");
      if (chatbot.style.display === "none" || chatbot.style.display === "") {
        chatbot.style.display = "block";
      } else {
        chatbot.style.display = "none";
      }
    }

    // Search Books in the Library Section
    function searchBooks() {
      const searchQuery = document.getElementById("searchBox").value.toLowerCase();
      const bookList = document.getElementById("bookList");
      const books = bookList.getElementsByTagName("li");

      for (let i = 0; i < books.length; i++) {
        const book = books[i].textContent.toLowerCase();
        if (book.includes(searchQuery)) {
          books[i].style.display = "";
        } else {
          books[i].style.display = "none";
        }
      }
    }