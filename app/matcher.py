from app.semantic_matcher import semantic_similarity

def match_resume_to_job(resume_skills, job_skills):
    """
    Compares resume skills with job requirements.
    """
    matched = set(resume_skills).intersection(set(job_skills))
    score = round((len(matched) / len(job_skills)) * 100, 2)

    missing = list(set(job_skills) - set(resume_skills))

    return {
        "match_score": score,
        "matched_skills": list(matched),
        "missing_skills": missing
    }
def rank_jobs(resume_skills, jobs_dict):
    """
    Ranks multiple job roles based on resume skills
    """
    results = []

    for role, job_skills in jobs_dict.items():
        matched = set(resume_skills) & set(job_skills)
        score = round((len(matched) / len(job_skills)) * 100, 2)

        results.append({
            "job_role": role,
            "match_score": score,
            "matched_skills": list(matched),
            "missing_skills": list(set(job_skills) - set(resume_skills))
        })

    # Sort by match score (highest first)
    results.sort(key=lambda x: x["match_score"], reverse=True)

    return results
from app.semantic_matcher import semantic_similarity


def hybrid_rank_jobs(resume_text, resume_skills, jobs_dict):
    """
    Hybrid ranking using:
    - Skill overlap (symbolic)
    - Semantic similarity (context-aware embeddings)
    """
    results = []

    for role, job_data in jobs_dict.items():
        job_skills = job_data["skills"]
        job_description = job_data["description"]

        # Skill overlap score
        matched = set(resume_skills) & set(job_skills)
        skill_score = (len(matched) / len(job_skills)) * 100

        # Semantic similarity score (context-aware)
        semantic_score = semantic_similarity(resume_text, job_description)

        # Hybrid weighted score
        final_score = round((0.6 * skill_score) + (0.4 * semantic_score), 2)

        results.append({
            "job_role": role,
            "final_score": final_score,
            "score_breakdown": {
                "skill_score": round(skill_score, 2),
                "semantic_score": semantic_score
            },
            "matched_skills": list(matched),
            "missing_skills": list(set(job_skills) - set(resume_skills))
        })

    results.sort(key=lambda x: x["final_score"], reverse=True)
    return results
