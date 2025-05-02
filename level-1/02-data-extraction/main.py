# main.py

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

# Load environment variables (for OPENAI_API_KEY)
load_dotenv()

llm = ChatOpenAI(temperature=0)

# Example unstructured input
input_text = """
Hi, my name is Jane Doe. You can reach me at jane.doe@example.com.
I’m currently located in Stockholm and work for OpenAI Research Group.
"""

# Prompt template for extracting structured data
template = """
Extract the following fields from the given text:
- Full Name
- Email Address
- Location
- Company Name

Text: {text}

Return your response as a JSON object.
"""

prompt = PromptTemplate(
    input_variables=["text"],
    template=template,
)

chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain with the input text
response = chain.run(input_text)

print("🧾 Extracted Data:\n")
print(response)
