import streamlit as st
from summarizer import get_video_id, get_transcript, summarize

st.set_page_config(
    page_title="YT Summarizer",
    page_icon="YS.png",
    layout="centered"
)

st.title("YouTube Video Summarizer")
st.caption("Paste any YouTube link — get a clean AI summary in seconds")

url = st.text_input("YouTube URL", placeholder="https://youtube.com/watch?v=...")

if st.button("Summarize", type="primary"):
    if not url:
        st.warning("Please enter a YouTube URL")
    else:
        with st.spinner("Fetching transcript and summarizing..."):
            try:
                video_id = get_video_id(url)
                transcript_text = get_transcript(video_id)
                summary = summarize(transcript_text)

                st.success("Done!")
                st.markdown("---")
                st.markdown(summary)

                words = len(transcript_text.split())
                st.caption(f"Summarized {words:,} words instantly")

            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")
                st.info("Make sure the video has captions / subtitles enabled")