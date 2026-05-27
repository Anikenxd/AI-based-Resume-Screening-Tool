# ==============================
# AI-Based Resume Screening Tool (Streamlit Web App)
# ==============================

import streamlit as st
import pandas as pd
import numpy as np
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from io import StringIO

# ==============================
# Setup and Downloads
# ==============================
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


def preprocess(text):
    """Clean and preprocess text data."""
    text = re.sub(r'[^a-zA-Z]', ' ', str(text))
    text = text.lower()
    words = text.split()
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
    return ' '.join(words)


# ==============================
# Streamlit UI
# ==============================
st.set_page_config(page_title="AI Resume Screening Tool", layout="centered")

st.title("🤖 AI-Based Resume Screening Tool")
st.write("Automatically match resumes to job descriptions using NLP and cosine similarity.")

# Upload resume dataset
uploaded_file = st.file_uploader(
    "📂 Upload Resume Dataset (CSV file)", type=["csv"])

# Upload or input job description
st.write("### 📝 Enter or Upload Job Description")
jd_text = st.text_area("Paste the job description here:")
jd_file = st.file_uploader(
    "Or upload a job description file (TXT, CSV, or PDF)", type=["txt", "csv", "pdf"])

# ==============================
# Process Job Description
# ==============================
job_desc = ""

if jd_file is not None:
    if jd_file.type == "text/plain":
        job_desc = jd_file.read().decode("utf-8")
    elif jd_file.type == "text/csv":
        jd_data = pd.read_csv(jd_file)
        job_desc = " ".join(jd_data.astype(str).values.flatten())
    elif jd_file.type == "application/pdf":
        import pdfminer.high_level as pdfminer
        job_desc = pdfminer.extract_text(jd_file)

if jd_text.strip() != "":
    job_desc = jd_text

# ==============================
# Run the Screening
# ==============================
if uploaded_file is not None and job_desc.strip() != "":
    df = pd.read_csv(uploaded_file)

    if "Resume" not in df.columns:
        st.error("❌ The CSV must contain a column named 'Resume'.")
    else:
        st.info("Processing resumes... This may take a moment ⏳")

        # Preprocess text
        df['Cleaned_Resume'] = df['Resume'].apply(preprocess)
        job_desc_cleaned = preprocess(job_desc)

        # TF-IDF + Cosine Similarity
        vectorizer = TfidfVectorizer(max_features=5000)
        vectors = vectorizer.fit_transform(
            df['Cleaned_Resume'].tolist() + [job_desc_cleaned])
        similarity = cosine_similarity(vectors[-1], vectors[:-1]).flatten()

        df['Match_Score'] = similarity
        top_matches = df.sort_values(
            by='Match_Score', ascending=False).head(10)

        # Show top results
        st.success("✅ Top Matching Resumes:")
        st.dataframe(top_matches[['Category', 'Match_Score', 'Resume']])

        # Download option
        csv = top_matches.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Top Matches as CSV",
            data=csv,
            file_name="top_resume_matches.csv",
            mime="text/csv"
        )

elif uploaded_file is not None:
    st.warning("⚠️ Please enter or upload a job description.")
elif job_desc.strip() != "":
    st.warning("⚠️ Please upload the resume dataset CSV.")
else:
    st.info("👆 Upload the resume dataset and job description to begin.")
