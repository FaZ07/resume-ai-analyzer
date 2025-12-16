from sentence_transformers import SentenceTransformer, util

# Load model once (very important for performance)
model = SentenceTransformer("all-MiniLM-L6-v2")


from sentence_transformers import SentenceTransformer, util

# Load model once (performance critical)
model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_similarity(resume_text: str, job_description: str) -> float:
    """
    Computes semantic similarity between resume text and full job description.
    Returns a percentage score.
    """
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_description, convert_to_tensor=True)

    similarity = util.cos_sim(resume_embedding, job_embedding).item()

    return round(similarity * 100, 2)
