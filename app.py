import streamlit as st
from resume_parser import extract_resume_text, extract_name_from_resume
from jd_parser import load_job_description
from resume_checker import compare_resume_with_jd
from roadmap_generator import suggest_learning_path
from report_generator import create_pdf_report
import time
import os

# Streamlit Page Setup
st.set_page_config(page_title="AI Career Mentor", page_icon="🎯", layout="centered")

st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 48px;
        color: #0A9396;
        font-weight: bold;
        font-family: 'Segoe UI', sans-serif;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #555;
        margin-bottom: 40px;
    }
    .section {
        background-color: #f7f7f7;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.05);
    }
    .stButton>button {
        background-color: #0A9396;
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }
    .stDownloadButton>button {
        background-color: #005F73;
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }
    footer {
        text-align: center;
        color: gray;
        margin-top: 50px;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Instructions
st.markdown("<div class='main-title'>AI Career Mentor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Upload your resume and a job description to receive personalized skill gap insights and a career report</div>", unsafe_allow_html=True)

# Upload Files
with st.sidebar:
    st.header("📂 Upload Files")
    resume_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
    jd_file = st.file_uploader("📝 Upload Job Description (TXT)", type=["txt"])

st.markdown("<div class='section'>", unsafe_allow_html=True)

if resume_file and jd_file:
    with st.spinner("🔍 Processing your documents..."):
        os.makedirs("data", exist_ok=True)
        resume_path = "data/resume.pdf"
        jd_path = "data/job_description.txt"
        with open(resume_path, "wb") as f:
            f.write(resume_file.read())
        with open(jd_path, "wb") as f:
            f.write(jd_file.read())

        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.002)
            progress.progress(i + 1)

        resume_text = extract_resume_text(resume_path)
        jd_text = load_job_description(jd_path)
        candidate_name = extract_name_from_resume(resume_text)
        match_score = compare_resume_with_jd(resume_text, jd_text)
        missing_skills = suggest_learning_path(resume_text, jd_text)

        st.success("✅ Analysis Complete!")
        st.subheader("📊 Resume Match Score")
        st.metric("Score", f"{match_score}%")

        st.subheader("🎯 Skill Gaps")
        if missing_skills:
            st.warning("🧠 These job-specific keywords are missing in your resume:")
            st.markdown("<div style='display: flex; flex-wrap: wrap; gap: 10px;'>", unsafe_allow_html=True)
            for skill in missing_skills:
                st.markdown(
                    f"<span style='background-color: #fff3cd; padding: 8px 12px; border-radius: 10px; color: #856404;'>{skill}</span>",
                    unsafe_allow_html=True,
                )
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.success("✅ Your resume covers all essential keywords from the job description!")

        st.subheader("📥 Download Report")
        pdf_path = create_pdf_report(candidate_name, match_score, missing_skills)
        with open(pdf_path, "rb") as f:
            st.download_button("📄 Download Career Report (PDF)", f, file_name="career_report.pdf")

else:
    st.info("👈 Upload both resume and job description to begin.")

st.markdown("</div>", unsafe_allow_html=True)

# Footer (No Emoji)
st.markdown("""
<footer>
Designed using <b>Python</b> & <b>Streamlit</b> • Developed by <b>Rayeesa Tabusum</b>
</footer>
""", unsafe_allow_html=True)
