import os
import warnings
from dotenv import load_dotenv, find_dotenv

# Suppress LangChain deprecation warnings for cleaner output
from langchain._api import LangChainDeprecationWarning
warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

# Load the OpenAI API key from a .env file
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]

# Import and initialize the ChatOpenAI model (GPT-4 Turbo)
from langchain_openai import ChatOpenAI
chatbot = ChatOpenAI(model="gpt-4o-2024-08-06")

# --- PART 1: Stateless Chat ---
# This is a simple chat without memory (no context retention)
from langchain_core.messages import HumanMessage

messages_to_chatbot = [
    HumanMessage(content="My favorite color is blue."),
]

response = chatbot.invoke(messages_to_chatbot)

print("\n----------\n")
print("My favorite color is blue.")
print("\n----------\n")
print(response.content)
print("\n----------\n")

response = chatbot.invoke([
    HumanMessage(content="What is my favorite color?")
])

print("\n----------\n")
print("What is my favorite color?")
print("\n----------\n")
print(response.content)
print("\n----------\n")

# --- PART 2: Stateful Chat using LangChain Memory ---
# Import core components for creating a memory-enabled chain
from langchain.chains import LLMChain  # Main abstraction that combines LLM, prompt, and memory into a single callable object
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder  # Used to structure the messages and memory into a reusable prompt format
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory  # Implements memory for the chat; uses a file-based history so that memory persists between runs

# Create a memory object to store conversation history
memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("messages.json"),  # File-based memory for persistence
    memory_key="messages",
    return_messages=True
)

# Create a chat prompt template that uses the memory context
prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

# Initialize the LLMChain with memory, prompt, and the chatbot
chain = LLMChain(
    llm=chatbot,
    prompt=prompt,
    memory=memory
)

# Interactions using the memory-enabled chain
response = chain.invoke("hello!")
print("\n----------\n")
print("hello!")
print("\n----------\n")
print(response)
print("\n----------\n")

response = chain.invoke("my name is Julio")
print("\n----------\n")
print("my name is Julio")
print("\n----------\n")
print(response)
print("\n----------\n")

response = chain.invoke("what is my name?")
print("\n----------\n")
print("what is my name?")
print("\n----------\n")
print(response)
print("\n----------\n")

"""
==============================
📝 Beginner's Notes (Tutorial Style)
==============================

1. ChatOpenAI (LangChain's wrapper around OpenAI Chat models)
   - Used to invoke chat-based LLMs like GPT-3.5 or GPT-4.
   - Stateless: Each interaction is independent unless memory is added.

2. HumanMessage
   - Represents a message from the user to the chatbot.
   - Must be wrapped before sending to `chatbot.invoke()`.

3. Memory (ConversationBufferMemory + FileChatMessageHistory)
   - Remembers past interactions.
   - File-based memory (`messages.json`) allows persistence across sessions.

4. ChatPromptTemplate and MessagesPlaceholder
   - Used to build dynamic prompts.
   - `MessagesPlaceholder` injects memory into the prompt.
   - `HumanMessagePromptTemplate` represents the current user input.

5. LLMChain
   - Combines a model, prompt, and memory into a reusable chain.
   - Automatically handles context injection from memory.

6. `chain.invoke("...")`
   - Sends input through the memory-enabled prompt and gets contextual output.

Example: After saying "my name is Julio", the chain remembers it and answers correctly when asked, "what is my name?"

Use this pattern to build memory-aware assistants, bots, or tools.
"""
