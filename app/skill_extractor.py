import spacy
from spacy.matcher import PhraseMatcher

# Load NLP model once (important for performance)
nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "python", "java", "sql", "aws", "docker", "kubernetes",
    "machine learning", "deep learning", "nlp",
    "fastapi", "flask", "react", "git"
]
SKILL_ALIASES = {
    "ml": "machine learning",
    "ai": "machine learning",
    "machine-learning": "machine learning",
    "deep-learning": "deep learning"
}

# Create phrase matcher
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(skill) for skill in SKILLS_DB]
matcher.add("SKILLS", patterns)


def extract_skills(text: str):
    doc = nlp(text)
    matches = matcher(doc)

    found_skills = set()

    # Phrase matches
    for _, start, end in matches:
        found_skills.add(doc[start:end].text.lower())

    # Alias handling
    for alias, normalized in SKILL_ALIASES.items():
        if alias in text:
            found_skills.add(normalized)

    return list(found_skills)
