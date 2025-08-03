# === IMPORTS ===

from crewai import Task, Agent
from textwrap import dedent
from log_manager import append_event
from models import BusinessareaInfo, BusinessareaInfoList


# === TASK FACTORY CLASS ===

class ResearchTasks:
    """
    Defines all the tasks assigned to agents.
    Provides one task for the Research Agent and one for the Research Manager.
    Each task includes callbacks for logging and optional output schemas.
    """

    def __init__(self, input_id: str):
        self.input_id = input_id

    def append_event_callback(self, task_output):
        """
        Callback to log when a task finishes.
        """
        print(f"Appending event for {self.input_id} with output {task_output}")
        append_event(self.input_id, task_output.exported_output)

    def technology_research(self, agent: Agent, technology: str, businessareas: list[str]) -> Task:
        """
        Task for the Research Agent to look up content for a specific technology
        across multiple business areas.
        """

        return Task(
            description=dedent(f"""\
                Research the business areas {businessareas} for the {technology} technology.
                For each business area, find:
                - URLs for 3 recent blog articles
                - Titles and URLs for 3 recent YouTube videos

                Return this collected information in a JSON object.

                🔎 Tips:
                - Google Search: "{technology} [BUSINESS AREA] blog articles"
                - YouTube: "{technology} in [BUSINESS AREA]"

                ⚠️ Important:
                - Do NOT generate fake results.
                - Return only real information, and nothing else.
                - Return exactly 3 blog articles and 3 videos per business area.
            """),
            agent=agent,
            expected_output="A JSON object containing the researched information for each business area in the technology.",
            callback=self.append_event_callback,
            output_json=BusinessareaInfo,
            async_execution=True
        )

    def manage_research(self, agent: Agent, technologies: list[str], businessareas: list[str], tasks: list[Task]) -> Task:
        """
        Task for the Research Manager to aggregate and validate all research.
        Runs after the research_agent tasks are done.
        """

        return Task(
            description=dedent(f"""\
                Based on the list of technologies {technologies} and business areas {businessareas},
                use the results from the Research Agent to compile a final JSON object.

                Include:
                - 3 blog URLs
                - 3 YouTube videos (title + URL)
                For each technology + business area pair.
            """),
            agent=agent,
            expected_output=dedent("""\
                A JSON object containing the URLs for 3 blog articles and 3 YouTube videos
                for each business area in each technology.
            """),
            callback=self.append_event_callback,
            context=tasks,  # Uses the research_agent tasks as context
            output_json=BusinessareaInfoList
        )

"""
🧠 BEGINNER NOTES — How tasks.py Works (CrewAI Agent Tasks)

🔹 1. Purpose
This file defines what each agent is responsible for:
- The Research Agent searches for blogs and videos (per technology).
- The Manager Agent collects and formats everything into the final result.

🔹 2. What is a Task?
In CrewAI:
- A Task = instructions + assigned agent + expected output + optional tools
- You can also attach a callback for logging or validation.

🔹 3. Class: ResearchTasks
This class defines both tasks and ties them to an `input_id` so logs can be stored properly.

🔹 4. Task 1: technology_research()
This task is assigned to the Research Agent.
It:
- Runs once per technology
- Is async-enabled so multiple technologies can run in parallel
- Returns a structured object (BusinessareaInfo)
- Logs output via a callback

🔹 5. Task 2: manage_research()
This task is assigned to the Manager.
It:
- Aggregates the research results
- Expects the full JSON output using the BusinessareaInfoList model
- Uses the research tasks as `context` so it can reference prior work

🔹 6. dedent()
We use `textwrap.dedent()` to keep the task instructions readable in code
but nicely formatted when passed into the LLM (no extra indentation).

🔹 7. async_execution=True
Means the task can be run in parallel — but only works with OpenAI models like GPT-4.

🔹 8. Callback
After each task finishes, `append_event_callback()` logs the output to the backend
so the frontend event log can update.

"""
