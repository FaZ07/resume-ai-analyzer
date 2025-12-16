# 🚀 AI-Powered Resume Analyzer (Full-Stack)

A full-stack AI application that analyzes resumes, extracts skills, and intelligently matches them to job roles using NLP, semantic embeddings, and explainable scoring.

🔗 GitHub Repository:  
https://github.com/FaZ07/resume-ai-analyzer

---

## 📌 Features

- Resume parsing from PDF files
- Skill extraction using NLP
- Job-role matching using:
  - Rule-based skill matching
  - Semantic similarity (Sentence Transformers)
- Explainable scoring system
- Top job-role recommendations
- Full-stack implementation (FastAPI + React)

---

## 🏗️ Project Structure

resume-ai-analyzer/
├── app/
│ ├── main.py
│ ├── resume_parser.py
│ ├── skill_extractor.py
│ ├── matcher.py
│ ├── semantic_matcher.py
│ └── job_data.json
│
├── frontend/
│ ├── src/
│ │ ├── App.jsx
│ │ ├── main.jsx
│ │ └── index.css
│ └── package.json
│
└── README.md


---

## ⚙️ Tech Stack

### Backend
- Python
- FastAPI
- pdfplumber
- scikit-learn
- sentence-transformers
- PyTorch

### Frontend
- React
- Vite
- JavaScript
- CSS

---

## 🧠 How Matching Works

### Skill Matching
Extracted resume skills are compared with job-required skills.

### Semantic Matching
Resume text and job descriptions are converted into embeddings and compared using cosine similarity.

### Final Score
Final Score = (Skill Score × 0.6) + (Semantic Score × 0.4)


---

## 📥 Example API Output

```json
{
  "resume_skills": ["python", "aws", "flask", "machine learning"],
  "top_job_matches": [
    {
      "job_role": "Backend Developer",
      "final_score": 57.47,
      "matched_skills": ["python", "aws", "flask"],
      "missing_skills": ["sql", "fastapi"]
    }
  ]
}

▶️ Run Locally

Backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --port 8001

Frontend
cd frontend
npm install
npm run dev

Open http://localhost:5173

🧪 Use Cases

Resume self-analysis

Skill gap identification

Career role recommendations

ATS-style resume screening

🔮 Future Improvements

Resume vs Job Description comparison

Docker support

Cloud deployment

Skill learning roadmap generation

👨‍💻 Author

FaZ07
GitHub: https://github.com/FaZ07