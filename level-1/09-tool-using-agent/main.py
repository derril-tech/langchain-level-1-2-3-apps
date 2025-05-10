# ====================================
# LangChain Agent with Tool Example
# Using gpt-4o-2024-08-06 + Tavily Search
# ====================================

# Load environment variables from .env file
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]  # Load OpenAI API Key

# Import LangChain's OpenAI LLM wrapper
from langchain_openai import ChatOpenAI

# Initialize the language model with GPT-4o
llm = ChatOpenAI(model="gpt-4o-2024-08-06")

# ====================================
# Tool: Tavily Web Search
# ====================================

# Import Tavily search tool from LangChain's community tools
from langchain_community.tools.tavily_search import TavilySearchResults

# Create an instance of the search tool with 2 max results
search = TavilySearchResults(max_results=2)

# Directly invoke the search tool (without agent) to demonstrate standalone tool use
response = search.invoke("Who are the top stars of the 2024 Eurocup?")

print("\n----------\n")
print("Who are the top stars of the 2024 Eurocup?")
print("\n----------\n")
print(response)
print("\n----------\n")

# ====================================
# Binding Tools to the Language Model
# ====================================

# Create a list of tools we want to bind to the LLM
tools = [search]

# Bind tools to the LLM (optional step for certain workflows)
llm_with_tools = llm.bind_tools(tools)

# ====================================
# Agent Creation with LangGraph (ReAct)
# ====================================

from langgraph.prebuilt import create_react_agent

# Create a reactive agent that can use tools
agent_executor = create_react_agent(llm, tools)

# ====================================
# Agent Call with Simple Message
# ====================================

from langchain_core.messages import HumanMessage

# Ask a question to the agent, which may use the search tool
response = agent_executor.invoke({
    "messages": [HumanMessage(content="Where is the soccer Eurocup 2024 played?")]
})

print("\n----------\n")
print("Where is the soccer Eurocup 2024 played? (agent)")
print("\n----------\n")
print(response["messages"])
print("\n----------\n")

# ====================================
# Streaming a Response from the Agent
# ====================================

print("When and where will it be the 2024 Eurocup final match? (agent with streaming)")
print("\n----------\n")

for chunk in agent_executor.stream({
    "messages": [HumanMessage(content="When and where will it be the 2024 Eurocup final match?")]
}):
    print(chunk)
    print("----")

print("\n----------\n")

# ====================================
# Using Agent with Memory (Stateful Threads)
# ====================================

from langgraph.checkpoint.memory import MemorySaver

# Enable memory to persist context across multiple messages
memory = MemorySaver()

# Re-create the agent executor with memory enabled
agent_executor = create_react_agent(llm, tools, checkpointer=memory)

# Set a thread ID for storing conversational context
config = {"configurable": {"thread_id": "001"}}

print("Who won the 2024 soccer Eurocup?")
for chunk in agent_executor.stream({
    "messages": [HumanMessage(content="Who won the 2024 soccer Eurocup?")]
}, config):
    print(chunk)
    print("----")

print("Who were the top stars of that winner team?")
for chunk in agent_executor.stream({
    "messages": [HumanMessage(content="Who were the top stars of that winner team?")]
}, config):
    print(chunk)
    print("----")

# Now simulate a new thread where context is not shared
print("(With new thread_id) About what soccer team we were talking?")
config = {"configurable": {"thread_id": "002"}}
for chunk in agent_executor.stream({
    "messages": [HumanMessage(content="About what soccer team we were talking?")]
}, config):
    print(chunk)
    print("----")

# ====================================
# END OF SCRIPT
# ====================================

############################################
# 🧠 LangChain Agent with Tool – Notes
############################################

# ✅ 1. os + dotenv: Used to securely load your OpenAI API key from a .env file.
#    Best practice for managing API secrets.

# ✅ 2. ChatOpenAI: Wrapper around OpenAI's GPT models. We used "gpt-4o-2024-08-06", the latest powerful multimodal model.

# ✅ 3. TavilySearchResults: A LangChain-compatible tool that can search the web. It returns the top 2 results for any query.

# ✅ 4. invoke(): You can call a tool directly without involving the LLM or an agent.

# ✅ 5. tools + bind_tools: Binding tools to LLM is optional unless you're manually wiring things. The agent handles this automatically.

# ✅ 6. create_react_agent(): This creates an LLM-powered agent that uses ReAct (reasoning and acting). It decides when to call tools like Tavily.

# ✅ 7. agent_executor.invoke(): Use this to send a static message to the agent and get a full response.

# ✅ 8. agent_executor.stream(): Sends a prompt to the agent and streams the reply token-by-token or chunk-by-chunk. Great for long answers.

# ✅ 9. MemorySaver: This enables memory (context retention). By using `thread_id`, you can simulate sessions that remember what was said earlier.

# ✅ 10. thread_id: Useful to manage conversations as separate threads. Different `thread_id`s mean different conversations.

# 🛠 This code demonstrates:
# - Tool use outside and inside agent
# - Creating an agent using LangGraph's `create_react_agent`
# - Using memory for multi-turn conversations
# - Streaming responses and managing conversation state

############################################
