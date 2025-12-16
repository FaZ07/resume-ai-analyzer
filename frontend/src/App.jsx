import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const analyzeResume = async () => {
    if (!file) return;

    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8001/analyze/", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("API request failed");
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError("Failed to analyze resume");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>Resume Analyzer</h1>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={analyzeResume} disabled={!file || loading}>
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>

      <br /><br />

      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
  <div style={{ marginTop: "30px" }}>
    <h2>Extracted Skills</h2>
    <div style={{ display: "flex", gap: "10px", flexWrap: "wrap" }}>
      {result.resume_skills.map((skill, idx) => (
        <span
          key={idx}
          style={{
            padding: "6px 12px",
            background: "#2d2d2d",
            borderRadius: "20px",
            fontSize: "14px"
          }}
        >
          {skill}
        </span>
      ))}
    </div>

    <h2 style={{ marginTop: "30px" }}>Top Job Matches</h2>

    {result.top_job_matches.map((job, idx) => (
      <div
        key={idx}
        style={{
          marginTop: "20px",
          padding: "20px",
          borderRadius: "10px",
          background: "#1f1f1f"
        }}
      >
        <h3>{job.job_role}</h3>

        <p><strong>Final Score:</strong> {job.final_score}%</p>

        <p>
          Skill Score: {job.score_breakdown.skill_score}% | Semantic Score:{" "}
          {job.score_breakdown.semantic_score}%
        </p>

        <p><strong>Matched Skills:</strong></p>
        <ul>
          {job.matched_skills.map((s, i) => (
            <li key={i}>{s}</li>
          ))}
        </ul>

        <p><strong>Missing Skills:</strong></p>
        <ul>
          {job.missing_skills.map((s, i) => (
            <li key={i} style={{ color: "#ff6b6b" }}>{s}</li>
          ))}
        </ul>
      </div>
    ))}
  </div>
)}

    </div>
  );
}

export default App;

