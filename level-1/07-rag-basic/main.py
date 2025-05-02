
---

### 🧠 `main.py`

```python
# main.py

from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import os
from dotenv import load_dotenv

# Load OpenAI key
load_dotenv()

# Load a document to be used as the knowledge base
loader = TextLoader("rag_source.txt")  # Place your RAG source text file here
documents = loader.load()

# Split the document into manageable chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
split_docs = text_splitter.split_documents(documents)

# Create a vector store using embeddings
embedding = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(split_docs, embedding)

# Set up the retriever and QA chain
retriever = vectorstore.as_retriever()
llm = ChatOpenAI(temperature=0)
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Ask a question
question = "What are the key takeaways from the document?"
answer = qa.run(question)

print("🧠 RAG Answer:\n")
print(answer)
