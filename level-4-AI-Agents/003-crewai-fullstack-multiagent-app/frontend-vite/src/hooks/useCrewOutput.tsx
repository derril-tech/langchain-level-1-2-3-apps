// === useCrewOutput Hook ===
// Handles API call + polling logic for CrewAI backend

import { useState, useEffect, useCallback } from "react";
import toast from "react-hot-toast";

interface CrewResult {
  [businessArea: string]: {
    blog_articles: { title: string; url: string }[];
    youtube_videos: { title: string; url: string }[];
  };
}

interface CrewEvent {
  timestamp: string;
  data: string;
}

// === Normalize raw backend result into typed CrewResult format ===

interface RawResult {
  businessareas: {
    businessarea: string;
    blog_articles_urls: string[];
    youtube_videos_urls: { name: string; url: string }[];
  }[];
}

const normalizeOutput = (rawResult: RawResult): CrewResult => {
  const result: CrewResult = {};

  if (Array.isArray(rawResult?.businessareas)) {
    for (const entry of rawResult.businessareas) {
      const area = entry.businessarea || "Unknown";

      result[area] = {
        blog_articles: (entry.blog_articles_urls || []).map((url) => ({
          title: decodeURIComponent(
            url.split("/").slice(-1)[0].replace(/[-_]/g, " ")
          ),
          url,
        })),
        youtube_videos: (entry.youtube_videos_urls || []).map((vid) => ({
          title: vid.name || "Untitled Video",
          url: vid.url,
        })),
      };
    }
  }

  return result;
};

export default function useCrewOutput() {
  const [inputId, setInputId] = useState<string | null>(null);
  const [status, setStatus] = useState<"PENDING" | "COMPLETE" | "ERROR" | null>(
    null
  );
  const [events, setEvents] = useState<CrewEvent[]>([]);
  const [result, setResult] = useState<CrewResult | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  // Submit form: call POST /api/multiagent
  const handleSubmit = useCallback(
    async (technologies: string[], businessareas: string[]) => {
      setIsLoading(true);
      setInputId(null);
      setStatus(null);
      setEvents([]);
      setResult(null);

      try {
        const res = await fetch("http://localhost:3001/api/multiagent", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ technologies, businessareas }),
        });

        if (!res.ok) throw new Error("Backend error");

        const data = await res.json();
        setInputId(data.input_id);
        toast.success("Crew launched successfully!");
      } catch (err) {
        console.error("POST error:", err);
        toast.error("Failed to launch Crew.");
        setIsLoading(false);
      }
    },
    []
  );

  // Polling: GET /api/multiagent/:input_id
  useEffect(() => {
    if (!inputId) return;

    const interval = setInterval(async () => {
      try {
        const res = await fetch(
          `http://localhost:3001/api/multiagent/${inputId}`
        );
        if (!res.ok) throw new Error("Polling failed");

        const data = await res.json();
        setStatus(data.status);
        setEvents(data.events);
        setResult(normalizeOutput(data.result)); // ✅ normalize backend result

        if (data.status === "COMPLETE" || data.status === "ERROR") {
          clearInterval(interval);
          setIsLoading(false);
        }
      } catch (err) {
        console.error("Polling error:", err);
        toast.error("Error fetching status.");
        clearInterval(interval);
        setIsLoading(false);
      }
    }, 2000);

    return () => clearInterval(interval);
  }, [inputId]);

  return {
    inputId,
    status,
    events,
    result,
    isLoading,
    handleSubmit,
  };
}

/**
 * 🧠 FRONTEND NOTES — useCrewOutput Hook
 *
 * 🔹 Purpose:
 * - This is the main logic hook for the frontend.
 * - It connects to the backend to:
 *     - Start the CrewAI process (POST)
 *     - Poll for results every 2 seconds (GET)
 *     - Track live status, events, and results
 *
 * 🔹 Key Concepts:
 * - `inputId`: UUID from the backend, used to poll
 * - `status`: "PENDING", "COMPLETE", or "ERROR"
 * - `events`: Real-time event log (CREW STARTED, etc.)
 * - `result`: Final JSON returned by Research Manager
 *
 * 🔹 handleSubmit():
 * - Called when the user clicks submit
 * - Sends POST request to launch the job
 * - Saves inputId so polling can begin
 *
 * 🔹 Polling useEffect():
 * - When `inputId` is set, starts polling every 2s
 * - Calls GET /api/multiagent/:inputId
 * - Updates events, result, and status
 *
 * 🔹 normalizeOutput():
 * - Maps backend's flexible structure into the frontend's fixed shape
 * - Handles missing keys, malformed data, or unexpected formats safely
 *
 * 🔹 Dependencies:
 * - Requires `react-hot-toast` for feedback
 *     npm install react-hot-toast
 */
