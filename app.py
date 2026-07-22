import streamlit as st
import fitz
from skill_extractor import extract_skills
from ats_score import calculate_ats_score

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get an ATS analysis.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("✅ Resume uploaded successfully!")

    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    resume_text = ""

    for page in pdf:
        resume_text += page.get_text()

    if len(resume_text.strip()) == 0:

        st.error("⚠ No readable text found.")

        st.info("""
This PDF appears to be image-based or scanned.

Current Version Supports:
✔ Word PDF
✔ Google Docs PDF
✔ Text PDFs

Coming Soon:
✔ OCR Support for Canva and Scanned PDFs
        """)

    else:

        st.success("✅ Resume Text Extracted")

        st.write("Characters Extracted:", len(resume_text))

        st.subheader("📃 Resume Text")

        st.text_area(
            "Resume",
            resume_text,
            height=300
        )

        skills = extract_skills(resume_text)

        st.subheader("💻 Skills Found")

        if skills:
            st.success(", ".join(skills))
        else:
            st.warning("No predefined skills detected.")

        score = calculate_ats_score(resume_text, skills)

        st.subheader("📊 ATS Score")

        st.progress(score / 100)

        st.metric("ATS Score", f"{score}/100")

        st.subheader("💡 Suggestions")

        if score >= 85:
            st.success("Excellent Resume!")

        elif score >= 70:
            st.info("Good Resume. Add more technical skills and projects.")

        else:
            st.warning(
                "Improve your resume by adding projects, certifications, technical skills and achievements."
            )