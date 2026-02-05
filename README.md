# 🤖 LangGraph AI Agent Project

## 📖 Project Overview

This is a **LangGraph-based AI Chatbot Agent** application with a FastAPI backend and Streamlit frontend. It allows users to interact with multiple AI models (Groq and OpenAI) with optional web search capabilities powered by Tavily.

### Key Features
- ✅ Multiple LLM providers (Groq and OpenAI)
- ✅ Web search integration via Tavily
- ✅ FastAPI REST API backend
- ✅ Interactive Streamlit UI
- ✅ Customizable system prompts
- ✅ Model selection (Llama 3.3, Mixtral, GPT-4o-mini)

---

## 🏗️ Project Structure

```
AI Agent/
├── Ai_agent.py          # Core AI agent logic using LangGraph
├── backend.py           # FastAPI server with /chat endpoint
├── frontend.py          # Streamlit UI for user interaction
├── .env                 # API keys configuration
├── Pipfile              # Dependency management
├── Pipfile.lock         # Locked dependencies
└── README.md            # This file
```

---

## 🔧 Technologies Used

- **LangChain & LangGraph**: AI agent framework
- **FastAPI**: Backend REST API
- **Streamlit**: Frontend UI
- **Uvicorn**: ASGI server
- **Groq API**: Fast LLM inference (Llama, Mixtral)
- **OpenAI API**: GPT models
- **Tavily API**: Web search functionality

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.14+ (or 3.10+)
- pip package manager
- API Keys for:
  - Groq (get from: https://console.groq.com)
  - OpenAI (get from: https://platform.openai.com)
  - Tavily (get from: https://tavily.com)

### Installation Steps

1. **Clone/Navigate to the project directory**
   ```bash
   cd "G:\AI Agent"
   ```

2. **Install dependencies**
   ```bash
   pip install langchain-groq langchain-openai langchain-community langgraph pydantic fastapi uvicorn streamlit requests python-dotenv tavily-python
   ```

3. **Configure API Keys**
   - Edit the `.env` file with your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```

---

## ▶️ Running the Application

### Method 1: Run Both Servers Manually

**Terminal 1 - Start Backend Server:**
```bash
cd "G:\AI Agent"
python backend.py
```
✅ Backend will run on: `http://127.0.0.1:9999`

**Terminal 2 - Start Frontend UI:**
```bash
cd "G:\AI Agent"
streamlit run frontend.py
```
✅ Frontend will open automatically in your browser at: `http://localhost:8501`

---

## 🎯 How to Use

1. **Open the Streamlit UI** in your browser (usually auto-opens at `http://localhost:8501`)

2. **Configure Your Agent:**
   - Enter a custom system prompt (e.g., "Act as a helpful coding assistant")
   - Select Provider: Groq or OpenAI
   - Choose a model:
     - **Groq**: llama-3.3-70b-versatile, mixtral-8x7b-32768
     - **OpenAI**: gpt-4o-mini
   - Toggle "Allow Web Search" if you want the agent to search the web

3. **Ask Questions:**
   - Type your query in the text area
   - Click "Ask Agent!"
   - View the AI response

---

## 🔍 API Endpoints

### POST /chat
**URL:** `http://127.0.0.1:9999/chat`

**Request Body:**
```json
{
  "model_name": "llama-3.3-70b-versatile",
  "model_provider": "Groq",
  "system_prompt": "Act as a helpful assistant",
  "messages": ["What is the capital of France?"],
  "allow_search": false
}
```

**Response:**
```json
"The capital of France is Paris."
```

---

## 🐛 Issues Fixed

1. **Typo in Environment Variable**: Fixed `AVILY_API_KEY` → `TAVILY_API_KEY` in `Ai_agent.py`
2. **Missing dotenv import**: Added `python-dotenv` to load environment variables from `.env` file
3. **Dependency Installation**: Installed all required AI/ML libraries

---

## 📦 Dependencies

```
langchain-groq          # Groq LLM integration
langchain-openai        # OpenAI LLM integration
langchain-community     # Community tools (Tavily search)
langgraph               # Agent framework
pydantic                # Data validation
fastapi                 # Backend API framework
uvicorn                 # ASGI server
streamlit               # Frontend UI
requests                # HTTP client
python-dotenv           # Environment variable management
tavily-python           # Web search API
```

---

## 🎓 Example Use Cases

1. **General Q&A**: Ask any question without web search
2. **Research Assistant**: Enable web search for current information
3. **Code Helper**: Set system prompt to "Act as a coding expert"
4. **Creative Writing**: Use different models for varied responses

---

## 🔒 Security Notes

- ⚠️ **Never commit `.env` file to version control**
- ⚠️ Keep your API keys private
- ⚠️ Rotate keys if accidentally exposed

---

## 📝 Current Status

✅ **Project is fully functional and running!**

- Backend Server: Running on `http://127.0.0.1:9999`
- Frontend UI: Running on `http://localhost:8501`
- All dependencies: Installed
- Code issues: Fixed
- API keys: Configured

---

## 🛠️ Troubleshooting

### Backend won't start
- Check if port 9999 is available
- Verify API keys in `.env` file
- Ensure all dependencies are installed

### Frontend can't connect to backend
- Make sure backend is running first
- Check the API_URL in `frontend.py` matches backend address

### API errors
- Verify your API keys are valid and have credits
- Check internet connection for API calls

---

## 📧 Support

For issues or questions:
1. Check the error messages in the terminal
2. Verify API keys are correct
3. Ensure all dependencies are installed
4. Check Python version compatibility

---

**Enjoy your AI Agent! 🚀**
