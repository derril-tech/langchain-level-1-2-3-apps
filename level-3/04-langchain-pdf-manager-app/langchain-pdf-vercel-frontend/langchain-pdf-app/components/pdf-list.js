import styles from "../styles/pdf-list.module.css";
import { useState, useEffect, useCallback, useRef } from "react";
import { debounce } from "lodash";
import PDFComponent from "./pdf";

export default function PdfList() {
  const [pdfs, setPdfs] = useState([]);
  const [selectedFile, setSelectedFile] = useState(null);
  const [filter, setFilter] = useState();
  const [selectedPdfId, setSelectedPdfId] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const didFetchRef = useRef(false);

  useEffect(() => {
    if (!didFetchRef.current) {
      didFetchRef.current = true;
      fetchPdfs();
    }
  }, []);

  async function fetchPdfs(selected) {
    let path = "/pdfs";
    if (selected !== undefined) {
      path = `/pdfs?selected=${selected}`;
    }
    const res = await fetch(process.env.NEXT_PUBLIC_API_URL + path);
    const json = await res.json();
    setPdfs(json);
  }

  const debouncedUpdatePdf = useCallback(
    debounce((pdf, fieldChanged) => {
      updatePdf(pdf, fieldChanged);
    }, 500),
    []
  );

  function handlePdfChange(e, id) {
    const target = e.target;
    const value = target.type === "checkbox" ? target.checked : target.value;
    const name = target.name;
    const copy = [...pdfs];
    const idx = pdfs.findIndex((pdf) => pdf.id === id);
    const changedPdf = { ...pdfs[idx], [name]: value };
    copy[idx] = changedPdf;
    debouncedUpdatePdf(changedPdf, name);
    setPdfs(copy);
  }

  async function updatePdf(pdf, fieldChanged) {
    const body_data = JSON.stringify(pdf);
    const url = process.env.NEXT_PUBLIC_API_URL + `/pdfs/${pdf.id}`;
    await fetch(url, {
      method: "PUT",
      body: body_data,
      headers: { "Content-Type": "application/json" },
    });
  }

  async function handleDeletePdf(id) {
    const res = await fetch(process.env.NEXT_PUBLIC_API_URL + `/pdfs/${id}`, {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
    });

    if (res.ok) {
      const copy = pdfs.filter((pdf) => pdf.id !== id);
      setPdfs(copy);
    }
  }

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = async (event) => {
    event.preventDefault();
    if (!selectedFile) {
      alert("Please select file to load.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);
    formData.append("file_name", selectedFile.name);

    const response = await fetch(
      process.env.NEXT_PUBLIC_API_URL + "/pdfs/upload",
      {
        method: "POST",
        body: formData,
      }
    );

    if (response.ok) {
      const newPdf = await response.json();
      setPdfs([...pdfs, newPdf]);
    } else {
      const errorText = await response.text();
      console.error("Upload failed with status:", response.status);
      console.error("Response:", errorText);
      alert("Error loading file.");
    }
  };

  const handleFilterChange = (value) => {
    setFilter(value);
    fetchPdfs(value);
  };

  const handleSubmitQuestion = async () => {
    const selectedPdf = pdfs.find((pdf) => pdf.selected);
    if (!selectedPdf || !question.trim()) {
      alert("Please select a PDF (checkbox) and enter a question.");
      return;
    }

    const selectedPdfId = selectedPdf.id;

    // ✅ Debug logs
    console.log("Selected PDF ID:", selectedPdfId);
    console.log("Question:", question);

    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/pdfs/qa-pdf/${selectedPdfId}`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question }),
      }
    );

    if (response.ok) {
      const result = await response.json();
      setAnswer(result.answer || result.summary || "No response received.");
    } else {
      const errorText = await response.text();
      setAnswer("Error: " + errorText);
    }
  };

  return (
    <div className={styles.container}>
      {/* Upload Section */}
      <div className={styles.mainInputContainer}>
        <form onSubmit={handleUpload} encType="multipart/form-data">
          <input
            className={styles.mainInput}
            type="file"
            accept=".pdf"
            onChange={handleFileChange}
          />
          <button className={styles.loadBtn} type="submit">
            Load PDF
          </button>
        </form>
      </div>

      {/* PDF List Section */}
      {!pdfs.length && <div>Loading...</div>}
      {pdfs.map((pdf) => (
        <div key={pdf.id}>
          <PDFComponent
            pdf={pdf}
            onDelete={handleDeletePdf}
            onChange={handlePdfChange}
          />
        </div>
      ))}

      {/* Q&A Section */}
      <div style={{ marginTop: "30px" }}>
        <div className={styles.questionSection}>
          <input
            className={styles.questionInput}
            type="text"
            placeholder="Ask a question about the selected PDF..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
          <button className={styles.askBtn} onClick={handleSubmitQuestion}>
            Ask Question
          </button>
          {answer && (
            <div className={styles.answerBox}>
              <strong>Answer:</strong> {answer}
            </div>
          )}
        </div>
      </div>

      {/* Filter Buttons */}
      <div className={styles.filters}>
        <button
          className={`${styles.filterBtn} ${
            filter === undefined ? styles.filterActive : ""
          }`}
          onClick={() => handleFilterChange()}
        >
          See All
        </button>
        <button
          className={`${styles.filterBtn} ${
            filter === true ? styles.filterActive : ""
          }`}
          onClick={() => handleFilterChange(true)}
        >
          See Selected
        </button>
        <button
          className={`${styles.filterBtn} ${
            filter === false ? styles.filterActive : ""
          }`}
          onClick={() => handleFilterChange(false)}
        >
          See Not Selected
        </button>
      </div>
    </div>
  );
}
