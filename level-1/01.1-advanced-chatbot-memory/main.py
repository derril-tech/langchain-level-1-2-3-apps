# --------------------
# 🧠 LangChain  Demo: Advanced ChatBot Memory & Sessions
# --------------------

# Suppress LangChain deprecation warnings for a cleaner output
import warnings
from langchain._api import LangChainDeprecationWarning
warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

# Load environment variables (like OpenAI API key) from .env file
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]

# Import OpenAI-powered chat model
from langchain_openai import ChatOpenAI
chatbot = ChatOpenAI(model="gpt-4-turbo")  # You can change the model name here

# --------------------
# 🤖 Basic Chat Usage
# --------------------

from langchain_core.messages import HumanMessage

# Create a message and send it to the chatbot
messagesToTheChatbot = [HumanMessage(content="My favorite color is blue.")]
response = chatbot.invoke(messagesToTheChatbot)

print("\n----------\n")
print("My favorite color is blue.")
print("\n----------\n")
print(response.content)
print("\n----------\n")

# Ask chatbot to recall the previous message (no memory yet!)
response = chatbot.invoke([HumanMessage(content="What is my favorite color?")])
print("\n----------\n")
print("What is my favorite color?")
print("\n----------\n")
print(response.content)
print("\n----------\n")

# --------------------
# 💾 Add Memory to the ChatBot
# --------------------

# ChatMessageHistory is an in-memory message history store provided by LangChain Community.
# It acts like a mini "notebook" that remembers previous messages in a chat session.
# This is useful when you want your chatbot to recall what was said earlier.
from langchain_community.chat_message_histories import ChatMessageHistory

# BaseChatMessageHistory is an abstract base class for all message history implementations.
# It defines the required structure and methods a memory class should have.
# We use it to make sure our `get_session_history()` function returns the correct type.
from langchain_core.chat_history import BaseChatMessageHistory

# RunnableWithMessageHistory is a wrapper that adds memory capabilities to a LangChain runnable (like a chatbot).
# It enables session-aware chat behavior, so your chatbot can have "conversations" that span multiple turns.
# This is key for building chatbots that remember things!
from langchain_core.runnables.history import RunnableWithMessageHistory

# 1.Simple memory store as (a python dictonary) to hold session history
chatbotMemory = {}

# 2. Fetch or create a session's chat history
# Define a function to retrieve or initialize chat history for a given session
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    # Check if this session ID already exists in our memory dictionary
    if session_id not in chatbotMemory:
        # If it doesn't exist, create a new ChatMessageHistory instance for it
        chatbotMemory[session_id] = ChatMessageHistory()
    # Return the chat history associated with this session ID
    return chatbotMemory[session_id]

# 3. Wrap chatbot with memory support
chatbot_with_message_history = RunnableWithMessageHistory(
    chatbot, 
    get_session_history
)

# --------------------
# 🧪 Try Session-Based Memory
# --------------------

# Session 1: store favorite color
session1 = {"configurable": {"session_id": "001"}}
response = chatbot_with_message_history.invoke(
    [HumanMessage(content="My favorite color is red.")],
    config=session1,
)
print("\n----------\n")
print("My favorite color is red.")
print("\n----------\n")
print(response.content)
print("\n----------\n")

# Ask chatbot to recall from session1
response = chatbot_with_message_history.invoke(
    [HumanMessage(content="What's my favorite color?")],
    config=session1,
)
print("\n----------\n")
print("What's my favorite color? (in session1)")
print("\n----------\n")
print(response.content)
print("\n----------\n")

# New session (session2): memory starts fresh
session2 = {"configurable": {"session_id": "002"}}
response = chatbot_with_message_history.invoke(
    [HumanMessage(content="What's my favorite color?")],
    config=session2,
)
print("\n----------\n")
print("What's my favorite color? (in session2)")
print("\n----------\n")
print(response.content)
print("\n----------\n")

# Session1 again: memory retained
response = chatbot_with_message_history.invoke(
    [HumanMessage(content="What's my favorite color?")],
    config=session1,
)
print("\n----------\n")
print("What's my favorite color? (in session1 again)")
print("\n----------\n")
print(response.content)
print("\n----------\n")

# Add name to session2
response = chatbot_with_message_history.invoke(
    [HumanMessage(content="Mi name is Derril.")],
    config=session2,
)
print("\n----------\n")
print("Mi name is Derril. (in session2)")
print("\n----------\n")
print(response.content)
print("\n----------\n")

# Recall name in session2
response = chatbot_with_message_history.invoke(
    [HumanMessage(content="What is my name?")],
    config=session2,
)
print("\n----------\n")
print("What is my name? (in session2)")
print("\n----------\n")
print(response.content)
print("\n----------\n")

# Recall favorite color in session1
response = chatbot_with_message_history.invoke(
    [HumanMessage(content="What is my favorite color?")],
    config=session1,
)
print("\n----------\n")
print("What is my favorite color? (in session1)")
print("\n----------\n")
print(response.content)
print("\n----------\n")

# Show/Print the chatbot memory
print(chatbotMemory)

# --------------------
# 🧠 Limited Memory Chain
# --------------------

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough

# Limit memory to the last N messages
def limited_memory_of_messages(messages, number_of_messages_to_keep=2):
    return messages[-number_of_messages_to_keep:]

# Create a system prompt with message placeholder
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer all questions to the best of your ability."),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Define the limited memory chain
limitedMemoryChain = (
    RunnablePassthrough.assign(messages=lambda x: limited_memory_of_messages(x["messages"]))
    | prompt 
    | chatbot
)

# Wrap the limited memory chain with memory history
chatbot_with_limited_message_history = RunnableWithMessageHistory(
    limitedMemoryChain,
    get_session_history,
    input_messages_key="messages",
)

# Store more facts in session1
response = chatbot_with_message_history.invoke(
    [HumanMessage(content="My favorite vehicles are Vespa scooters.")],
    config=session1,
)
print("\n----------\n")
print("My favorite vehicles are Vespa scooters. (in session1)")
print("\n----------\n")
print(response.content)
print("\n----------\n")

response = chatbot_with_message_history.invoke(
    [HumanMessage(content="My favorite city is Amsterdam.")],
    config=session1,
)
print("\n----------\n")
print("My favorite city is Amsterdam. (in session1)")
print("\n----------\n")
print(response.content)
print("\n----------\n")

# Ask with limited memory chain
response = chatbot_with_limited_message_history.invoke(
    {
        "messages": [HumanMessage(content="what is my favorite color?")],
    },
    config=session1,
)
print("\n----------\n")
print("what is my favorite color? (chatbot with memory limited to the last 2 messages)")
print("\n----------\n")
print(response.content)
print("\n----------\n")

# Ask again with full memory
response = chatbot_with_message_history.invoke(
    [HumanMessage(content="what is my favorite color?")],
    config=session1,
)
print("\n----------\n")
print("what is my favorite color? (chatbot with unlimited memory)")
print("\n----------\n")
print(response.content)
print("\n----------\n")


# --------------------
# 📚 BEGINNER NOTES (Put in .py as comments)
# --------------------

"""
NOTES: LangChain Chatbot with Memory

1. ✅ API Setup:
   We use the `dotenv` package to load your OpenAI API key securely from a `.env` file.

2. 🤖 ChatOpenAI:
   This is LangChain's wrapper around OpenAI's GPT models. We use `ChatOpenAI` to create a chatbot instance.

3. 💬 HumanMessage:
   This class represents messages from the user. You pass it to the chatbot to simulate a chat.

4. 🧠 No Memory by Default:
   Without memory, the chatbot cannot recall anything from previous interactions. It treats each message in isolation.

5. 💾 Adding Memory:
   Using `RunnableWithMessageHistory` and `ChatMessageHistory`, we can persist chat history by session.

6. 🪪 Sessions:
   We simulate sessions using a `session_id` (like "001", "002"). Each session can remember its own conversation history.

7. 🔄 Switching Between Sessions:
   Each session has isolated memory. So the chatbot remembers "Julio" in session2 but not in session1.

8. 🧠 Limited Memory Chains:
   Sometimes we want the chatbot to remember only a few recent messages. We use a function to truncate the memory to the last N messages.

9. 🧪 Comparing Behaviors:
   We compare how the chatbot responds with full memory vs. limited memory to see the effect of chat history.

This is a great starting point for understanding how LangChain handles chat, memory, and multi-session context!
"""
