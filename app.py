import os
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_KEY = os.environ.get("GEMINI_API_KEY")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    topic = data.get("topic")
    prompt = f"Viral YouTube Shorts strategist: Give 3 viral ideas, hooks, and titles for: {topic}."
    
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(API_URL, json=payload)
        ai_text = response.json()['candidates'][0]['content']['parts'][0]['text']
        return jsonify({"success": True, "data": ai_text})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
