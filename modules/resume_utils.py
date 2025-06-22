import google.generativeai as genai
import streamlit as st
import fitz  # PyMuPDF for reading PDFs

# Configure Gemini API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def generate_resume_summary(*args):
    """
    Generates a resume summary using Gemini API.
    - If 1 argument: treat it as resume text (PDF case).
    - If 4 arguments: use name, role, skills, experience (form input case).
    """
    if len(args) == 1:
        resume_text = args[0]
        prompt = f"You're a career expert. Summarize this resume:\n\n{resume_text}"
    else:
        name, role, skills, experience = args
        prompt = (
            f"Write a compelling professional resume summary for {name}, "
            f"who is applying for a {role} role. "
            f"Key skills: {skills}. Experience: {experience}."
        )

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()


def extract_text_from_pdf(uploaded_file):
    """
    Extracts raw text from an uploaded PDF resume using PyMuPDF.
    """
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()
import google.generativeai as genai
import streamlit as st
import fitz  # PyMuPDF for reading PDFs

# Configure Gemini API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def generate_resume_summary(*args):
    """
    Generates a resume summary using Gemini API.
    - If 1 argument: treat it as resume text (PDF case).
    - If 4 arguments: use name, role, skills, experience (form input case).
    """
    if len(args) == 1:
        resume_text = args[0]
        prompt = f"You're a career expert. Summarize this resume:\n\n{resume_text}"
    else:
        name, role, skills, experience = args
        prompt = (
            f"Write a compelling professional resume summary for {name}, "
            f"who is applying for a {role} role. "
            f"Key skills: {skills}. Experience: {experience}."
        )

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()


def extract_text_from_pdf(uploaded_file):
    """
    Extracts raw text from an uploaded PDF resume using PyMuPDF.
    """
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()
