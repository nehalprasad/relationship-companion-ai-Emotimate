import pandas as pd
import plotly.express as px
from sentiment_analyzer import get_sentiment, get_emotion

def plot_emotion_trend(messages):
    data = []
    for m in messages:
        _, score = get_sentiment(m["message"])
        data.append({
            "date": m["timestamp"].date(),
            "score": score
        })

    df = pd.DataFrame(data)
    trend = df.groupby("date")["score"].mean().reset_index()

    fig = px.line(trend, x="date", y="score", title="🧠 Emotional Trend Over Time",
                  labels={"date": "Date", "score": "Average Sentiment Score"},
                  markers=True)
    return fig

def plot_emotion_distribution(messages):
    data = []
    for m in messages:
        emotion, _ = get_emotion(m["message"])
        data.append(emotion)

    df = pd.DataFrame(data, columns=["emotion"])
    count = df["emotion"].value_counts().reset_index()
    count.columns = ["emotion", "count"]

    fig = px.pie(count, values='count', names='emotion', title='🎭 Overall Emotion Distribution')
    return fig
