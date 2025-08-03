// === MAIN PAGE ===
// Renders Input, Event Log, and Final Output components

"use client";

import InputSection from "../components/InputSection";
import EventLog from "../components/EventLog";
import FinalOutput from "../components/FinalOutput";
import useCrewOutput from "../hooks/useCrewOutput";

export default function HomePage() {
  const { inputId, status, result, events, isLoading, handleSubmit } =
    useCrewOutput();

  return (
    <div className="space-y-10">
      {/* Step 1: Input form to start the multi-agent process */}
      <InputSection
        onSubmit={handleSubmit}
        isLoading={isLoading}
        currentStatus={status}
      />

      {/* Step 2: Real-time log updates from the backend */}
      {inputId && <EventLog events={events} status={status} />}

      {/* Step 3: Final JSON output once complete */}
      {status === "COMPLETE" && result && <FinalOutput result={result} />}
    </div>
  );
}

/**
 * 🧠 FRONTEND NOTES — page.tsx (Main UI)
 *
 * 🔹 Purpose:
 * This is the main page that orchestrates:
 * - User input (via <InputSection />)
 * - Real-time log updates (via <EventLog />)
 * - Final output display (via <FinalOutput />)
 *
 * 🔹 State Management:
 * - All logic is centralized in the custom hook: `useCrewOutput()`
 * - That hook handles:
 *     - form state
 *     - API call (POST /api/multiagent)
 *     - polling for results
 *     - status/events/result
 *
 * 🔹 Conditional Rendering:
 * - `inputId`: if present, show live log
 * - `status === COMPLETE`: show result
 *
 * 🔹 Styling:
 * - `space-y-10`: Adds vertical spacing between sections
 * - Uses Tailwind to keep layout clean and consistent
 *
 * 🔹 Next Steps:
 * - Build `useCrewOutput.tsx` (logic)
 * - Build `InputSection`, `EventLog`, `FinalOutput` components
 */
