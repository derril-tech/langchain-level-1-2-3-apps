# -------------------------------
# 1. Load API Key from .env file
# -------------------------------
import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env
_ = load_dotenv(find_dotenv())

# Store OpenAI API Key in a variable
openai_api_key = os.environ["OPENAI_API_KEY"]

# -------------------------------
# 2. Import LLM from LangChain
# -------------------------------
from langchain_openai import ChatOpenAI

# Initialize the language model (LLM) using GPT-3.5-turbo
llm = ChatOpenAI(model="gpt-4o-2024-08-06")

# -------------------------------
# 3. Load a PDF Document
# -------------------------------
from langchain_community.document_loaders import PyPDFLoader

# Define the path to your PDF file
file_path = "./data/Be_Good.pdf"

# Load the PDF using LangChain's PDF loader
loader = PyPDFLoader(file_path)
docs = loader.load()  # Extract all text as LangChain Document objects

# -------------------------------
# 4. Split the Document into Chunks
# -------------------------------
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Create a text splitter that breaks text into chunks of 1000 characters
# with a 200-character overlap to preserve context
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# Apply the splitter to the loaded documents
splits = text_splitter.split_documents(docs)

# -------------------------------
# 5. Embed and Store Text Chunks in Vector Database
# -------------------------------
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

# Create a vector database from document chunks using OpenAI embeddings
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

# Convert the vectorstore into a retriever that can search for relevant chunks
retriever = vectorstore.as_retriever()

# -------------------------------
# 6. Define Prompt and Create the RAG Chain
# -------------------------------
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# Define the system prompt that guides how the assistant should respond
system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise.\n\n{context}"
)

# Set up the final prompt structure for the chat
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# Combine the LLM and prompt into a question-answering chain
question_answer_chain = create_stuff_documents_chain(llm, prompt)

# Create the full retrieval-augmented generation chain
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# -------------------------------
# 7. Ask a Question and Print Results
# -------------------------------

# Send a question to the RAG chain
response = rag_chain.invoke({"input": "What is this article about?"})

# Display the formatted output
print("\n----------\n")
print("What is this article about?")
print("\n----------\n")
print(response["answer"])
print("\n----------\n")
print("Show metadata:")
print("\n----------\n")
print(response["context"][0].metadata)
print("\n----------\n")


"""
 NOTES: Understanding the Workflow of this LangChain Script

1. ENVIRONMENT SETUP:
   We start by securely loading our OpenAI API key using a `.env` file. This allows us to avoid hardcoding secrets.

2. LANGUAGE MODEL:
   We initialize `ChatOpenAI` with a specific model (`gpt-4o-2024-08-06`). This is the brain behind the assistant.

3. DOCUMENT LOADING:
   We load a PDF using `PyPDFLoader`, which breaks it into LangChain Document objects containing both text and metadata.

4. TEXT SPLITTING:
   Long documents are split into smaller chunks using `RecursiveCharacterTextSplitter`. This is important so the model doesn't get overwhelmed by too much text at once.

5. VECTOR STORE:
   Each chunk is converted into a numerical format (embedding) with `OpenAIEmbeddings` and stored in a Chroma vector database. This allows for fast and smart similarity searches.

6. PROMPT + CHAIN SETUP:
   We define how the assistant should behave using a system prompt. Then we build a RAG (Retrieval-Augmented Generation) chain that pulls in relevant context from the documents to help the model answer questions more accurately.

7. ASKING QUESTIONS:
   Finally, we ask the model a question ("What is this article about?") and print both the answer and the metadata (such as page number or source file) of the first supporting chunk.

This is a foundational LangChain Level 1 application — ideal for document Q&A systems, personal knowledge bases, and basic AI assistants using real documents.
"""
