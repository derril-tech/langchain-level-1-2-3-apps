# Step 1: Load environment variables (like API keys) from a .env file
import os
from dotenv import load_dotenv, find_dotenv

# Automatically find and load the .env file
_ = load_dotenv(find_dotenv())

# Read the OpenAI API key from the environment
openai_api_key = os.environ["OPENAI_API_KEY"]

# Step 2: Import the LLM from LangChain and define the model
from langchain_openai import ChatOpenAI

# Initialize the ChatOpenAI model with gpt-4o
llm = ChatOpenAI(model="gpt-4o-2024-08-06")

# Step 3: Import all necessary LangChain modules
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, HumanMessagePromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Optional import (can be useful for HTML parsing)
import bs4

# Step 4: Load the input document
loader = TextLoader("./data/be-good.txt")

# Read the contents of the document
docs = loader.load()

# Step 5: Split the document into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,       # Each chunk has ~1000 characters
    chunk_overlap=200      # Overlap 200 characters between chunks for better context
)

# Apply the splitter to your documents
splits = text_splitter.split_documents(docs)

# Step 6: Convert the text chunks into vector embeddings using Chroma
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

# Create a retriever to search over the vectorstore
retriever = vectorstore.as_retriever()

# Step 7: Define the RAG prompt template directly (since hub is incompatible with some Python versions)
prompt = ChatPromptTemplate(
    input_variables=['context', 'question'],
    metadata={
        'lc_hub_owner': 'rlm',
        'lc_hub_repo': 'rag-prompt',
        'lc_hub_commit_hash': '50442af133e61576e74536c6556cefe1fac147cad032f4377b60c436e6cdcb6e'
    },
    messages=[
        HumanMessagePromptTemplate(
            prompt=PromptTemplate(
                input_variables=['context', 'question'],
                template="You are an assistant for question-answering tasks. "
                         "Use the following pieces of retrieved context to answer the question. "
                         "If you don't know the answer, just say that you don't know. "
                         "Use three sentences maximum and keep the answer concise.\n"
                         "Question: {question} \nContext: {context} \nAnswer:"
            )
        )
    ]
)

# Step 8: Define a function to format the retrieved documents
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Step 9: Create the RAG chain pipeline
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Step 10: Ask a question and get the response from the RAG chain
response = rag_chain.invoke("What is this article about?")

# Step 11: Print the question and the model's response
print("\n----------\n")
print("What is this article about?")
print("\n----------\n")
print(response)
print("\n----------\n")



# ------------------------------------------------------------------
# 🔰 LangChain RAG Pipeline - Step-by-Step Notes
# ------------------------------------------------------------------

# ✅ Step 1: Environment Variables
# We load environment variables (like the OpenAI API key) from a `.env` file so we can keep sensitive info outside of the code.

# ✅ Step 2: Language Model Setup
# We initialize the ChatOpenAI object using the "gpt-4o-2024-08-06" model. This will be used to generate our responses.

# ✅ Step 3: Imports
# LangChain provides many tools: for loading text, splitting it, embedding it, and interacting with LLMs in a pipeline.

# ✅ Step 4: Load Documents
# We use `TextLoader` to read a local `.txt` file into memory. This becomes the base content our model will use.

# ✅ Step 5: Text Splitting
# Long documents are broken into overlapping chunks using `RecursiveCharacterTextSplitter`. This helps preserve meaning during retrieval.

# ✅ Step 6: Embeddings and Vector Store
# Text chunks are converted to vector embeddings using OpenAI, then stored in a Chroma vector database, allowing fast semantic search.

# ✅ Step 7: Prompt Template
# We define a structured prompt manually. It tells the LLM how to answer questions using only retrieved context.

# ✅ Step 8: Format Function
# Converts the retrieved docs into plain text format, ready to be passed to the prompt.

# ✅ Step 9: Build the Chain
# This combines: retriever → formatted docs → prompt → LLM → output parser, forming a full Retrieval-Augmented Generation (RAG) chain.

# ✅ Step 10: Run the Chain
# We pass a user question to the chain and get a concise answer based on the loaded document.

# ✅ Step 11: Output
# Finally, we print the question and the LLM's answer to the console.

# ------------------------------------------------------------------
# This is a simple and complete example of a Retrieval-Augmented Generation (RAG) system using LangChain + GPT-4o.
# Great starting point for beginner LangChain developers. ✅
# ------------------------------------------------------------------
