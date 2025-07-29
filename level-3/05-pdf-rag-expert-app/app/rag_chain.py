# app/rag_chain.py
from operator import itemgetter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableLambda
from langchain_community.vectorstores.lancedb import LanceDB
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from pydantic import BaseModel
import lancedb
import os

load_dotenv()

# =====================================================================
# 🧠 Goal:
# We are now using LanceDB instead of PGVector for our vector database.
# LanceDB is a lightweight, local-first vector DB that stores data on disk.
# =====================================================================

# ---------------------------------------------------------------------
# 📁 1. Setup LanceDB connection (local, file-based)
# ---------------------------------------------------------------------
ldb_connection = lancedb.connect(".lancedb")
vector_store = LanceDB(
    connection=ldb_connection,
    embedding=OpenAIEmbeddings(),
    table_name="pdf_rag_collection"
)
retriever = vector_store.as_retriever()

# ---------------------------------------------------------------------
# 🤖 2. Setup LLM (GPT-4o)
# ---------------------------------------------------------------------
llm = ChatOpenAI(model="gpt-4o")

# ---------------------------------------------------------------------
# 🧾 3. Prompt Template
# ---------------------------------------------------------------------
ANSWER_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant answering questions about logistics-related PDFs. "
               "Use only the provided context. If the answer is not contained in the context, say you don't know."),
    ("human", "Context:\n{context}\n\nQuestion: {question}")
])

# ---------------------------------------------------------------------
# 📥 4. Input Schema for LangServe
# ---------------------------------------------------------------------
class QuestionInput(BaseModel):
    question: str

# ---------------------------------------------------------------------
# 🧬 5. Build Inner Chain
# ---------------------------------------------------------------------
inner_chain = (
    RunnableParallel(
        context=itemgetter("question") | retriever,
        question=itemgetter("question")
    ) |
    RunnableParallel(
        answer=ANSWER_PROMPT | llm,
        docs=itemgetter("context")
    )
)

# ---------------------------------------------------------------------
# 🌐 6. Final Chain with Pydantic schema and LangServe-compatible output
# ---------------------------------------------------------------------
# This wraps the inner_chain and ensures it:
# - Accepts { "question": "..." } as input
# - Returns { "answer": { content: "..." } }
# ---------------------------------------------------------------------
def wrap_langserve(input: QuestionInput):
    result = inner_chain.invoke({"question": input.question})
    return {"answer": result["answer"]}  # required format for LangServe frontend

final_chain = RunnableLambda(wrap_langserve).with_types(input_type=QuestionInput)

"""
===========================================================================
📘  NOTES – LangChain RAG Chain with LanceDB (rag_chain.py)
===========================================================================

✅ Key Fix:
LangServe’s POST /invoke requires:
    1. A typed input (Pydantic model)
    2. A Runnable that returns a clean dict like: { "answer": { content: "..." } }

So we wrap our multi-stage chain in a simple `RunnableLambda` that:
    ➤ accepts `QuestionInput`
    ➤ extracts `.question`
    ➤ invokes the inner chain
    ➤ formats the output correctly

Now it works end-to-end with:
    - LangServe Playground (/rag/playground)
    - React frontend (axios POST)

===========================================================================

"""
