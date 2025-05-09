# ================================================
# LangChain Beginner Example with GPT-4o (2024-08-06)
# ================================================

# Load environment variables (like your API key)
import os
from dotenv import load_dotenv, find_dotenv

# Find and load the .env file that contains your API key
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]

# ----------------------------------------
# Import the LLM from LangChain's OpenAI module
from langchain_openai import ChatOpenAI

# Initialize the LLM with GPT-4o
llm = ChatOpenAI(model="gpt-4o-2024-08-06")

# ----------------------------------------
# Prepare documents to be stored in the vector database
from langchain_core.documents import Document

documents = [
    Document(
        page_content="John F. Kennedy served as the 35th president of the United States from 1961 until his assassination in 1963.",
        metadata={"source": "us-presidents-doc"},
    ),
    Document(
        page_content="Robert F. Kennedy was a key political figure and served as the U.S. Attorney General; he was also assassinated in 1968.",
        metadata={"source": "us-politics-doc"},
    ),
    Document(
        page_content="The Kennedy family is known for their significant influence in American politics and their extensive philanthropic efforts.",
        metadata={"source": "kennedy-family-doc"},
    ),
    Document(
        page_content="Edward M. Kennedy, often known as Ted Kennedy, was a U.S. Senator who played a major role in American legislation over several decades.",
        metadata={"source": "us-senators-doc"},
    ),
    Document(
        page_content="Jacqueline Kennedy Onassis, wife of John F. Kennedy, was an iconic First Lady known for her style, poise, and dedication to cultural and historical preservation.",
        metadata={"source": "first-lady-doc"},
    ),
]

# ----------------------------------------
# Store the documents in a vector database using Chroma and OpenAI embeddings
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

# Create a vector store by embedding the documents
vectorstore = Chroma.from_documents(
    documents,
    embedding=OpenAIEmbeddings(),
)

# ----------------------------------------
# Run a basic similarity search for the word "John"
response = vectorstore.similarity_search("John")

print("\n----------\n")
print("Search for John in the vector database:")
print("\n----------\n")
print(response)
print("\n----------\n")

# Run the same search but also include similarity scores
response = vectorstore.similarity_search_with_score("John")

print("\n----------\n")
print("Search for John in the vector database (with scores):")
print("\n----------\n")
print(response)
print("\n----------\n")

# ----------------------------------------
# Use the vectorstore as a retriever with specific settings (top 1 result)
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 1},
)

# Batch search for "John" and "Robert"
response = retriever.batch(["John", "Robert"])

print("\n----------\n")
print("Search for John and Robert in the vector database (with vectorstore as retriever):")
print("\n----------\n")
print(response)
print("\n----------\n")

# ----------------------------------------
# Alternative way to create a retriever using RunnableLambda
from typing import List
from langchain_core.runnables import RunnableLambda

# Wrap the similarity_search function with RunnableLambda and bind top 1 result
retriever = RunnableLambda(vectorstore.similarity_search).bind(k=1)

# Batch search using the runnable retriever
response = retriever.batch(["John", "Robert"])

print("\n----------\n")
print("Search for John and Robert in the vector database (select top result):")
print("\n----------\n")
print(response)
print("\n----------\n")

# ----------------------------------------
# Create a prompt and chain for asking questions based on retrieved documents
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# Define the prompt template
message = """
Answer this question using the provided context only.

{question}

Context:
{context}
"""

# Use the prompt template in a LangChain-compatible format
prompt = ChatPromptTemplate.from_messages([("human", message)])

# Combine retriever, prompt, and LLM into a chain
chain = {
    "context": retriever,
    "question": RunnablePassthrough()} | prompt | llm

# Ask a question using the chain
response = chain.invoke("tell me about Jackie")

print("\n----------\n")
print("tell me about Jackie (simple retriever):")
print("\n----------\n")
print(response.content)
print("\n----------\n")

# ================================================
#  Notes - LangChain Concepts
# ================================================

"""
1. Environment Variables:
   We load your API key securely using `dotenv`. This allows you to store credentials in a `.env` file rather than in the code.

2. ChatOpenAI:
   This sets up access to OpenAI's GPT models. We're using `gpt-4o-2024-08-06`, a more advanced and faster version.

3. Documents:
   Each `Document` contains some text (`page_content`) and metadata (like a source label). These will be used in retrieval tasks.

4. Embeddings and Vector Store:
   `OpenAIEmbeddings` turns text into numerical vectors. `Chroma` stores these vectors and lets us search them efficiently based on similarity.

5. Similarity Search:
   This is how we retrieve relevant documents. A search for "John" will return documents that talk about John Kennedy or similar topics.

6. similarity_search_with_score():
   This is like similarity_search but also shows how closely each result matches your query (as a score).

7. Retriever:
   Instead of manually calling similarity_search every time, we can turn our vectorstore into a `retriever`, which can be used in pipelines.

8. RunnableLambda:
   This wraps a function (like similarity_search) to make it usable inside LangChain pipelines and lets you bind parameters.

9. Prompt Template:
   This helps you structure how questions are asked to the LLM. You can insert `{question}` and `{context}` dynamically.

10. Chain:
    The chain ties everything together. It:
      - Retrieves relevant context
      - Formats the prompt
      - Sends it to the LLM
      - Returns an answer based only on that context

11. Final Invocation:
    We ask, "tell me about Jackie", and the chain fetches related info and gives an LLM-based answer based on that context.

Useful for tutorials:
💡 This example shows how to connect retrieval with LLMs using LangChain’s modular system—great for building chatbots or assistants that answer based on real documents.
"""
