from flask import Flask, jsonify, request, render_template
import requests
from groq import Groq

app = Flask(__name__)

# Function to perform Google Search
def google_search(query, api_key, cx):
    google_url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}"
    response = requests.get(google_url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Google Search API error: {response.status_code}"}

# Function to perform Google Image Search
def google_image_search(query, api_key, cx):
    google_url = f"https://www.googleapis.com/customsearch/v1?q={query}&searchType=image&key={api_key}&cx={cx}"
    response = requests.get(google_url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Google Image Search API error: {response.status_code}"}

# Function to perform YouTube Search
def youtube_search(query, api_key):
    youtube_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={api_key}"
    response = requests.get(youtube_url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"YouTube Search API error: {response.status_code}"}

# Function to summarize and search based on the summary
def summarize_and_search(user_query, model_id, api_key, google_api_key, google_cx, youtube_api_key):
    # Generate prompt for summarization
    prompt = f"Summarize the following query in one sentence, and use it to perform searches on Google, Google Images, and YouTube:\n\nQuery: {user_query}\n"

    # Generate response using Groq
    client = Groq(api_key=api_key)
    completion = client.chat.completions.create(
        model=model_id,
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    # Collect the summarized response
    summary_response = ""
    for chunk in completion:
        summary_response += (chunk.choices[0].delta.content or "")

    # Use the summarized query to perform Google Search, Image Search, and YouTube Search
    google_results = google_search(summary_response, google_api_key, google_cx)
    google_images = google_image_search(summary_response, google_api_key, google_cx)
    youtube_results = youtube_search(summary_response, youtube_api_key)

    return {
        "google_results": google_results,
        "google_images": google_images,
        "youtube_results": youtube_results
    }