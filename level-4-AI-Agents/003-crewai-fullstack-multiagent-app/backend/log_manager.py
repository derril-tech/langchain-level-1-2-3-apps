# === IMPORTS ===

from dataclasses import dataclass
from datetime import datetime
from threading import Lock
from typing import List, Dict


# === DATA MODELS ===

@dataclass
class Event:
    """Stores a single log entry with timestamp and message."""
    timestamp: datetime
    data: str


@dataclass
class Output:
    """Stores the full output for an input_id including status, events, and final result."""
    status: str                     # e.g., "STARTED", "COMPLETE", "ERROR"
    events: List[Event]             # Log of all significant steps/events
    result: str                     # Final result (JSON string or raw string)


# === SHARED STATE ===

# Lock to ensure only one thread modifies the outputs at a time
outputs_lock = Lock()

# Global dictionary of outputs indexed by input_id (UUID string)
outputs: Dict[str, Output] = {}


# === APPEND FUNCTION ===

def append_event(input_id: str, event_data: str):
    """
    Thread-safe function to add an event to the log of a given input_id.
    Creates the Output object if it's the first time this ID is seen.
    """

    with outputs_lock:
        # First-time event → create output entry
        if input_id not in outputs:
            print(f"Start output {input_id}")
            outputs[input_id] = Output(
                status='STARTED',
                events=[],
                result=''
            )
        else:
            print(f"Appending event for {input_id}")

        # Add new event to the log
        outputs[input_id].events.append(
            Event(timestamp=datetime.now(), data=event_data)
        )


"""
🧠 BEGINNER NOTES — How log_manager.py Works (CrewAI Backend)

🔹 1. Purpose
This file handles **event logging and output tracking** for each agent run.
It ensures **thread-safe storage and updates** during concurrent execution.

🔹 2. Event & Output Models
- `Event`: A log entry with a timestamp and message.
- `Output`: Stores:
  • current status (STARTED / COMPLETE / ERROR)
  • all log events (list of Event objects)
  • final result (as string or JSON)

🔹 3. outputs_lock
We use Python's `Lock()` to **prevent race conditions** when multiple threads write to `outputs`.

🔹 4. outputs (Global Store)
This is a shared dictionary that holds all crew outputs, indexed by `input_id` (UUID string).
Every crew run gets its own entry.

🔹 5. append_event()
- Called whenever we want to add a log entry for a given crew job.
- If it's the first event for a job, it initializes the entry.
- It appends the new event (with current timestamp) to the job's log.

🔹 6. Why Thread Safety?
Because Flask spins up multiple threads (especially when using `Thread()` to run crews),
we need to **lock** shared resources like dictionaries to avoid data corruption or collisions.

"""
