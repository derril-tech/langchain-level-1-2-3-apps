import React, { useState, useRef } from "react";
import axios from "axios";

type ChatItem = {
  question: string;
  answer: string;
  timestamp: string;
};

const App: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [question, setQuestion] = useState("");
  const [chatHistory, setChatHistory] = useState<ChatItem[]>([]);
  const [loading, setLoading] = useState(false);
  const fileInputRef = useRef<HTMLInputElement | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    try {
      await axios.post("http://localhost:8000/upload", formData);
      alert("✅ PDF uploaded and processed successfully.");
    } catch (err) {
      alert("❌ Upload failed. Check server logs.");
      console.error(err);
    }
  };

  const handleAsk = async () => {
    if (!question.trim()) return;
    setLoading(true);
    try {
      const response = await axios.post<{ answer: { content: string } }>(
        "http://localhost:8000/rag/invoke",
        { input: question } // ✅ Fix: wrap question as input
      );
      const answer = response.data.answer?.content || "No answer returned.";
      const timestamp = new Date().toLocaleString();
      setChatHistory([...chatHistory, { question, answer, timestamp }]);
      setQuestion("");
    } catch (err) {
      alert("❌ Failed to fetch answer.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-4xl mx-auto bg-white p-8 rounded-xl shadow-md">
        <h1 className="text-3xl font-bold mb-6 text-blue-700">
          📄 AI PDF Q&A Assistant
        </h1>

        {/* File upload */}
        <div className="mb-6">
          <input
            type="file"
            accept="application/pdf"
            onChange={handleFileChange}
            ref={fileInputRef}
            className="mb-3"
          />
          <button
            onClick={handleUpload}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Upload PDF
          </button>
        </div>

        {/* Question input */}
        <div className="mb-6">
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask a question about the PDF..."
            className="w-full border border-gray-300 rounded px-4 py-2"
          />
          <button
            onClick={handleAsk}
            disabled={loading}
            className="mt-3 bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
          >
            {loading ? "Thinking..." : "Ask"}
          </button>
        </div>

        {/* Chat history */}
        <div className="space-y-4">
          {chatHistory.map((item, index) => (
            <div
              key={index}
              className="bg-gray-100 p-4 rounded border border-gray-300"
            >
              <div className="text-xs text-gray-500 mb-1">
                🕒 {item.timestamp}
              </div>
              <p className="font-semibold text-blue-800">Q: {item.question}</p>
              <p className="mt-1 text-gray-700">A: {item.answer}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default App;
