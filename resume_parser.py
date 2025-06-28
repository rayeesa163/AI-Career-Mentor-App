import fitz  # PyMuPDF
import re

def extract_resume_text(resume_path):
    doc = fitz.open(resume_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.lower()

def extract_name_from_resume(resume_text):
    # Try to find a name from the first few lines
    lines = resume_text.split('\n')
    for line in lines:
        words = line.strip().split()
        if 1 < len(words) <= 4 and all(word.isalpha() for word in words):
            return line.title()
    return "Candidate"
