from typing import List

# === LangChain + OpenAI (Plugin-based) Imports ===
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.retrieval_qa.base import RetrievalQA

# === LangChain Community Components ===
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders.pdf import PyPDFLoader

# === LangChain Text Processing ===
from langchain_text_splitters import RecursiveCharacterTextSplitter

# === Pydantic schema for question-based endpoint ===
from schemas import QuestionRequest


from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
import schemas
import crud
from database import SessionLocal

from uuid import uuid4

# === Instantiate Language Models ===
llm = OpenAI()  # Used in RetrievalQA
langchain_llm = OpenAI(temperature=0)  # Used in summarization

# === API Router for /pdfs endpoints ===
router = APIRouter(prefix="/pdfs")

# === Dependency Injection for DB Session ===
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# === CRUD PDF Routes ===

@router.post("", response_model=schemas.PDFResponse, status_code=status.HTTP_201_CREATED)
def create_pdf(pdf: schemas.PDFRequest, db: Session = Depends(get_db)):
    return crud.create_pdf(db, pdf)

@router.post("/upload", response_model=schemas.PDFResponse, status_code=status.HTTP_201_CREATED)
def upload_pdf(
    file: UploadFile = File(...),
    file_name: str = Form(...),
    db: Session = Depends(get_db)
):
    return crud.upload_pdf(db, file, file_name)

@router.get("", response_model=List[schemas.PDFResponse])
def get_pdfs(selected: bool = None, db: Session = Depends(get_db)):
    return crud.read_pdfs(db, selected)

@router.get("/{id}", response_model=schemas.PDFResponse)
def get_pdf_by_id(id: int, db: Session = Depends(get_db)):
    pdf = crud.read_pdf(db, id)
    if pdf is None:
        raise HTTPException(status_code=404, detail="PDF not found")
    return pdf

@router.put("/{id}", response_model=schemas.PDFResponse)
def update_pdf(id: int, pdf: schemas.PDFRequest, db: Session = Depends(get_db)):
    updated_pdf = crud.update_pdf(db, id, pdf)
    if updated_pdf is None:
        raise HTTPException(status_code=404, detail="PDF not found")
    return updated_pdf

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_pdf(id: int, db: Session = Depends(get_db)):
    if not crud.delete_pdf(db, id):
        raise HTTPException(status_code=404, detail="PDF not found")
    return {"message": "PDF successfully deleted"}

# === LangChain Summarization Route ===

summarize_template_string = """
        Provide a summary for the following text:
        {text}
"""

summarize_prompt = PromptTemplate(
    template=summarize_template_string,
    input_variables=['text'],
)

summarize_chain = LLMChain(
    llm=langchain_llm,
    prompt=summarize_prompt,
)

@router.post('/summarize-text')
async def summarize_text(text: str):
    summary = summarize_chain.run(text=text)
    return {'summary': summary}

# === LangChain PDF Q&A Route ===

@router.post("/qa-pdf/{id}")
def qa_pdf_by_id(id: int, question_request: QuestionRequest, db: Session = Depends(get_db)):
    pdf = crud.read_pdf(db, id)
    if pdf is None:
        raise HTTPException(status_code=404, detail="PDF not found")

    # Load PDF and chunk it
    loader = PyPDFLoader(pdf.file)
    document = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=400)
    document_chunks = text_splitter.split_documents(document)

    # Embed and store chunks
    embeddings = OpenAIEmbeddings()
    stored_embeddings = FAISS.from_documents(document_chunks, embeddings)

    # Setup Retrieval QA chain
    QA_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=stored_embeddings.as_retriever()
    )

    question = question_request.question
    answer = QA_chain.run(question)
    return answer
