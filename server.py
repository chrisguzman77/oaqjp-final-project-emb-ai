"""
Emotion Detector web server.

Provides a Flask endpoint to analyze text for basic emotions
using the Watson NLP service.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    """Handle GET requests for emotion detection."""
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if request.get('dominant_emotion') is None:
        return "Invalid input! Try again."

    return response

@app.route("/")
def render_index_page():
    """Render the home page with the input form."""
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
