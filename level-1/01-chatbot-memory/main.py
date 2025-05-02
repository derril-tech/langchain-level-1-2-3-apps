# main.py

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

# Load environment variables (for OPENAI_API_KEY)
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(temperature=0)

# Set up memory for the conversation
memory = ConversationBufferMemory()

# Create the conversation chain with memory
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

print("💬 Chatbot with Memory is running. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in {"exit", "quit"}:
        print("👋 Goodbye!")
        break

    response = conversation.predict(input=user_input)
    print(f"Bot: {response}\n")
