
---

### 🧠 `main.py`

```python
# main.py

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import pandas as pd
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Load example "database" (CSV or in-memory table)
data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Department": ["HR", "Engineering", "Marketing"]
})

# Convert table to plain text format
table_text = data.to_string(index=False)

# Example question
user_question = "Who is the oldest employee and what department do they work in?"

# Build prompt
template = """
You are given a table of employee data:

{table}

Answer the following question based on the table:
{question}
"""

prompt = PromptTemplate(
    input_variables=["table", "question"],
    template=template,
)

llm = ChatOpenAI(temperature=0)
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain
response = chain.run({"table": table_text, "question": user_question})

print("📊 Answer:\n")
print(response)
