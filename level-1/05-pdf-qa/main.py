
---

### 🧠 `main.py`

```python
# main.py

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.document_loaders import PyPDFLoader
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load the PDF file
pdf_path = "example.pdf"  # Make sure this PDF exists in the same folder
loader = PyPDFLoader(pdf_path)
pages = loader.load()

# Combine all text from pages
full_text = "\n".join([page.page_content for page in pages])

# Example question
user_question = "What is the main topic discussed in the PDF?"

# Prompt for answering based on PDF content
template = """
You are given the text of a PDF document.

Document:
{text}

Question:
{question}

Answer in 2-3 sentences.
"""

prompt = PromptTemplate(
    input_variables=["text", "question"],
    template=template,
)

llm = ChatOpenAI(temperature=0)
chain = LLMChain(llm=llm, prompt=prompt)

# Run chain
response = chain.run({"text": full_text, "question": user_question})

print("📄 Answer:\n")
print(response)
