import { useState, useRef, useEffect } from "react";

// ==========================================
// API Layer
// ==========================================
const API_BASE = "http://localhost:8000";

async function analyzeResume(file, targetRole) {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("target_role", targetRole);

  const response = await fetch(`${API_BASE}/analyze`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.detail || `Server Error: ${response.status}`);
  }
  return response.json();
}

async function fetchRoles() {
  const response = await fetch(`${API_BASE}/roles`);
  if (!response.ok) throw new Error("Failed to fetch roles");
  return response.json();
}

// ==========================================
// Components
// ==========================================
function UploadScreen({ onAnalyze, error }) {
  const [file, setFile] = useState(null);
  const [role, setRole] = useState("machine learning engineer");
  const [availableRoles, setAvailableRoles] = useState([]);
  const [dragging, setDragging] = useState(false);
  const fileRef = useRef();

  useEffect(() => {
    fetchRoles().then(data => setAvailableRoles(data.roles)).catch(console.error);
  }, []);

  const handleFile = (f) => {
    if (f && f.type === "application/pdf") setFile(f);
    else alert("Please upload a PDF file.");
  };

  const handleDrop = (e) => {
    e.preventDefault(); 
    setDragging(false);
    handleFile(e.dataTransfer.files[0]);
  };

  // Only requires a file and a role to proceed now
  const canSubmit = file && role;

  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", padding: "4rem 1rem" }}>
      
      <div style={{ textAlign: "center", marginBottom: "2.5rem", maxWidth: "600px" }}>
        <div style={{ display: "inline-flex", alignItems: "center", padding: "6px 14px", background: "#e0e7ff", color: "#4338ca", borderRadius: "9999px", fontSize: "12px", fontWeight: "700", textTransform: "uppercase", marginBottom: "1.5rem" }}>
          ✨ AI-Powered Career Intelligence
        </div>
        <div style={{ width: "72px", height: "72px", borderRadius: "50%", background: "linear-gradient(135deg, #6366f1, #8b5cf6)", display: "flex", alignItems: "center", justifyContent: "center", margin: "0 auto 1.5rem", boxShadow: "0 10px 25px -5px rgba(99, 102, 241, 0.5)", color: "white" }}>
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
        </div>
        <h1 style={{ fontSize: "38px", fontWeight: "800", color: "#111827", margin: "0 0 1rem", lineHeight: "1.2" }}>
          Career<span style={{ color: "#6366f1" }}>Lens</span> AI
        </h1>
        <p style={{ fontSize: "16px", color: "#6b7280", maxWidth: "420px", margin: "0 auto", lineHeight: "1.6" }}>
          Upload your resume, discover your objective fit score, and get a personalized learning roadmap.
        </p>
      </div>

      <div style={{ width: "100%", maxWidth: "560px", background: "#ffffff", borderRadius: "24px", boxShadow: "0 20px 40px -10px rgba(0,0,0,0.08)", border: "1px solid #f3f4f6", padding: "40px", boxSizing: "border-box" }}>
        {error && (
          <div style={{ background: "#fef2f2", border: "1px solid #fecaca", borderRadius: "12px", padding: "16px", marginBottom: "24px", color: "#dc2626", fontSize: "14px", display: "flex", alignItems: "center", gap: "8px" }}>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
            {error}
          </div>
        )}

        <div style={{ display: "flex", flexDirection: "column", gap: "24px" }}>

          <div>
            <label style={{ fontSize: "14px", fontWeight: "600", color: "#374151", display: "block", marginBottom: "8px" }}>Target Role</label>
            <select value={role} onChange={e => setRole(e.target.value)} style={{ width: "100%", height: "56px", padding: "0 16px", borderRadius: "14px", border: "1px solid #d1d5db", background: "#ffffff", fontSize: "15px", color: "#1f2937", cursor: "pointer", outline: "none" }}>
              {availableRoles.length > 0 ? availableRoles.map(r => (
                <option key={r} value={r}>{r.split(" ").map(w => w[0].toUpperCase() + w.slice(1)).join(" ")}</option>
              )) : <option value="machine learning engineer">Machine Learning Engineer</option>}
            </select>
          </div>

          <div>
            <label style={{ fontSize: "14px", fontWeight: "600", color: "#374151", display: "block", marginBottom: "8px" }}>Resume Document</label>
            <div onDragOver={e => { e.preventDefault(); setDragging(true); }} onDragLeave={() => setDragging(false)} onDrop={handleDrop} onClick={() => fileRef.current.click()} style={{ height: "220px", border: `2px dashed ${file ? "#86efac" : (dragging ? "#6366f1" : "#d1d5db")}`, borderRadius: "16px", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", textAlign: "center", cursor: "pointer", background: file ? "#f0fdf4" : (dragging ? "#eef2ff" : "#fafafa") }}>
              <input ref={fileRef} type="file" accept=".pdf" style={{ display: "none" }} onChange={e => handleFile(e.target.files[0])} />
              {file ? (
                <>
                  <div style={{ color: "#22c55e", marginBottom: "16px", background: "#dcfce7", padding: "16px", borderRadius: "50%" }}><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></div>
                  <p style={{ fontWeight: "700", margin: "0 0 4px", fontSize: "16px", color: "#166534" }}>{file.name}</p>
                </>
              ) : (
                <>
                  <div style={{ color: dragging ? "#6366f1" : "#9ca3af", marginBottom: "16px" }}><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg></div>
                  <p style={{ fontWeight: "600", margin: "0 0 8px", fontSize: "16px", color: dragging ? "#4f46e5" : "#374151" }}>Click or drag to upload</p>
                </>
              )}
            </div>
          </div>

          <button disabled={!canSubmit} onClick={() => onAnalyze(file, role)} style={{ width: "100%", height: "56px", marginTop: "8px", borderRadius: "14px", fontSize: "16px", fontWeight: "700", cursor: canSubmit ? "pointer" : "not-allowed", background: canSubmit ? "linear-gradient(135deg, #6366f1, #8b5cf6)" : "#f3f4f6", color: canSubmit ? "#ffffff" : "#9ca3af", border: "none" }}>
            {canSubmit ? "Analyze Resume →" : "Add PDF to continue"}
          </button>
        </div>
      </div>
    </div>
  );
}

function AnalysisScreen({ result, onViewRoadmap, onReset }) {
  const [tab, setTab] = useState("matched");
  const { fit_score, role, matched_skills, missing_skills, resume_data, recommendation } = result;
  const scoreColor = fit_score >= 80 ? "#22c55e" : fit_score >= 60 ? "#3b82f6" : fit_score >= 40 ? "#f59e0b" : "#ef4444";

  return (
    <div style={{ maxWidth: 700, margin: "0 auto", padding: "2rem 1rem" }}>
      <div style={{ background: "#fff", borderRadius: 24, border: "1px solid #f3f4f6", padding: "32px", marginBottom: 24, display: "flex", gap: 32, alignItems: "center", boxShadow: "0 10px 25px -5px rgba(0,0,0,0.05)" }}>
        <div style={{ fontSize: 64, color: scoreColor, fontWeight: "800", lineHeight: 1 }}>{fit_score}%</div>
        <div>
          <p style={{ fontSize: 13, textTransform: "uppercase", color: "#6b7280", margin: "0 0 6px", fontWeight: 600 }}>Fit Score</p>
          <h2 style={{ margin: "0 0 8px", fontSize: 24, fontWeight: 800, textTransform: "capitalize", color: "#111827" }}>{role}</h2>
          <p style={{ margin: "0 0 16px", fontSize: 14, color: "#4b5563", fontWeight: 500 }}>{resume_data.name} · {resume_data.experience_years}y exp</p>
          <p style={{ margin: 0, fontSize: 15, color: "#4b5563", lineHeight: 1.6 }}>{recommendation}</p>
        </div>
      </div>

      <div style={{ background: "#fff", borderRadius: 24, border: "1px solid #f3f4f6", padding: "24px 32px", marginBottom: 24 }}>
        <div style={{ display: "flex", gap: 8, marginBottom: 20 }}>
          <button onClick={() => setTab("matched")} style={{ padding: "8px 16px", fontWeight: tab === "matched" ? "700" : "500", background: tab === "matched" ? "#f3f4f6" : "transparent", color: tab === "matched" ? "#111827" : "#6b7280", border: "none", borderRadius: 10, cursor: "pointer", fontSize: 14 }}>✓ Matched ({matched_skills.length})</button>
          <button onClick={() => setTab("missing")} style={{ padding: "8px 16px", fontWeight: tab === "missing" ? "700" : "500", background: tab === "missing" ? "#f3f4f6" : "transparent", color: tab === "missing" ? "#111827" : "#6b7280", border: "none", borderRadius: 10, cursor: "pointer", fontSize: 14 }}>✗ Missing ({missing_skills.length})</button>
        </div>
        <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
          {(tab === "matched" ? matched_skills : missing_skills).map(skill => (
            <span key={skill} style={{ padding: "6px 14px", borderRadius: 20, fontSize: 13, fontWeight: 600, background: tab === "matched" ? "#dcfce7" : "#fee2e2", color: tab === "matched" ? "#16a34a" : "#dc2626" }}>{skill}</span>
          ))}
        </div>
      </div>

      <div style={{ display: "flex", gap: 12 }}>
        <button onClick={onViewRoadmap} style={{ flex: 1, padding: "16px", borderRadius: 16, background: "linear-gradient(135deg, #6366f1, #8b5cf6)", color: "#fff", border: "none", cursor: "pointer", fontWeight: "700", fontSize: 15 }}>View Learning Roadmap →</button>
        <button onClick={onReset} style={{ padding: "16px 24px", borderRadius: 16, background: "#ffffff", border: "1px solid #d1d5db", cursor: "pointer", fontWeight: "600", fontSize: 15, color: "#374151" }}>New Analysis</button>
      </div>
    </div>
  );
}

function RoadmapScreen({ result, onBack }) {
  const { roadmap, role } = result;
  const grouped = { high: roadmap.filter(i => i.priority === "high"), medium: roadmap.filter(i => i.priority === "medium"), low: roadmap.filter(i => i.priority === "low") };

  return (
    <div style={{ maxWidth: 700, margin: "0 auto", padding: "2rem 1rem" }}>
      <button onClick={onBack} style={{ marginBottom: 24, padding: "8px 16px", borderRadius: 10, border: "1px solid #d1d5db", cursor: "pointer", background: "#fff", fontWeight: 600, color: "#374151", fontSize: 14 }}>← Back to Results</button>
      <h2 style={{ textTransform: "capitalize", marginBottom: 32, fontSize: 28, fontWeight: 800, color: "#111827" }}>Roadmap: {role}</h2>

      {roadmap.length === 0 ? (
        <div style={{ background: "#fff", padding: 40, borderRadius: 24, textAlign: "center", border: "1px solid #f3f4f6" }}>
          <div style={{ fontSize: 48, marginBottom: 16 }}>🏆</div>
          <h3 style={{ margin: "0 0 8px", fontSize: 20 }}>You have all required skills!</h3>
        </div>
      ) : (
        ["high", "medium", "low"].map(priority => {
          if (!grouped[priority].length) return null;
          const colors = { high: "#dc2626", medium: "#f59e0b", low: "#10b981" };
          return (
            <div key={priority} style={{ marginBottom: 32 }}>
              <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 16 }}>
                <div style={{ width: 8, height: 8, borderRadius: "50%", background: colors[priority] }} />
                <h3 style={{ textTransform: "capitalize", fontSize: 16, color: "#374151", margin: 0, fontWeight: 700 }}>{priority} Priority</h3>
              </div>
              <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
                {grouped[priority].map(item => (
                  <div key={item.skill} style={{ background: "#fff", borderRadius: 20, border: "1px solid #f3f4f6", padding: "24px" }}>
                    <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 16 }}>
                      <span style={{ fontWeight: 700, textTransform: "capitalize", fontSize: 16, color: "#111827" }}>{item.skill}</span>
                      <span style={{ fontSize: 12, color: "#4b5563", background: "#f3f4f6", padding: "4px 10px", borderRadius: 12, fontWeight: 600 }}>~{item.estimatedWeeks || item.estimated_weeks} weeks</span>
                    </div>
                    <ul style={{ margin: 0, paddingLeft: 20, fontSize: 14, color: "#4b5563", lineHeight: 1.6 }}>
                      {item.resources.map(r => <li key={r} style={{ marginBottom: 6 }}>{r}</li>)}
                    </ul>
                  </div>
                ))}
              </div>
            </div>
          );
        })
      )}
    </div>
  );
}

// ==========================================
// Main Application State
// ==========================================
export default function App() {
  const [screen, setScreen] = useState("upload");
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleAnalyze = async (file, role) => {
    setError(null);
    setScreen("loading");
    try {
      const analysisResult = await analyzeResume(file, role);
      setResult(analysisResult);
      setScreen("analysis");
    } catch (err) {
      setError(err.message);
      setScreen("upload");
    }
  };

  return (
    <div style={{ minHeight: "100vh", background: "radial-gradient(circle at 50% 0%, #eef2ff 0%, #f9fafb 40%, #f9fafb 100%)", fontFamily: "system-ui, -apple-system, sans-serif" }}>
      <header style={{ background: "rgba(255, 255, 255, 0.8)", backdropFilter: "blur(12px)", borderBottom: "1px solid #f3f4f6", padding: "16px 24px", position: "sticky", top: 0, zIndex: 10 }}>
        <button onClick={() => { setScreen("upload"); setResult(null); setError(null); }} style={{ background: "none", border: "none", cursor: "pointer", fontWeight: "800", fontSize: 16, color: "#111827", display: "flex", alignItems: "center", gap: 8 }}>
          <div style={{ width: 24, height: 24, borderRadius: "50%", background: "linear-gradient(135deg, #6366f1, #8b5cf6)", color: "white", display: "flex", alignItems: "center", justifyContent: "center" }}><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></div>
          CareerLens AI
        </button>
      </header>

      <main style={{ paddingBottom: "4rem" }}>
        {screen === "upload" && <UploadScreen onAnalyze={handleAnalyze} error={error} />}
        {screen === "loading" && (
          <div style={{ textAlign: "center", padding: "6rem 2rem", display: "flex", flexDirection: "column", alignItems: "center", gap: 24 }}>
            <div style={{ width: 48, height: 48, border: "4px solid #e0e7ff", borderTopColor: "#6366f1", borderRadius: "50%", animation: "spin 1s linear infinite" }}></div>
            <div>
              <h3 style={{ fontSize: 18, fontWeight: 700, margin: "0 0 8px", color: "#111827" }}>Analyzing Resume</h3>
              <p style={{ color: "#6b7280", margin: 0 }}>Extracting data and calculating fit score...</p>
            </div>
            <style>{`@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }`}</style>
          </div>
        )}
        {screen === "analysis" && result && <AnalysisScreen result={result} onViewRoadmap={() => setScreen("roadmap")} onReset={() => setScreen("upload")} />}
        {screen === "roadmap" && result && <RoadmapScreen result={result} onBack={() => setScreen("analysis")} />}
      </main>
    </div>
  );
}