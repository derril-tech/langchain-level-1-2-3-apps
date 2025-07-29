import os
import hashlib
from pathlib import Path
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import LanceDB
from langchain_openai import OpenAIEmbeddings
import lancedb
from dotenv import load_dotenv

load_dotenv()

# Connect to local LanceDB folder
ldb_connection = lancedb.connect(".lancedb")
collection_name = "pdf_rag_collection"

# Load existing collection or create new one
vector_store = LanceDB(
    connection=ldb_connection,
    embedding=OpenAIEmbeddings(),
    table_name=collection_name
)

def hash_text(text: str) -> str:
    """Generate a unique hash for a given text chunk (used for deduplication)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def ingest_single_pdf(file_path: str):
    """Ingest one PDF file (used by /upload endpoint)."""
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Generate hashes for current chunks
    new_docs = []
    existing_hashes = {
        hash_text(doc.page_content)
        for doc in vector_store.similarity_search(" ", k=1000)
    }

    for doc in documents:
        chunk_hash = hash_text(doc.page_content)
        if chunk_hash not in existing_hashes:
            doc.metadata["hash"] = chunk_hash
            doc.metadata["source"] = file_path
            new_docs.append(doc)

    if new_docs:
        vector_store.add_documents(new_docs)
        print(f"✅ Ingested {len(new_docs)} new chunks from {os.path.basename(file_path)}")
    else:
        print(f"ℹ️ No new content found in {os.path.basename(file_path)} — already ingested.")

def ingest_all_pdfs_in_folder(folder_path: str = "pdf-documents"):
    """Ingest all PDFs in the given folder, skipping duplicates."""
    pdf_files = Path(folder_path).rglob("*.pdf")
    for file_path in pdf_files:
        ingest_single_pdf(str(file_path))

if __name__ == "__main__":
    ingest_all_pdfs_in_folder()
    print("✅ Finished ingesting all available PDFs.")
