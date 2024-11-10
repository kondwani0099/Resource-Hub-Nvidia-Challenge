# Resource Hub 

Welcome to the **Resource Hub**, an all-in-one platform designed to enhance your learning and document management experience. The platform combines AI-powered tools, emotion-aware interactions, document processing features, and web scraping capabilities that make learning smarter and more engaging.

## Features

### Emotion Awareness 🤖💬
- **Encouragement & Support**: The AI tutor detects users' emotions and offers encouragement when feeling down or disengaged.
- **Quiz Creation**: When users feel excited or engaged, the system dynamically creates quizzes to challenge and enhance their learning experience.

### Document Upload & Management 📄
- **Upload Various Document Types**: Users can upload and manage a wide range of files, including:
  - **Images** (JPG, PNG)
  - **PDFs**
  - **Text Files** (TXT)
  - **Word Documents** (DOC/DOCX)
- **Tagging System**: Automatically tags and categorizes all uploaded files for easy retrieval and organization.

### Thesis Creation & Processing 📚
- **Generate Thesis**: Upload large documents to automatically generate a structured thesis from your content.
- **Plagiarism Report**: The system scans for plagiarism and provides a report. It also offers to rewrite sections as needed.
- **Export Options**: Download documents in multiple formats:
  - PDF
  - DOC/DOCX
  - TXT

### Library Search & History 🔍
- **Advanced Search**: Quickly find relevant documents in your personal library using keywords and filters.
- **History**: Keeps track of your uploaded files and interactions for future reference.

### Multimedia Highlights 🌟
- **Top Media Content**: Highlights top images, URLs, and videos related to each document you upload.

### Web Scraping for Resources 🌐
- **Automated Resource Collection**: Use web scraping to gather articles, images, videos, and other resources from the web, which are automatically added to your library.
- **Search External Content**: Find relevant external resources (articles, PDFs, and videos) on a given topic and integrate them into your personal library.

### Credit System 💳
- **Credits**: Start with 100 free credits, which are used for advanced features like thesis generation and plagiarism reports.
- **Payment**: Easily purchase more credits when needed.

### Interactive Chatbot 🤖
- **AI Tutor & Assistant**: Ask questions, get answers, and receive personalized feedback on your learning progress.

## Tech Stack 🛠️
- **Frontend**: 
  - HTML, CSS, JavaScript
  - Tailwind CSS for responsive and modern UI design
- **Backend**: 
  - Flask (Python)
  - Nvidia APIs for emotion detection
  - Hugging Face for AI and NLP models
- **Database**: 
  - MongoDB for storing documents, user data, and interactions
- **Web Scraping Tools**:
  - BeautifulSoup and Scrapy for scraping web content
- **Tools**:
  - Figma for UI/UX design
  - Google Colab for AI model training and experimentation
  - Visual Studio Code (VS Code) for development

## Folder Structure 📂
```
/resource_hub
│
├── app.py                 # Main application file
├── utils/                 # Utility functions
│   ├── file_handling.py   # Functions to handle file uploads and processing
│   ├── search.py          # Search logic for library and history
│   ├── chatbot.py         # Chatbot and AI-related logic
│   └── webscraper.py      # Web scraping logic for gathering external resources
├── thesisai/              # AI models and logic for thesis generation
│   └── thesis_generator.py
├── documentprocess/       # Document processing (tagging, analysis, plagiarism checks)
│   └── process_document.py
├── static/                # CSS, images, and other static files
├── templates/             # HTML files for Flask app
├── database/              # Database connection and management
│   └── db_connection.py   # MongoDB connection handling
└── README.md              # This file
```

## License 📝
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

Enjoy smarter learning and resource management with Resource Hub! 🎓🌟
