from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.embeddings.nvidia import NVIDIAEmbedding
from llama_index.llms.nvidia import NVIDIA
from llama_index.core.node_parser import SentenceSplitter

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, template_folder='templates')

# Configure file upload folder
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Set NVIDIA API key from environment
nvidia_api_key = os.getenv("NVIDIA_API_KEY")
if not nvidia_api_key:
    raise ValueError("NVIDIA API key is missing. Please set it in the .env file.")

# Initialize settings
Settings.text_splitter = SentenceSplitter(chunk_size=500)
Settings.embed_model = NVIDIAEmbedding(model="NV-Embed-QA", api_key=nvidia_api_key, truncate="END")
Settings.llm = NVIDIA(model="meta/llama3-70b-instruct", api_key=nvidia_api_key)

# Load documents and create an index
def load_documents():
    documents = SimpleDirectoryReader(UPLOAD_FOLDER).load_data()
    index = VectorStoreIndex.from_documents(documents)
    return index

# Load the index globally
document_index = load_documents()