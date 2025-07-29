from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from langserve import add_routes
from app.rag_chain import final_chain
from app.ingest import ingest_single_pdf
from app.chat_memory import save_chat, get_chat_history
import os
import shutil

from app.chat_db import init_db, save_chat, get_all_chats
from fastapi.responses import JSONResponse


app = FastAPI()

# Allow frontend (e.g., Vite dev server) to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount your LangChain RAG chain under /rag
add_routes(app, final_chain, path="/rag")


# Directory where uploaded PDFs are stored
UPLOAD_FOLDER = "app/data"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 📤 Upload + Embed PDF (used by React frontend)
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    try:
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        ingest_single_pdf(file_path)
        return {"message": f"✅ {file.filename} uploaded and embedded successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 💬 Save a single chat message (React chat box)
@app.post("/chat")
async def chat(question: str = Form(...)):
    response = final_chain.invoke({"question": question})
    answer = response.get("answer", "")
    save_chat(question, answer)
    return {"question": question, "answer": answer}

# 🕒 Retrieve chat history
@app.get("/history")
async def history():
    return JSONResponse(content=get_chat_history())


# Initialize DB on startup
init_db()

@app.post("/save_chat")
async def save_chat_endpoint(data: dict):
    question = data.get("question")
    answer = data.get("answer")
    if not question or not answer:
        return JSONResponse(status_code=400, content={"error": "Missing question or answer."})
    save_chat(question, answer)
    return {"message": "Chat saved successfully."}

@app.get("/chat-history")
async def fetch_chat_history():
    history = get_all_chats()
    return {"history": history}

