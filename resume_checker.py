import re

def extract_keywords(text):
    # Extract clean words of length 3+ from the text
    return set(re.findall(r'\b[a-zA-Z]{3,}\b', text.lower()))

def compare_resume_with_jd(resume_text, jd_text):
    # Extract keywords from both
    resume_words = extract_keywords(resume_text)
    jd_words = extract_keywords(jd_text)

    # Filter job description words to only those that are likely skills
    potential_skills = [word for word in jd_words if word in resume_words]

    if not jd_words:
        return 0

    # Calculate percentage match
    match_score = round((len(potential_skills) / len(jd_words)) * 100)
    return match_score


