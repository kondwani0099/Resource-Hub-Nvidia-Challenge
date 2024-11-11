from flask import Flask, render_template, request, jsonify ,send_from_directory
from werkzeug.utils import secure_filename
import os
# from rag import reload_index, answer_query
# from emotion import analyze_emotion
from emotion import*
from dotenv import load_dotenv
from search import*
from rag import*


load_dotenv()

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Define the folder where your books are stored
BOOK_FOLDER = './uploads'


@app.route('/api/books', methods=['GET'])
def list_books():
    try:
        # List all PDF files in the uploads folder
        books = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if f.endswith('.pdf')]
        return jsonify(books)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/uploads/<path:filename>', methods=['GET'])
def serve_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    print("Attempting to serve:", file_path)  # Debug print
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/get_books', methods=['GET'])
def get_books():
    # List all PDF files in the uploads folder
    files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.pdf')]
    return jsonify(files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith('.pdf'):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return jsonify({"message": "File uploaded successfully"}), 200
    else:
        return jsonify({"error": "Invalid file format. Only PDFs are allowed."}), 400

@app.route('/')
def index():
    return render_template('index-main.html')


@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')

    try:
        # Use the query engine from `document_index`
        query_engine = document_index.as_query_engine(similarity_top_k=20)
        response = query_engine.query(question)

        # Ensure response is serializable (if response has text property, otherwise adjust accordingly)
        result = response.text if hasattr(response, 'text') else str(response)
        return jsonify({'response': result})

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'An error occurred while processing your question.'}), 500

@app.route('/upload_image', methods=['POST'])
def upload_image():
    try:
        data = request.get_json()
        app.logger.info(f"Received data: {data}")
        images = data.get('images')

        if not images or not isinstance(images, list) or len(images) == 0:
            return jsonify({'error': 'No image data provided'}), 400

        detected_emotions = []
        responses = []

        for idx, image_data in enumerate(images):
            if ',' in image_data:
                image_data = image_data.split(',')[1]

            image_bytes = base64.b64decode(image_data)

            # Ensure that the image is correctly decoded
            if not image_bytes:
                return jsonify({'error': f'Image {idx + 1} data is invalid'}), 400

            nparr = np.frombuffer(image_bytes, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # Check if the image is properly decoded
            if img is None or img.size == 0:
                return jsonify({'error': f'Failed to decode image {idx + 1}'}), 400

            try:
                # Detect emotions using DeepFace
                results = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)

                if isinstance(results, list):
                    emotion = results[0]['dominant_emotion']
                else:
                    emotion = results['dominant_emotion']

                detected_emotions.append(emotion)
                app.logger.info(f"Detected emotion for image {idx + 1}: {emotion}")

                # Generate response using Groq
                response = generate_response(emotion)
                responses.append(response)
                app.logger.info(f"Generated response for image {idx + 1}: {response}")

                # Additionally analyze with Gemini model
                gemini_prompt = f"Detect emotions on the face image for further analysis."
                gemini_response = model.generate_content([gemini_prompt, Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))])
                responses.append(gemini_response.text)

            except Exception as e:
                app.logger.error(f"Error during emotion analysis for image {idx + 1}: {str(e)}")
                detected_emotions.append("No face detected")
                responses.append("No face detected in the image.")

        return jsonify({
            'message': 'Images processed successfully',
            'detected_emotions': detected_emotions,
            'responses': responses
        }), 200

    except Exception as e:
        app.logger.error(f"Image processing failed: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500


@app.route('/search', methods=['POST'])
def search():
    # Get data from the POST request
    data = request.get_json()
    user_query = data.get("query")
    
    if not user_query:
        return jsonify({"error": "Query parameter is required"}), 400
    
    google_api_key = ""
    google_cx = ""
    youtube_api_key = ""
    api_key = ""  # Example Groq API Key
    user_query = "Find the links for the users query here ,{user_query}"
    model_id = ""  # Example model ID from Groq

    # Call summarize and search function
    results = summarize_and_search(user_query, model_id, api_key, google_api_key, google_cx, youtube_api_key)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
