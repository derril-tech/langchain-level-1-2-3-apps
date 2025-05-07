# ================================================
# LangChain : Extracting Entities
# ================================================

# 1. Load environment variables (e.g., OpenAI API key)
import os
from dotenv import load_dotenv, find_dotenv

# Automatically find and load the .env file
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]  # Your OpenAI key

# 2. Import and configure the LLM (Language Model)
from langchain_openai import ChatOpenAI

# Initialize the LLM with a specific model
llm = ChatOpenAI(model="gpt-4o-2024-08-06")

"""
Define what information you want to extract
We'll use Pydantic to define an schema to extract personal information.
Pydantic is a Python library used for data validation. It helps ensure that the data your program receives matches the format you expect, and it provides helpful error messages when the data doesn't conform to your specifications. Essentially, Pydantic allows you to enforce that the data structures in Python adhere to specific types and constraints, making your code more robust and error-resistant.
Document the attributes and the schema itself: This information is sent to the LLM and is used to improve the quality of information extraction.
Do not force the LLM to make up information! We import Optional for the attributes allowing the LLM to output None if it doesn't know the answer.
When you use Optional in type hints, you are indicating that a variable can either be of a specified type or it can be None.

"""

# 3. Define data models using Pydantic for structure and validation
from typing import Optional, List
from pydantic import BaseModel, Field  # ✅ Use pydantic directly for v2


class Person(BaseModel):
    """Information about a person."""
    # This docstring is used as a description of the schema by the LLM

    name: Optional[str] = Field(default=None, description="The name of the person")
    lastname: Optional[str] = Field(default=None, description="The lastname of the person if known")
    country: Optional[str] = Field(default=None, description="The country of the person if known")

class Data(BaseModel):
    """Extracted data about people."""
    people: List[Person]  # List allows extracting multiple people in one pass

# 4. Create a prompt template that tells the LLM what to do
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert extraction algorithm. "
            "Only extract relevant information from the text. "
            "If you do not know the value of an attribute asked to extract, "
            "return null for the attribute's value.",
        ),
        ("human", "{text}"),  # Placeholder for actual input text
    ]
)

# 5. Create the full processing chain: prompt + model + output schema
chain = prompt | llm.with_structured_output(schema=Data)

# 6. Try it on a single review mentioning one person
comment = "I'm so impressed with this product! It has truly transformed how I approach my daily tasks. The quality exceeds my expectations, and the customer support is truly exceptional. I've already suggested it to all my colleagues and relatives. - Emily Clarke, Canada"

response = chain.invoke({"text": comment})
print("\n----------\n")
print("Key data extraction of a single user:")
print("\n----------\n")
print(response)
print("\n----------\n")

# 7. Try it on a review that mentions multiple people
text_input = """
Alice Johnson from Canada recently reviewed a book she loved.
Meanwhile, Bob Smith from the USA shared his insights on the same book in a different review.
Both reviews were very insightful.
"""

response = chain.invoke({"text": text_input})
print("\n----------\n")
print("Key data extraction of a review with several users:")
print("\n----------\n")
print(response)
print("\n----------\n")

# ===========================
# Notes / Quick Guide
# ===========================

"""
# LangChain Beginner Notes

1. **Environment Setup**
   - We use the `dotenv` library to securely load our OpenAI API key from a `.env` file.
   - This keeps sensitive data like API keys out of your source code.

2. **LLM Configuration**
   - We load OpenAI’s `gpt-4o-2024-08-06` model using the LangChain `ChatOpenAI` wrapper.

3. **Schema Definition**
   - We use Pydantic models (`BaseModel`) to define what data we want to extract.
   - Fields are marked as `Optional` so the LLM can skip them if not found.

4. **Prompt Engineering**
   - The system prompt gives clear instructions to the LLM on how to extract data.
   - A human placeholder `{text}` is used so we can insert different user inputs.

5. **The Chain**
   - We combine the prompt with the LLM and define the expected output using `with_structured_output`.
   - This chain allows us to pass in raw text and receive structured data (like names and countries).

6. **Testing**
   - We test the chain using one comment and one multi-person review to see how well it extracts info.

7. **Printing Results**
   - Extracted results are printed for clarity. Each block is separated to make outputs easy to read.

This script is perfect if you're starting out with LangChain and want to learn how to do basic information extraction using OpenAI models.
"""
