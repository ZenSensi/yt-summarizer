# 🎬 YouTube Video Summarizer

An AI-powered web app that summarizes any YouTube video in seconds — built with Python, Streamlit, and DeepSeek AI via OpenRouter.

> Built by a BCA Year 1 student as a first AI project. 100% free to run and deploy.

---

## 🚀 Live Demo

[**Try it live →**](https://YOUR_USERNAME-yt-summarizer.streamlit.app)

---

## ✨ What It Does

Paste any YouTube URL → get an instant AI-generated summary:

- **TL;DR** — 2-3 sentence overview
- **Key Points** — 5-7 bullet points
- **Main Takeaway** — the single most important idea

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web UI |
| youtube-transcript-api | Extracts video transcript |
| OpenAI library | API client (works with OpenRouter) |
| DeepSeek V3 (free) | AI model via OpenRouter |
| Streamlit Cloud | Free deployment |

---

## 📁 Project Structure

```
yt-summarizer/
├── app.py              # Streamlit UI
├── summarizer.py       # Core logic — transcript + AI
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignores .env and venv
└── .env                # Your API key (never pushed to GitHub)
```

---

## ⚙️ Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/ZenSensi/yt-summarizer.git
cd yt-summarizer
```

**2. Create virtual environment**
```bash
python -m venv venv

# Activate:
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac / Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your API key**

Create a `.env` file in the root folder:
```
OPENROUTER_API_KEY=sk-or-your-key-here
```

Get your free key at [openrouter.ai](https://openrouter.ai)

**5. Run the app**
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## ☁️ Deploy on Streamlit Cloud

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set main file to `app.py`
5. Go to **Advanced settings → Secrets** and add:
```toml
OPENROUTER_API_KEY = "sk-or-your-key-here"
```
6. Click Deploy — live in 2 minutes

---

## 📦 Requirements

```
openai>=1.0.0
youtube-transcript-api>=0.6.2
streamlit>=1.32.0
python-dotenv>=1.0.0
```

---

## ⚠️ Known Limitations

- Only works on videos that have captions/subtitles enabled
- Free DeepSeek model may occasionally be rate-limited — retry after 1-2 minutes
- Very long videos get truncated to first 6000 characters of transcript

---

## 🔮 Planned Upgrades

- [ ] Hindi and multilingual video support
- [ ] Copy summary to clipboard button
- [ ] Download summary as PDF
- [ ] Show video thumbnail
- [ ] Save past summaries history
- [ ] Model switcher dropdown

---

## 👤 Author

**Arnabh** — BCA (Data Science & AI) Student  
[@zenslife.exe](https://www.instagram.com/zenslife.exe/) on Instagram  

---

## 📄 License

MIT License — free to use and modify.
