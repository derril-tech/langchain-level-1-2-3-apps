# main.py
# ------------------------------
# LangChain RAG + LangSmith Evaluation
# Compatible with langchain==0.1.16, langsmith==0.1.17, pydantic<2.0
# ------------------------------

import os
from dotenv import load_dotenv, find_dotenv

# Load your environment variables from .env
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]

# === Imports ===
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.callbacks.tracers import LangChainTracer
import langsmith
from langchain import smith, chat_models

# === Load document ===
loader = TextLoader("data/be-good-and-how-not-to-die.txt")
documents = loader.load()

print(f"Document type: {type(documents)}")
print(f"Number of loaded documents: {len(documents)}")
print(f"First doc metadata: {documents[0].metadata}")
print(f"Character count: {len(documents[0].page_content)}")

# === Split document ===
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=3000,
    chunk_overlap=400,
)
document_chunks = text_splitter.split_documents(documents)
print(f"Now you have {len(document_chunks)} chunks.")

# === Embedding and Vector Store ===
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(document_chunks, embeddings)

# === LangSmith Tracer ===
tracer = LangChainTracer(project_name="SimpleRAG3")

# === LLM Setup ===
llm = ChatOpenAI(model="gpt-4o-2024-08-06", temperature=0)

# === Prompt Template ===
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = PromptTemplate.from_template(template)

# === Corrected Runnable Chain (works with dict inputs from LangSmith dataset) ===
from langchain.schema.runnable import RunnableMap

chain = (
    RunnableMap({
        "context": lambda x: x["question"],  # ensure only the question string goes to retriever
        "question": lambda x: x["question"],  # pass through for prompt
    })
    | prompt
    | llm
    | StrOutputParser()
)


# === Local Test Run ===
response = chain.invoke({"question": "What is the target audience of this article?"})
print(f"Test response: {response}")

# === LangSmith Evaluation Setup ===
eval_config = smith.RunEvalConfig(
    evaluators=["cot_qa"],  # built-in chain-of-thought evaluator
    custom_evaluators=[],
    eval_llm=chat_models.ChatOpenAI(model="gpt-4", temperature=0)
)

# === Run Chain Evaluation on LangSmith Dataset ===
client = langsmith.Client()
chain_results = client.run_on_dataset(
    dataset_name="simpleRagDataSet",  # must exist in your LangSmith UI
    llm_or_chain_factory=chain,
    evaluation=eval_config,
    project_name="test-loyal-conference-76-v3",
    concurrency_level=5,
    verbose=True,
)

