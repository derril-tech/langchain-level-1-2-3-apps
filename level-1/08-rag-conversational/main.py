
---

### 🧠 `main.py`

```python
# main.py

from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import ChatVectorDBChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load and split the document
loader = TextLoader("conversational_rag_source.txt")  # Place your source text here
documents = loader.load()
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
split_docs = splitter.split_documents(documents)

# Create embeddings and vectorstore
embedding = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(split_docs, embedding)

# Memory for maintaining chat history
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Set up LLM and RAG chain
llm = ChatOpenAI(temperature=0)
qa_chain = ChatVectorDBChain.from_llm(
    llm=llm,
    vectorstore=vectorstore,
    memory=memory
)

print("💬 Conversational RAG Chatbot is running. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in {"exit", "quit"}:
        print("👋 Goodbye!")
        break

    result = qa_chain.run(user_input)
    print(f"Bot: {result}\n")
