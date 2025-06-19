import streamlit as st
from modules.resume_utils import generate_resume_summary

st.set_page_config(page_title="AI Resume Generator", page_icon="💼", layout="centered")
st.title("📄 AI Resume Summary Generator")

# 🧾 Input fields
name = st.text_input("Enter your name")
role = st.text_input("Enter your target job role")
skills = st.text_area("List your top skills (comma-separated)")
experience = st.text_area("Briefly describe your past experience")

# 📤 Submit button
if st.button("✍️ Generate Summary"):
    if not name or not role or not skills or not experience:
        st.warning("⚠️ Please fill in all fields!")
    else:
        with st.spinner("Generating your resume summary..."):
            summary = generate_resume_summary(name, role, skills, experience)
        st.markdown("###  Your Resume Summary")
        st.success(summary)
