
---

### 🧠 `main.py`

```python
# main.py

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langserve import add_routes
from fastapi import FastAPI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the LLM and prompt
llm = ChatOpenAI(temperature=0)
prompt = PromptTemplate.from_template("Respond to the user input: {input}")
chain = LLMChain(llm=llm, prompt=prompt)

# Create FastAPI app and add LangServe route
app = FastAPI()
add_routes(app, chain, path="/chat")

# Start the app using: uvicorn main:app --reload
# and visit: http://localhost:8000/docs
