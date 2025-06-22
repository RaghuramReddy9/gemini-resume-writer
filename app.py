import streamlit as st
from modules.resume_utils import generate_resume_summary, extract_text_from_pdf

st.set_page_config(page_title="AI Resume Generator", page_icon="💼", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #4ade80;'>AI Resume Summary Generator</h1>
    <p style='text-align: center;'>Create job-ready summaries using Google Gemini</p>
    <hr>
""", unsafe_allow_html=True)

st.subheader("🧾 Option 1: Fill Resume Details Manually")

name = st.text_input("Full Name")
role = st.text_input("Target Job Role")
skills = st.text_area("Top Skills (comma-separated)")
experience = st.text_area("Brief Work Experience")

if st.button("Generate Summary from Details"):
    if not name or not role or not skills or not experience:
        st.warning("⚠️ Please complete all fields.")
    else:
        with st.spinner("Generating your resume summary..."):
            summary = generate_resume_summary(name, role, skills, experience)
        st.success(summary)

st.markdown("---")

st.subheader("📤 Option 2: Upload Your Resume (PDF)")

uploaded_file = st.file_uploader("Upload a PDF Resume", type=["pdf"])

if uploaded_file:
    with st.spinner("Analyzing your resume..."):
        try:
            resume_text = extract_text_from_pdf(uploaded_file)
            summary = generate_resume_summary(resume_text)
            st.success(summary)
        except Exception as e:
            st.error(f"❌ Error reading file or generating summary: {e}")
