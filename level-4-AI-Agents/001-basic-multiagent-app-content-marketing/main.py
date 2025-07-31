"""
=======================================================
🧠 BEGINNER’S NOTES — LangGraph Multi-Agent App in Python
=======================================================

📌 What This App Does:
This script creates a team of AI agents that work together like a real content marketing team:
- The **Online Researcher** finds content online.
- The **Blog Manager** turns it into a blog post.
- The **Social Media Manager** crafts a tweet about it.
- A **Content Marketing Manager** (router) decides who acts next.

🚀 Key Technologies:
- LangGraph: Builds the "flow" between agents.
- LangChain: Powers the AI agent logic.
- OpenAI (GPT-4o): Used for intelligent decisions and content creation.
- PowerShell + VS Code: Environment setup for running and testing.

✅ Result:
You get a complete cycle where research becomes a blog, then a tweet—no human needed!

"""

# ========================
# 📦 1. Load API Environment Variables
# ========================

# Python's built-in 'os' module is used to interact with the environment
import os
from dotenv import load_dotenv, find_dotenv

# Automatically finds and loads variables (like OPENAI_API_KEY) from your .env file
_ = load_dotenv(find_dotenv())
openai_api_key = os.getenv("OPENAI_API_KEY")  # Used later to authenticate OpenAI access

# ========================
# 🧠 2. Core Imports (LangChain + LangGraph)
# ========================

# Loads the OpenAI-powered LLM (Large Language Model)
from langchain_openai import ChatOpenAI

# Message objects used throughout LangChain and LangGraph
from langchain_core.messages import HumanMessage, BaseMessage

# Parser for interpreting function outputs in JSON format
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser

# Lets us define custom prompts with placeholders for message history
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Used to build and run the actual graph of agents
from langgraph.graph import StateGraph, END

# Used to create LLM agents and wrap them with tools
from langchain.agents import AgentExecutor, create_openai_tools_agent

# Lets us define and register our own tools
from langchain.tools import tool

# Importing a built-in web search tool (Tavily)
from langchain_community.tools.tavily_search import TavilySearchResults

# ========================
# 🔧 3. Utilities (Web scraping, types, warnings)
# ========================

import requests  # For HTTP requests to websites
from bs4 import BeautifulSoup  # For scraping visible content from HTML

import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)  # Clean output from annoying HTML warnings

# Python typing system for structured state in LangGraph
from typing import TypedDict, Annotated, Sequence
import functools  # For partially applying functions (used for agent nodes)
import operator  # Used for additive state merging (e.g., adding messages together)

# ========================
# 🔨 4. Define Custom Tool: Web Scraper
# ========================

@tool("process_search_tool", return_direct=False)
def process_search_tool(url: str) -> str:
    """
    Scrapes readable text from a given URL using BeautifulSoup.
    This helps agents get info from websites.
    """
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.get_text()

# Group of tools available to all agents (search + web scraping)
tools = [TavilySearchResults(max_results=1), process_search_tool]

# ========================
# 🧠 5. Agent Creator (Factory Function)
# ========================

def create_new_agent(llm: ChatOpenAI, tools: list, system_prompt: str) -> AgentExecutor:
    """
    Factory function that builds a LangChain agent with tools and a system prompt.
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="messages"),  # Stores conversation history
        MessagesPlaceholder(variable_name="agent_scratchpad")  # Stores reasoning steps
    ])
    agent = create_openai_tools_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools)

# ========================
# 🧱 6. Agent Node Wrapper
# ========================

def agent_node(state, agent, name):
    """
    Runs an agent and returns a new message wrapped in proper format for LangGraph state.
    """
    result = agent.invoke(state)  # Send input through the agent
    return {"messages": [HumanMessage(content=result["output"], name=name)]}  # Return message to graph state

# ========================
# 🧠 7. Define Agents and Roles
# ========================

# Set up the LLM used by all agents (GPT-4o)
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Our team members (in order)
content_marketing_team = ["online_researcher", "blog_manager", "social_media_manager"]

# Manager prompt for deciding who works next
system_prompt_manager = (
    "As a content marketing manager, your role is to oversee these agents: {content_marketing_team}. "
    "Based on the user's request, determine the next best action. Respond with only one of: {options}. "
    "When all tasks are complete, respond with 'FINISH'."
)

# Options the manager can choose from
options = ["FINISH"] + content_marketing_team

# Function schema for choosing the next role
function_def = {
    "name": "route",
    "description": "Select the next role.",
    "parameters": {
        "title": "routeSchema",
        "type": "object",
        "properties": {"next": {"title": "Next", "anyOf": [{"enum": options}]}},
        "required": ["next"]
    }
}

# The actual routing chain (prompt → LLM → function → JSON parser)
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt_manager),
    MessagesPlaceholder(variable_name="messages"),
    ("system", "Who should act next? Choose from: {options}")
]).partial(options=str(options), content_marketing_team=", ".join(content_marketing_team))

content_marketing_manager_chain = (
    prompt
    | llm.bind_functions(functions=[function_def], function_call="route")
    | JsonOutputFunctionsParser()
)

# Create each specialized agent using the factory function
online_researcher_agent = create_new_agent(
    llm, tools, "You are an online researcher tasked with gathering current info on any topic."
)

blog_manager_agent = create_new_agent(
    llm, tools, "You are a blog manager responsible for creating high-quality SEO blog articles."
)

social_media_manager_agent = create_new_agent(
    llm, tools, "You are a social media manager crafting impactful tweets from blog content."
)

# Wrap each agent into a callable node for the graph
online_researcher_node = functools.partial(agent_node, agent=online_researcher_agent, name="online_researcher")
blog_manager_node = functools.partial(agent_node, agent=blog_manager_agent, name="blog_manager")
social_media_manager_node = functools.partial(agent_node, agent=social_media_manager_agent, name="social_media_manager")

# ========================
# 💾 8. Define Shared State Between Agents
# ========================

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]  # List of all messages (chat memory)
    next: str  # Keeps track of who goes next (from the manager decision)

# ========================
# 🛠️ 9. Build the LangGraph Workflow
# ========================

# Initialize the state machine (workflow)
workflow = StateGraph(AgentState)

# Add nodes (each agent or controller)
workflow.add_node("content_marketing_manager", content_marketing_manager_chain)
workflow.add_node("online_researcher", online_researcher_node)
workflow.add_node("blog_manager", blog_manager_node)
workflow.add_node("social_media_manager", social_media_manager_node)

# Define normal transitions (agent → manager)
for agent in content_marketing_team:
    workflow.add_edge(agent, "content_marketing_manager")

# Define conditional transitions from the manager (based on `.next`)
workflow.add_conditional_edges(
    "content_marketing_manager",
    lambda x: x["next"],
    {agent: agent for agent in content_marketing_team} | {"FINISH": END}
)

# Define the starting point of the graph
workflow.set_entry_point("content_marketing_manager")

# Compile the entire workflow into a runnable app
multiagent = workflow.compile()

# ========================
# 🚀 10. Run the Application!
# ========================

if __name__ == "__main__":
    # User input to start the agent cycle
    input_message = HumanMessage(
        content="""Write me a report of 100 words on the benefits of lifting heavy weights"""
    )

    # Run the graph with a recursion limit to avoid infinite loops
    for step in multiagent.stream({"messages": [input_message]}, {"recursion_limit": 150}):
        if "__end__" not in step:
            print(step, "\n\n-----------------------------\n")
