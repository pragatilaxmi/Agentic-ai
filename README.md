# NewsForge 📰🤖

**NewsForge** is an AI-powered multi-agent news authoring system that researches, fact-checks, writes, and publishes news articles automatically.

## 🌟 Features

- **Multi-Agent Pipeline**: Specialized agents for research, fact-checking, writing, social media, and publishing
- **Fact-Checking**: Automated verification using vector store retrieval and AI analysis
- **Multiple AI Backends**: Primary Gemini API with Hugging Face fallback
- **Web Research**: Tavily API integration with RSS feed fallback
- **Social Media Generation**: Automatic post and hashtag creation
- **Translation Support**: Multi-language article translation (optional)
- **REST API**: FastAPI backend with comprehensive endpoints
- **Web UI**: Simple, responsive frontend with mock mode for development

## 🏗️ Architecture

```
User Request
    ↓
Frontend (HTML/JS)
    ↓
FastAPI Backend
    ↓
┌─────────────────────────────────────────┐
│  Multi-Agent Pipeline                   │
│                                         │
│  1. Research Agent                      │
│     ├─ Tavily API Search                │
│     └─ RSS Feed Fallback                │
│                                         │
│  2. Claim Extraction (Gemini)           │
│                                         │
│  3. Fact-Check Agent                    │
│     ├─ ChromaDB Vector Retrieval        │
│     └─ AI Verification                  │
│                                         │
│  4. Writing Agent                       │
│     └─ Evidence-based article generation│
│                                         │
│  5. Social Agent                        │
│     └─ Posts & hashtag generation       │
│                                         │
│  6. Publish Agent                       │
│     └─ Markdown file export             │
│                                         │
│  7. Translation Agent (optional)        │
└─────────────────────────────────────────┘
    ↓
Article Output
```

## 📋 Prerequisites

- Python 3.9 or higher
- API Keys:
  - Google Gemini API (required)
  - Tavily API (optional, for web search)
  - Hugging Face API (optional, for fallback)
  - LangSmith API (optional, for monitoring)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd agent
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your API keys
# At minimum, you need GEMINI_API_KEY
```

Example `.env` configuration:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
GEMINI_COMPLETION_ENDPOINT=https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro:generateContent
TAVILY_API_KEY=your_tavily_key_here  # optional
CHROMA_DIR=./chromadb_store
MAX_RETRIEVE=5
CONFIDENCE_THRESHOLD=0.8
```

### 5. Run the Application

#### Start the Backend API

```bash
# From the project root
cd src
uvicorn api.app:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at: `http://127.0.0.1:8000`

#### Open the Frontend

Simply open `frontend/index.html` in your web browser, or serve it with a simple HTTP server:

```bash
# Python 3
cd frontend
python -m http.server 3000

# Then open http://localhost:3000 in your browser
```

### 6. Test the System

Visit the web UI and:
1. Enter a topic (e.g., "Latest developments in AI")
2. Configure word count and style
3. Click "Generate"
4. Watch the multi-agent pipeline work!

## 📁 Project Structure

```
agent/
├── src/
│   ├── agents/                    # Specialized agent modules
│   │   ├── research_agent.py      # Web research & RSS
│   │   ├── factcheck_agent.py     # Fact verification
│   │   ├── writing_agent.py       # Article generation
│   │   ├── social_agent.py        # Social media content
│   │   ├── publish_agent.py       # File export
│   │   └── indexer.py             # Document indexing
│   │
│   ├── api/
│   │   └── app.py                 # FastAPI application
│   │
│   ├── orchestrator/
│   │   └── langgraph_orchestrator.py  # Workflow orchestration
│   │
│   ├── utils/
│   │   ├── gemini_client.py       # Gemini API wrapper
│   │   ├── tavily_client.py       # Tavily search wrapper
│   │   └── hf_client.py           # Hugging Face wrapper
│   │
│   ├── vectorstore/
│   │   └── chroma_store.py        # ChromaDB integration
│   │
│   ├── config.py                  # Configuration management
│   └── main.py                    # CLI entry point
│
├── frontend/
│   ├── index.html                 # Web UI
│   └── app.js                     # Frontend logic
│
├── .env.example                   # Environment template
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `GEMINI_API_KEY` | Yes | - | Google Gemini API key |
| `GEMINI_COMPLETION_ENDPOINT` | Yes | - | Gemini API endpoint |
| `TAVILY_API_KEY` | No | - | Tavily search API key |
| `HUGGINGFACE_API_KEY` | No | - | Hugging Face API key |
| `CHROMA_DIR` | No | `./chromadb_store` | ChromaDB storage path |
| `MAX_RETRIEVE` | No | `5` | Max documents to retrieve |
| `CONFIDENCE_THRESHOLD` | No | `0.8` | Fact-check confidence threshold |
| `ALLOWED_ORIGINS` | No | `localhost:*` | CORS allowed origins |
| `DEBUG` | No | `false` | Enable debug logging |

## 🧪 Testing

### Run Import Diagnostics

```bash
python diagnose_imports.py
```

### Test Individual Components

```bash
# Test Gemini client
python test_import.py

# Test API routes
python check_routes.py
```

### Run Unit Tests (requires pytest)

```bash
pytest tests/
```

## 📡 API Endpoints

### Health Check
```http
GET /health
```
Returns API health status

### Ping
```http
GET /ping
```
Simple connectivity test

### Generate Article
```http
POST /api/generate
Content-Type: application/json

{
  "topic": "Latest AI developments",
  "specs": {
    "word_count": 400,
    "style": "objective",
    "translate_to": null
  }
}
```

**Response:**
```json
{
  "status": "ok",
  "article": "...",
  "provenance": [...],
  "social": {
    "posts": [...],
    "hashtags": [...]
  },
  "publish": {
    "path": "/published/article.md"
  }
}
```

## 🐛 Troubleshooting

### ChromaDB Issues

If you see ChromaDB deprecation warnings:
```bash
# The system will automatically fallback to in-memory storage
# For persistence, ensure CHROMA_DIR is set correctly
```

### Import Errors

```bash
# Ensure you're in the virtual environment
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### API Key Issues

```bash
# Verify your .env file exists and has correct keys
cat .env  # Linux/Mac
type .env  # Windows

# Test API key
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('GEMINI_API_KEY:', bool(os.getenv('GEMINI_API_KEY')))"
```

### CORS Errors

If the frontend can't connect to the backend:
1. Ensure backend is running on `http://127.0.0.1:8000`
2. Check `ALLOWED_ORIGINS` in `.env`
3. Open browser console for detailed error messages

## 🔒 Security Notes

⚠️ **Important**: Never commit your `.env` file to version control!

- API keys are stored in `.env` (git-ignored)
- Use `.env.example` as a template
- Rotate any exposed API keys immediately
- Restrict CORS origins in production
- Consider adding API authentication for production use

## 🚀 Production Deployment

### Recommended Improvements

1. **Add Authentication**: Implement JWT or API key authentication
2. **Rate Limiting**: Add rate limiting middleware
3. **Caching**: Implement Redis caching for research results
4. **Monitoring**: Add observability (OpenTelemetry, Sentry)
5. **Database**: Use persistent database for article storage
6. **Queue System**: Use Celery/RQ for long-running tasks
7. **Containerization**: Use Docker for deployment

### Docker Deployment

This starts the FastAPI backend and a static server for the frontend (Nginx):

```bash
# From project root
docker-compose up -d

# Backend API -> http://127.0.0.1:8000
# Frontend UI  -> http://127.0.0.1:3000
```

The compose file mounts your working directory into the api container, installs requirements, and runs uvicorn. Environment variables are read from .env.

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📝 License

[Specify your license here]

## 🙏 Acknowledgments

- Google Gemini API for AI generation
- Tavily for web search
- LangChain & LangGraph for orchestration
- ChromaDB for vector storage
- FastAPI for the backend framework

## 📞 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Check existing documentation
- Review the troubleshooting section

---

**Built with ❤️ using AI agents**
