from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_chat(messages, max_messages=100):
    # Combine most meaningful messages into one string
    texts = [m["message"] for m in messages if len(m["message"].split()) > 4][:max_messages]
    combined_text = " ".join(texts)

    if not combined_text.strip():
        return "Chat too short to summarize."

    # Split if too long for model (max tokens ~1024 for distilbart)
    chunks = [combined_text[i:i+1000] for i in range(0, len(combined_text), 1000)]

    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=120, min_length=40, do_sample=False)[0]['summary_text']
        summaries.append(summary)

    return " ".join(summaries)
