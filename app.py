import streamlit as st
from sentiment_analyzer import get_sentiment, get_emotion
from chat_parser import parse_chat
from visualizer import plot_emotion_trend, plot_emotion_distribution
from chat_summarizer import summarize_chat

st.set_page_config(page_title="Relationship Companion AI", layout="centered")
st.title("💬 Relationship Companion AI Neews")

uploaded_file = st.file_uploader("Upload your WhatsApp chat file (.txt)", type="txt")

if uploaded_file:
    with open("data/temp_chat.txt", "wb") as f:
        f.write(uploaded_file.read())

    messages = parse_chat("data/temp_chat.txt")

    st.success(f"✅ Successfully parsed {len(messages)} messages!")

    st.subheader("📄 Chat Preview")
    for m in messages[:5]:  # Show first 5
        st.markdown(f"🕓 {m['timestamp']} - **{m['sender']}**: {m['message']}")

    st.subheader("🧠 Chat with Sentiment & Emotion")
    for m in messages[:10]:  # Show first 10 with analysis
        label, score = get_sentiment(m["message"])
        emotion, e_score = get_emotion(m["message"])
        st.markdown(f"🕓 {m['timestamp']} - **{m['sender']}**: {m['message']}")
        st.markdown(f"👉 Sentiment: **{label}** ({score})")
        st.markdown(f"🎭 Emotion: **{emotion}** ({e_score})")
        st.markdown("---")

    st.subheader("📈 Emotional Trend Over Time")
    fig_trend = plot_emotion_trend(messages)
    st.plotly_chart(fig_trend, use_container_width=True)

    st.subheader("📊 Overall Emotion Distribution")
    fig_pie = plot_emotion_distribution(messages)
    st.plotly_chart(fig_pie, use_container_width=True)

st.subheader("🧾 Relationship Summary")

if st.button("📄 Generate Summary"):
    with st.spinner("Analyzing full conversation..."):
        summary = summarize_chat(messages)
        st.markdown(f"📝 **Summary:**\n\n{summary}")
else:
    st.info("📂 Please upload a WhatsApp chat .txt file to begin.")
