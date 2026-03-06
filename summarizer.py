from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
import os

os.environ["OPENROUTER_API_KEY"] = "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"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)

def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None

def get_transcript(video_id):
    ytt = YouTubeTranscriptApi()
    try:
        # Try English first
        transcript = ytt.fetch(video_id, languages=['en'])
    except:
        try:
            # Fall back to Hindi
            transcript = ytt.fetch(video_id, languages=['hi'])
        except:
            # Try whatever language is available
            transcript = ytt.fetch(video_id)
    full_text = " ".join([t.text for t in transcript])
    return full_text

def summarize(transcript_text):
    response = client.chat.completions.create(
        model="z-ai/glm-4.5-air:free",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that summarizes YouTube videos clearly and concisely."
            },
            {
                "role": "user",
                "content": f"""Summarize this YouTube transcript. Give me:

1. **TL;DR** (2-3 sentences)
2. **Key Points** (5-7 bullet points)
3. **Main Takeaway** (1 sentence)

Transcript:
{transcript_text[:6000]}"""
            }
        ],
        extra_headers={
            "HTTP-Referer": "http://localhost:8501",
            "X-Title": "YT Summarizer"
        }
    )
    return response.choices[0].message.content