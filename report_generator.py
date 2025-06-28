from fpdf import FPDF
import os

def create_pdf_report(name, score, skills):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="AI Career Mentor Report", ln=1, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=1)
    pdf.cell(200, 10, txt=f"Resume Match Score: {score}%", ln=1)
    pdf.ln(5)

    if skills:
        pdf.cell(200, 10, txt="Suggested Skills to Learn:", ln=1)
        for skill in skills:
            pdf.cell(200, 10, txt=f"- {skill.title()}", ln=1)
    else:
        pdf.cell(200, 10, txt="You're ready for this job!", ln=1)

    os.makedirs("outputs", exist_ok=True)
    path = "outputs/career_report.pdf"
    pdf.output(path)
    return path

