from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
import shutil
import json
import os

from app.resume_parser import extract_text_from_pdf
from app.skill_extractor import extract_skills
from app.matcher import hybrid_rank_jobs


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze/")
async def analyze_resume(file: UploadFile = File(...)):
    temp_file_path = f"temp_{file.filename}"

    # Save uploaded file temporarily
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process resume
    text = extract_text_from_pdf(temp_file_path)
    resume_skills = extract_skills(text)

    # Load job data
    with open("app/job_data.json", "r") as f:
        jobs = json.load(f)

    # Rank jobs
    ranked_jobs = hybrid_rank_jobs(text, resume_skills, jobs)


    # Clean up temp file (LAST STEP)
    os.remove(temp_file_path)

    return {
        "resume_skills": resume_skills,
        "top_job_matches": ranked_jobs[:3]
    }

