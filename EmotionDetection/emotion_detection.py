import requests
import json

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    myobj = { "raw_document": { "text": text_to_analyse } }

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)

    def invalid_response():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    if response.status_code != 200:
        return invalid_response()

    formatted = json.loads(response.text)
    
    predictions = formatted.get('emotionPredictions', [])
    if not predictions:
        return invalid_response

    emotion_block = predictions[0].get('emotion', {}) if predictions else {}
    
    anger    = float(emotion_block.get('anger',    0.0))
    disgust  = float(emotion_block.get('disgust',  0.0))
    fear     = float(emotion_block.get('fear',     0.0))
    joy      = float(emotion_block.get('joy',      0.0))
    sadness  = float(emotion_block.get('sadness',  0.0))

    scores = {
        'anger':   anger,
        'disgust': disgust,
        'fear':    fear,
        'joy':     joy,
        'sadness': sadness
    }
    dominant = max(scores, key=scores.get)
            
    return {
        'anger':           anger,
        'disgust':         disgust,
        'fear':            fear,
        'joy':             joy,
        'sadness':         sadness,
        'dominant_emotion': dominant
    }
