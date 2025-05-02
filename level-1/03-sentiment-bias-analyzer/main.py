
---

### 🧠 `main.py`

```python
# main.py

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

# Load OpenAI key
load_dotenv()

# Set up the model
llm = ChatOpenAI(temperature=0)

# Example input text
input_text = """
The government’s reckless spending has driven us into a financial disaster.
Only radical reform can save the economy now.
"""

# Prompt for sentiment and bias classification
template = """
Analyze the following text and classify:
1. Sentiment: Positive, Neutral, or Negative
2. Political Bias: Left, Center, or Right

Text: {text}

Respond in this format:
Sentiment: <Positive/Neutral/Negative>
Political Bias: <Left/Center/Right>
"""

prompt = PromptTemplate(
    input_variables=["text"],
    template=template,
)

chain = LLMChain(llm=llm, prompt=prompt)

# Run the model
result = chain.run(text=input_text)

print("📊 Analysis Result:\n")
print(result)
