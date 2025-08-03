# === IMPORTS ===

from crewai import Crew
from agents import ResearchAgents
from tasks import ResearchTasks
from log_manager import append_event


# === CREW WRAPPER CLASS ===

class TechnologyResearchCrew:
    """
    Orchestrates agents and tasks into a working CrewAI pipeline.
    Responsible for setup, execution, and logging events for each input run.
    """

    def __init__(self, input_id: str):
        self.input_id = input_id
        self.crew = None
        self.agents = ResearchAgents()  # Pull in both manager and researcher

    def setup_crew(self, technologies: list[str], businessareas: list[str]):
        """
        Prepares the agents, assigns tasks, and builds the Crew instance.
        """

        print(f"Setting up crew for {self.input_id} with technologies {technologies} and businessareas {businessareas}")

        # === Step 1: Initialize agents ===
        research_manager = self.agents.research_manager(technologies, businessareas)
        research_agent = self.agents.research_agent()

        # === Step 2: Initialize tasks ===
        tasks = ResearchTasks(input_id=self.input_id)

        # One research task per technology (executed in parallel)
        technology_research_tasks = [
            tasks.technology_research(research_agent, technology, businessareas)
            for technology in technologies
        ]

        # One manager task to consolidate and validate all research
        manage_research_task = tasks.manage_research(
            research_manager,
            technologies,
            businessareas,
            technology_research_tasks
        )

        # === Step 3: Create crew ===
        self.crew = Crew(
            agents=[research_manager, research_agent],
            tasks=[*technology_research_tasks, manage_research_task],
            verbose=2
        )

    def kickoff(self):
        """
        Runs the full CrewAI process and returns the final output.
        Logs major milestones for frontend tracking.
        """

        if not self.crew:
            print(f"Crew not found for {self.input_id}")
            return

        append_event(self.input_id, "CREW STARTED")

        try:
            print(f"Running crew for {self.input_id}")
            results = self.crew.kickoff()
            append_event(self.input_id, "CREW COMPLETED")
            return results

        except Exception as e:
            append_event(self.input_id, "CREW FAILED")
            return str(e)
        
"""
🧠 BEGINNER NOTES — How crews.py Works (CrewAI Orchestration)

🔹 1. Purpose
This file ties everything together:
- It connects agents and tasks
- Builds the multi-agent crew
- Runs the execution and logs the result

🔹 2. TechnologyResearchCrew Class
This class handles all orchestration for one user request.
It is initialized with an `input_id`, which helps track logs and results uniquely.

🔹 3. setup_crew()
1. Creates the Research Manager and Agent
2. Assigns a task to each agent
   - One research task per technology
   - One manager task to consolidate all outputs
3. Creates a `Crew` object with agents + tasks

🔹 4. kickoff()
This method:
- Starts the Crew run
- Logs the status at key checkpoints:
    • CREW STARTED
    • CREW COMPLETED
    • CREW FAILED (on exception)
- Returns the final result back to `api.py`

🔹 5. Logging
We use `append_event()` to log key milestones so the frontend
can display a real-time event log to the user.

🔹 6. Task Execution Mode
Although the crew runs sequentially by default, each `technology_research` task
is marked `async_execution=True`, allowing those tasks to run in parallel.

"""
