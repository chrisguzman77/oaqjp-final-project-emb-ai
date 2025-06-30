from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger   = response['anger']
    disgust = response['disgust']
    fear    = response['fear']
    joy     = response['joy']
    sadness = response['sadness']
    dominant= response['dominant_emotion']

    if dominant is None:
        return "Invalid input! Try again."
    else:
        return response

@app.route("/")
def render_index_page():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)