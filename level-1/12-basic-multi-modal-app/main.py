# main.py

import os
import base64
import uuid
from dotenv import load_dotenv
from PIL import Image
import mimetypes

from unstructured.partition.pdf import partition_pdf

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain.storage import InMemoryStore
from langchain.retrievers.multi_vector import MultiVectorRetriever

from langchain.schema import SystemMessage, HumanMessage

# -----------------------------
# STEP 1: Load environment + setup
# -----------------------------
load_dotenv()
pdf_path = "startupai-financial-report-v2.pdf"
output_folder = "figures"
os.makedirs(output_folder, exist_ok=True)

# Ensure OCR is enabled for unstructured
os.environ["OCR_AGENT"] = "pytesseract"

# -----------------------------
# STEP 2: Partition the PDF
# -----------------------------
raw_pdf_elements = partition_pdf(
    filename=pdf_path,
    extract_images_in_pdf=True,
    infer_table_structure=True,
    output_image_dir_path=output_folder,
)

# -----------------------------
# STEP 3: Separate elements
# -----------------------------
text_elements, table_elements, image_paths = [], [], []

for element in raw_pdf_elements:
    if "Table" in str(type(element)):
        table_elements.append(element.text)
    elif "Text" in str(type(element)):
        text_elements.append(element.text)

for fname in os.listdir(output_folder):
    if fname.lower().endswith((".png", ".jpg", ".jpeg")):
        image_paths.append(os.path.join(output_folder, fname))

# -----------------------------
# STEP 4: Initialize LLMs + Embedder
# -----------------------------
llm_text = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
llm_vision = ChatOpenAI(model="gpt-4o", temperature=0, max_tokens=500)
embedder = OpenAIEmbeddings()

# -----------------------------
# STEP 5: Summarize and assign unique IDs
# -----------------------------
summaries = []         # Vector DB content
raw_docs = {}          # UID → Original content map

# -- Text
for i, chunk in enumerate(text_elements):
    messages = [
        SystemMessage(content="You are a helpful assistant that summarizes PDF text."),
        HumanMessage(content=f"Summarize the following:\n\n{chunk}")
    ]
    summary = llm_text.invoke(messages).content
    uid = str(uuid.uuid4())
    summaries.append(Document(page_content=summary, metadata={"uid": uid, "type": "text"}))
    raw_docs[uid] = chunk

# -- Tables
for i, table in enumerate(table_elements):
    messages = [
        SystemMessage(content="You are a helpful assistant that summarizes table data."),
        HumanMessage(content=f"Summarize the following table:\n\n{table}")
    ]
    summary = llm_text.invoke(messages).content
    uid = str(uuid.uuid4())
    summaries.append(Document(page_content=summary, metadata={"uid": uid, "type": "table"}))
    raw_docs[uid] = table

# -- Images (base64)
for i, path in enumerate(image_paths):
    with open(path, "rb") as f:
        img_bytes = f.read()
        b64_image = base64.b64encode(img_bytes).decode("utf-8")

    mime = mimetypes.guess_type(path)[0] or "image/png"
    image_dict = {
        "type": "image_url",
        "image_url": {"url": f"data:{mime};base64,{b64_image}"}
    }

    messages = [
        SystemMessage(content="You are an expert at describing images."),
        HumanMessage(content=[
            image_dict,
            {"type": "text", "text": "Describe this image in detail from a PDF report."}
        ])
    ]
    summary = llm_vision.invoke(messages).content
    uid = str(uuid.uuid4())
    summaries.append(Document(page_content=summary, metadata={"uid": uid, "type": "image"}))
    raw_docs[uid] = f"<Image: {os.path.basename(path)}>"

# -----------------------------
# STEP 6: Store in Chroma + DocStore
# -----------------------------
vectorstore = Chroma.from_documents(
    summaries,
    embedding=embedder,
    collection_name="multi_modal_rag"
)

docstore = InMemoryStore()
for uid, content in raw_docs.items():
    docstore.mset([(uid, content)])

retriever = MultiVectorRetriever(
    vectorstore=vectorstore,
    docstore=docstore,
    id_key="uid",
)

# -----------------------------
# STEP 7: Run a test query
# -----------------------------
query = "What is the ROI and total sales of the company?"
results = retriever.get_relevant_documents(query)

print("\n--- RAG Results for Query ---")
for i, doc in enumerate(results):
    print(f"[{i+1}] {doc}\n")

