# === IMPORTS ===

from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from uuid import uuid4
from threading import Thread
from datetime import datetime
from dotenv import load_dotenv  
load_dotenv()                   
from log_manager import outputs, outputs_lock, Event, append_event
from crews import TechnologyResearchCrew
from log_manager import Output

# === INITIALIZE FLASK APP ===

app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS)
# This allows our frontend (e.g. React app on port 3000) to talk to this backend (port 3001)
CORS(app, resources={r"/api/*": {"origins": "*"}})


# === POST ENDPOINT: Launch Multi-Agent Crew ===

@app.route('/api/multiagent', methods=['POST'])
def run_multiagent():
    """
    Starts a new CrewAI job.
    Accepts a JSON payload with 'technologies' and 'businessareas'.
    Returns a unique input_id immediately.
    """
    data = request.json

    if not data or 'technologies' not in data or 'businessareas' not in data:
        abort(400, description="Invalid request with missing data.")

    input_id = str(uuid4())
    technologies = data['technologies']
    businessareas = data['businessareas']

    # ✅ Initialize output early to avoid 404 during polling
    with outputs_lock:
        outputs[input_id] = Output(
            status="STARTED",
            events=[Event(timestamp=datetime.now(), data="CREW STARTED")],
            result=""
        )

    # ✅ Start background crew processing
    thread = Thread(target=kickoff_crew, args=(input_id, technologies, businessareas))
    thread.start()

    return jsonify({"input_id": input_id}), 200




# === GET ENDPOINT: Fetch Status of Multi-Agent Crew ===

@app.route('/api/multiagent/<input_id>', methods=['GET'])
def get_status(input_id):
    """
    Returns the status, final result, and event log for a given input_id.
    """

    with outputs_lock:
        output = outputs.get(input_id)
        if output is None:
            abort(404, description="Output not found")

    try:
        import json
        result_json = json.loads(output.result)  # Try parsing output string as JSON
    except Exception:
        result_json = output.result  # If parsing fails, return raw string

    return jsonify({
        "input_id": input_id,
        "status": output.status,
        "result": result_json,
        "events": [
            {
                "timestamp": event.timestamp.isoformat(),
                "data": event.data
            } for event in output.events
        ]
    })


# === CREW STARTUP FUNCTION ===

def kickoff_crew(input_id, technologies: list[str], businessareas: list[str]):
    """
    Runs the multi-agent crew logic for the given input_id.
    Assumes output has already been initialized in the POST handler.
    """

    print(f"Running crew for {input_id} with technologies {technologies} and businessareas {businessareas}")
    results = None

    try:
        # Step 1: Set up the crew
        crew = TechnologyResearchCrew(input_id)
        crew.setup_crew(technologies, businessareas)

        # Step 2: Kickoff execution (sync or async)
        results = crew.kickoff()

    except Exception as e:
        # Handle failure — mark as ERROR
        print(f"CREW FAILED: {str(e)}")
        append_event(input_id, f"CREW FAILED: {str(e)}")
        with outputs_lock:
            outputs[input_id].status = 'ERROR'
            outputs[input_id].result = str(e)
        return

    # Step 3: Save successful result
    with outputs_lock:
        outputs[input_id].status = 'COMPLETE'
        outputs[input_id].result = results
        outputs[input_id].events.append(
            Event(timestamp=datetime.now(), data="Crew complete")
        )



# === MAIN ENTRY POINT ===

if __name__ == '__main__':
    # Run the backend server on port 3001
    app.run(debug=True, port=3001)

"""
🧠 BEGINNER NOTES — How the CrewAI Flask Backend Works

🔹 1. Flask App
We use Flask to create an HTTP API that allows a frontend (like React or Next.js) to send input and receive AI-generated output.

🔹 2. CORS
CORS is enabled so that the browser can fetch data across different ports (frontend on :3000, backend on :3001).

🔹 3. POST /api/multiagent
This endpoint accepts a JSON object with 'technologies' and 'businessareas'.
It starts a CrewAI agent run using `Thread()` so it doesn't block the main Flask thread.
It returns a unique input_id (UUID) to track this run.

🔹 4. GET /api/multiagent/<input_id>
This endpoint returns:
- The current status of the crew ("STARTED", "COMPLETE", or "ERROR")
- The final structured result
- A list of log events with timestamps

🔹 5. kickoff_crew()
This function is the actual multi-agent runner.
It:
- Instantiates the Crew (via TechnologyResearchCrew)
- Sets it up with the provided input
- Calls `.kickoff()` to run agents and tasks
- Logs output to a shared `outputs` dictionary (protected with `outputs_lock`)

🔹 6. Threading
CrewAI runs in the background thread to keep the API responsive.
This allows instant feedback (input_id) while the AI agents continue processing in the background.

🔹 7. Logs and Status
Event logs and final results are stored using a shared dictionary (`outputs`).
We lock this dictionary using `outputs_lock` to avoid race conditions during multi-threading.

"""
