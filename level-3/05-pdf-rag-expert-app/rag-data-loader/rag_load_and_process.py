# rag-data-loader/rag_load_and_process.py

import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, UnstructuredPDFLoader
from langchain.text_splitter import SemanticChunker
from langchain_community.vectorstores.pgvector import PGVector
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from tqdm import tqdm

# Load environment variables
load_dotenv()

# Postgres connection string
CONNECTION_STRING = "postgresql+psycopg://postgres:postgres@localhost:5432/pdf_rag_db"

# Directory where PDFs are stored
PDF_DIRECTORY = "./pdf-documents"

# Load documents from PDF directory
print("🔍 Loading PDF documents...")
loader = DirectoryLoader(PDF_DIRECTORY, glob="**/*.pdf", loader_cls=UnstructuredPDFLoader)
docs = loader.load()

# Flatten doc output in case of nested format
flattened_docs = [doc for doc in docs if doc]

# Use a semantic chunker for smarter text splits
print("✂️ Splitting documents into semantic chunks...")
text_splitter = SemanticChunker(OpenAIEmbeddings())
chunks = text_splitter.split_documents(flattened_docs)

# Create vector store and persist it in PGVector
print("💾 Storing embeddings in PGVector...")
vectorstore = PGVector.from_documents(
    documents=chunks,
    embedding=OpenAIEmbeddings(),
    collection_name="pdf_rag_collection",
    connection_string=CONNECTION_STRING,
)

print("✅ Done! PDF embeddings loaded and stored.")
