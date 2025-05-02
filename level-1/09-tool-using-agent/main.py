
---

### 🧠 `main.py`

```python
# main.py

from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.utilities import SerpAPIWrapper
from langchain.tools import Tool as LangChainTool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define a simple math tool
def calculator_tool(input_text):
    try:
        return str(eval(input_text))
    except Exception as e:
        return f"Error: {e}"

# Wrap it as a LangChain Tool
tools = [
    LangChainTool(
        name="Calculator",
        func=calculator_tool,
        description="Useful for doing basic math operations, e.g. '3*4+2'"
    )
]

# Initialize LLM and agent
llm = ChatOpenAI(temperature=0)
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

print("🤖 Tool-Using Agent is running. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in {"exit", "quit"}:
        print("👋 Goodbye!")
        break

    result = agent.run(user_input)
    print(f"Agent: {result}\n")
