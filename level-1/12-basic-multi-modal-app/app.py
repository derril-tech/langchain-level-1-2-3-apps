# app.py

import streamlit as st
from dotenv import load_dotenv
import os

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.storage import InMemoryStore
from langchain.retrievers.multi_vector import MultiVectorRetriever

# ----------------------------
# STEP 1: Load environment and setup
# ----------------------------
load_dotenv()
embedder = OpenAIEmbeddings()

# ----------------------------
# STEP 2: Load vectorstore and docstore
# ----------------------------
# Important: these must match what you used in main.py
VECTOR_COLLECTION = "multi_modal_rag"
vectorstore = Chroma(
    collection_name=VECTOR_COLLECTION,
    embedding_function=embedder,
    persist_directory=".chroma_store"  # optional if you persist
)

# Simulated docstore with example contents (in real case, reload from disk)
docstore = InMemoryStore()
# You could serialize raw_docs from main.py and load them here
# For demo purposes, we’ll leave it empty

retriever = MultiVectorRetriever(
    vectorstore=vectorstore,
    docstore=docstore,
    id_key="uid"
)

# ----------------------------
# STEP 3: Streamlit UI
# ----------------------------
st.set_page_config(page_title="MultiModal RAG App", layout="wide")
st.title("🧠 MultiModal PDF Q&A (LangChain + GPT-4o)")

query = st.text_input("Ask a question about your PDF:", "")

if query:
    with st.spinner("Thinking..."):
        results = retriever.get_relevant_documents(query)

    st.subheader("📄 RAG Answers")
    for i, doc in enumerate(results):
        st.markdown(f"**Result {i+1}**")
        st.write(doc.page_content)
        st.markdown("---")
