
#Step1: Setup UI with streamlit (model provider, model, system prompt, web_search, query)
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Agent Studio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern, attractive UI
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main background with gradient */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    
    /* Header styling */
    h1 {
        background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        font-size: 3.5rem !important;
        text-align: center;
        margin-bottom: 0.5rem;
        animation: fadeInDown 0.8s ease-out;
    }
    
    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #a8b2d1;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        animation: fadeIn 1s ease-out;
    }
    
    /* Card-like containers */
    .stTextArea, .stSelectbox, .stRadio, .stCheckbox {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .stTextArea:hover, .stSelectbox:hover {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(168, 237, 234, 0.3);
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(168, 237, 234, 0.15);
    }
    
    /* Text inputs and textareas */
    textarea, input {
        background: rgba(255, 255, 255, 0.08) !important;
        color: #e6f1ff !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
    }
    
    textarea:focus, input:focus {
        border: 1px solid #a8edea !important;
        box-shadow: 0 0 20px rgba(168, 237, 234, 0.3) !important;
    }
    
    /* Labels */
    label {
        color: #a8edea !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.8rem 3rem;
        font-size: 1.2rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        width: 100%;
        margin-top: 1rem;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    /* Response container */
    .response-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 2rem;
        border: 1px solid rgba(168, 237, 234, 0.2);
        margin-top: 2rem;
        animation: slideInUp 0.5s ease-out;
    }
    
    /* Success/Error messages */
    .stSuccess, .stError, .stWarning {
        border-radius: 10px;
        padding: 1rem;
        animation: fadeIn 0.5s ease-out;
    }
    
    /* Checkbox and Radio */
    .stCheckbox, .stRadio {
        color: #e6f1ff;
    }
    
    /* Selectbox */
    div[data-baseweb="select"] > div {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
        border-right: 1px solid rgba(168, 237, 234, 0.1);
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border-left: 4px solid #667eea;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        color: #a8b2d1;
    }
    
    /* Markdown text in response */
    .stMarkdown {
        color: #e6f1ff;
        line-height: 1.8;
    }
    
    /* Subheader */
    h2, h3 {
        color: #a8edea !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 🤖 AI Agent Studio")
st.markdown('<p class="subtitle">✨ Create and Interact with Intelligent AI Agents ✨</p>', unsafe_allow_html=True)

# Create two columns for better layout
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 🎯 Agent Configuration")
    
    # System prompt
    system_prompt = st.text_area(
        "🧠 Define Your AI Agent",
        height=120,
        placeholder="e.g., Act as a helpful assistant who provides detailed and accurate information...",
        help="Customize how your AI agent behaves and responds"
    )
    
    # Provider selection
    provider = st.radio(
        "⚡ Select AI Provider",
        ("Groq", "OpenAI"),
        horizontal=True,
        help="Choose between Groq (fast) or OpenAI (powerful)"
    )
    
    # Model selection
    MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
    MODEL_NAMES_OPENAI = ["gpt-4o-mini"]
    
    if provider == "Groq":
        selected_model = st.selectbox(
            "🔮 Select Model",
            MODEL_NAMES_GROQ,
            help="Choose the AI model to power your agent"
        )
    elif provider == "OpenAI":
        selected_model = st.selectbox(
            "🔮 Select Model",
            MODEL_NAMES_OPENAI,
            help="Choose the AI model to power your agent"
        )
    
    # Web search toggle
    allow_web_search = st.checkbox(
        "🌐 Enable Web Search",
        help="Allow the agent to search the web for up-to-date information"
    )

with col2:
    st.markdown("### 💬 Your Query")
    
    # User query
    user_query = st.text_area(
        "📝 Ask Anything",
        height=280,
        placeholder="Type your question here...\n\nExamples:\n• Explain quantum computing\n• What's the weather like today?\n• Write a Python function to sort a list",
        help="Enter your question or request for the AI agent"
    )

# Ask button (full width)
API_URL = "http://127.0.0.1:9999/chat"

if st.button("🚀 Ask Agent"):
    if user_query.strip():
        # Show loading spinner
        with st.spinner("🤔 Agent is thinking..."):
            import requests
            
            payload = {
                "model_name": selected_model,
                "model_provider": provider,
                "system_prompt": system_prompt,
                "messages": [user_query],
                "allow_search": allow_web_search
            }
            
            try:
                response = requests.post(API_URL, json=payload, timeout=60)
                if response.status_code == 200:
                    response_data = response.json()
                    
                    # Check if response_data is a dictionary
                    if isinstance(response_data, dict):
                        if "error" in response_data:
                            st.error(f"❌ {response_data['error']}")
                        elif "response" in response_data:
                            st.markdown("---")
                            st.markdown("### 🎯 Agent Response")
                            st.markdown(f'<div class="response-container">{response_data["response"]}</div>', unsafe_allow_html=True)
                            st.success("✅ Response generated successfully!")
                        else:
                            st.error("❌ Unexpected response format from backend")
                    else:
                        # Backend returned a string directly
                        st.markdown("---")
                        st.markdown("### 🎯 Agent Response")
                        st.markdown(f'<div class="response-container">{response_data}</div>', unsafe_allow_html=True)
                        st.success("✅ Response generated successfully!")
                else:
                    st.error(f"❌ Backend error: {response.status_code}")
                    with st.expander("View error details"):
                        st.code(response.text)
            except requests.exceptions.ConnectionError:
                st.error("❌ Cannot connect to backend!")
                st.markdown('<div class="info-box">💡 Make sure the backend server is running on http://127.0.0.1:9999<br>Run: <code>python backend.py</code></div>', unsafe_allow_html=True)
            except requests.exceptions.Timeout:
                st.error("⏱️ Request timed out. The agent took too long to respond.")
            except requests.exceptions.JSONDecodeError:
                st.error("❌ Invalid response from backend")
                st.info("Check backend logs for more information")
            except Exception as e:
                st.error(f"❌ Unexpected error: {str(e)}")
                with st.expander("View full traceback"):
                    import traceback
                    st.code(traceback.format_exc())
    else:
        st.warning("⚠️ Please enter a query before asking the agent!")

# Footer
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: #64748b; font-size: 0.9rem;">Built with ❤️ using Streamlit & LangGraph</p>',
    unsafe_allow_html=True
)
