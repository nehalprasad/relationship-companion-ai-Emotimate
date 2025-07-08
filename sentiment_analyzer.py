from transformers import pipeline

sentiment_pipeline = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False)

def get_sentiment(text):
    if not text.strip():
        return "NEUTRAL", 0.0
    result = sentiment_pipeline(text[:512])[0]
    label = result['label']
    score = round(result['score'], 2)
    numeric = score if label == "POSITIVE" else -score
    return label, numeric

def get_emotion(text):
    if not text.strip():
        return "neutral", 0.0
    result = emotion_pipeline(text[:512])[0]
    return result['label'], round(result['score'], 2)
