import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# এপিআই কী রেন্ডার থেকে আসবে
API_KEY = os.environ.get("GEMINI_API_KEY")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

@app.route('/')
def home():
    return "YouTube Shorts AI Toolkit is Live! 🚀"

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    topic = data.get("topic")
    prompt = f"Viral YouTube Shorts strategist: Write a viral 3-second hook and a catchy title for: {topic}."
    
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(API_URL, json=payload)
        ai_text = response.json()['candidates'][0]['content']['parts'][0]['text']
        return jsonify({"success": True, "data": ai_text})
    except:
        return jsonify({"success": False, "error": "API Issue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
