import re
from collections import Counter

def extract_keywords(text):
    # Extract clean words with length > 2
    return re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())

def suggest_learning_path(resume_text, jd_text):
    stopwords = {
        "and", "the", "with", "for", "are", "this", "that", "have", "has", "you",
        "your", "from", "will", "all", "any", "our", "can", "who", "what", "when",
        "where", "how", "not", "job", "role", "work", "should", "their", "more",
        "get", "let", "also", "here", "there", "been", "being"
    }

    # Tokenize and filter
    resume_tokens = extract_keywords(resume_text)
    jd_tokens = extract_keywords(jd_text)

    resume_set = set(resume_tokens)
    jd_cleaned = [word for word in jd_tokens if word not in stopwords]

    # Count most common words in JD
    jd_counter = Counter(jd_cleaned)
    common_jd_keywords = [word for word, count in jd_counter.items() if count >= 2]

    # Get only the important job terms missing in resume
    missing = sorted(set(common_jd_keywords) - resume_set)
    return [word.title() for word in missing if len(word) > 2]
