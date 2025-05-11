# -----------------------------------------
# LangChain + LangServe Deployment Example
# -----------------------------------------

# Load environment variables from a .env file
from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())  # Load environment variables silently
openai_api_key = os.environ["OPENAI_API_KEY"]  # Read the OpenAI API key

# Import LangChain and LangServe modules
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI
from langserve import add_routes

# -----------------------------
# Step 1: Create the LLM (GPT-4o)
# -----------------------------
# Initialize the OpenAI chat model with GPT-4o
llm = ChatOpenAI(model="gpt-4o-2024-08-06")

# -----------------------------
# Step 2: Define the prompt template
# -----------------------------
# This system message tells the LLM to translate the input text into the user's target language
system_template = "Translate the following into {language}:"

# Create a ChatPromptTemplate with system and user messages
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# -----------------------------
# Step 3: Create the output parser
# -----------------------------
# This parser turns the LLM's output into a plain string
parser = StrOutputParser()

# -----------------------------
# Step 4: Build the LangChain chain
# -----------------------------
# Combine prompt -> model -> parser into a single executable chain
chain = prompt_template | llm | parser

# -----------------------------
# Step 5: Create the FastAPI app
# -----------------------------
# FastAPI is used to serve the chain as an API
app = FastAPI(
    title="simpleTranslator",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

# -----------------------------
# Step 6: Add LangServe routes
# -----------------------------
# This adds the /chain/playground route to interact with the chain in a web browser
add_routes(
    app,
    chain,
    path="/chain",
)

# -----------------------------
# Step 7: Run the server
# -----------------------------
# This block ensures the server runs when you execute the script directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

# ---------------------------------------------
# ✨ Beginner Notes for LangChain Deployment ✨
# ---------------------------------------------
# 1. load_dotenv(): Loads your .env file so your API keys and environment variables are private.
# 2. ChatOpenAI(): This initializes your connection to OpenAI's GPT-4o model. You can change the model name here.
# 3. ChatPromptTemplate: Lets you build conversation-style prompts. You tell the system what to do ("translate") and pass user input dynamically.
# 4. StrOutputParser: A simple way to turn the model's response into a clean string.
# 5. The chain: This is the core LangChain concept—it's a pipeline of prompt → model → output parser.
# 6. FastAPI: A popular Python web framework. We use it here to expose your LangChain app as a web API.
# 7. LangServe: A helper to automatically wire your LangChain chain into FastAPI, complete with a built-in playground UI.
# 8. uvicorn.run(): Runs your FastAPI app locally at http://localhost:8000. You’ll find the interactive playground at /chain/playground.
#
# 🧠 Tip: This is a perfect setup to prototype translation apps or other basic LLM workflows, especially when you need quick feedback.
# 📦 To run this, make sure you’ve installed dependencies: pip install langserve[all] fastapi uvicorn python-dotenv
