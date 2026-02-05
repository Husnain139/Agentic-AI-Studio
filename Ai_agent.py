#Setup API KEY 

import os 
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

#Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm=ChatOpenAI(model="gpt-4o-mini")
groq_llm=ChatGroq(model="llama-3.3-70b-versatile")

search_tool=TavilySearchResults(max_results=2)

#setup AI agents with Searchtool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt="Act as an AI chatbot who is smart and friendly"

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="OpenAI":
        llm=ChatOpenAI(model=llm_id)

    tools=[TavilySearchResults(max_results=2)] if allow_search else []
    
    # Create the agent using the correct API
    # In LangGraph 1.0.7+, use 'prompt' parameter for system messages
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    
    if system_prompt and system_prompt.strip():
        # Create a prompt template with system message
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ])
        agent = create_react_agent(llm, tools, prompt=prompt_template)
    else:
        # No system prompt
        agent = create_react_agent(llm, tools)
    
    # Format messages properly
    from langchain_core.messages import HumanMessage
    formatted_messages = [HumanMessage(content=msg) for msg in query]
    
    state={"messages": formatted_messages}
    
    try:
        response=agent.invoke(state)
        messages=response.get("messages", [])
        ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
        return ai_messages[-1] if ai_messages else "No response generated"
    except Exception as e:
        return f"Error: {str(e)}"

