import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extract text from uploaded PDF
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        try:
            page_text = page.extract_text()
            if page_text:
                # Fix: replace invalid characters
                text += page_text.encode("utf-8", errors="ignore").decode("utf-8") + "\n"
        except Exception as e:
            text += f"\n[Error reading this page: {e}]\n"
    return text


# Rank resumes
def rank_resumes(job_description, resumes):
    docs = [job_description] + resumes
    vectorizer = TfidfVectorizer().fit_transform(docs)
    vectors = vectorizer.toarray()
    scores = cosine_similarity([vectors[0]], vectors[1:]).flatten()
    return scores

# Streamlit UI
st.set_page_config(page_title="Resume Ranker", layout="centered")
st.title("AI Resume Screening & Ranking System")

job_description = st.text_area("Enter the Job Description")
uploaded_files = st.file_uploader("Upload Resume PDFs", type=["pdf"], accept_multiple_files=True)

if job_description and uploaded_files:
    resumes = [extract_text_from_pdf(file) for file in uploaded_files]
    scores = rank_resumes(job_description, resumes)

    results = pd.DataFrame({
        "Resume": [file.name for file in uploaded_files],
        "Match Score": scores
    }).sort_values(by="Match Score", ascending=False)

    st.subheader("Ranking Results")
    st.write(results)
