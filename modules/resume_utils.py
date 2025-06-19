import streamlit as st
import google.generativeai as genai

# Load Gemini model
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_resume_summary(name, role, skills, experience):
    prompt = f"""
    Create a professional resume summary for the following person:
    
    Name: {name}
    Role: {role}
    Skills: {skills}
    Experience: {experience}

    Make it sound confident and job-ready. Limit to 3–4 sentences.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error: Could not generate summary.\nDetails: {e}"
