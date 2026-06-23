# 🤖 AI-Based Resume Screening Tool

An AI-powered Resume Screening Tool built with Python and Streamlit that automatically matches resumes to job descriptions using Natural Language Processing (NLP) and Cosine Similarity.

## 🚀 Project Overview

Recruiters often receive hundreds of resumes for a single job opening. This project helps automate the initial screening process by comparing resumes against a job description and ranking candidates based on their similarity scores.

The application uses NLP techniques to preprocess text data and machine learning algorithms to calculate matching scores.

## ✨ Features

✅ Upload resume datasets in CSV format
✅ Enter or upload job descriptions
✅ Resume text preprocessing using NLP
✅ TF-IDF Vectorisation
✅ Cosine Similarity Matching
✅ Automatic candidate ranking
✅ Download top matching resumes as CSV
✅ User-friendly Streamlit web interface

## 🛠️ Technologies Used

* 🐍 Python
* 🎈 Streamlit
* 🐼 Pandas
* 🔢 NumPy
* 🧠 NLTK
* 🤖 Scikit-learn
* 📄 PDFMiner
* 📊 Machine Learning & NLP

## 📂 Project Workflow

### 1️⃣ Data Input

* Upload resume dataset (CSV)
* Enter or upload job description

### 2️⃣ Text Preprocessing

* Remove special characters
* Convert text to lowercase
* Remove stopwords
* Perform lemmatisation

### 3️⃣ Feature Extraction

* Convert text into numerical vectors using TF-IDF

### 4️⃣ Similarity Analysis

* Calculate cosine similarity between resumes and job descriptions

### 5️⃣ Candidate Ranking

* Assign match scores
* Display top matching resumes
* Export results as CSV

## 📊 Machine Learning Techniques Used

### TF-IDF Vectorisation

Converts textual data into numerical feature vectors based on word importance.

### Cosine Similarity

Measures how closely a resume matches the job description.

## 📸 Application Preview

Add screenshots of:

<img width="1920" height="1080" alt="Screenshot 2026-06-23 191822" src="https://github.com/user-attachments/assets/f668b72b-003e-475c-b83c-714918fa03da" />

<img width="1920" height="1080" alt="Screenshot 2026-06-23 191911" src="https://github.com/user-attachments/assets/6bb13e56-08e4-4319-9219-838345bb4f65" />


## 🔧 Installation

### Clone Repository

```bash
git clone https://github.com/Anikenxd/AI-based-Resume-Screening-Tool.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

## 📋 Required Libraries

```text
streamlit
pandas
numpy
nltk
scikit-learn
pdfminer.six
```

## 🎯 Learning Outcomes

* Natural Language Processing (NLP)
* Text Preprocessing
* TF-IDF Vectorization
* Cosine Similarity
* Machine Learning Fundamentals
* Streamlit Web Application Development

## 🌱 Future Improvements

* Support for DOCX resumes
* Resume skill extraction
* AI-based candidate recommendations
* Interactive analytics dashboard
* Resume keyword highlighting

## 👨‍💻 Author

**Afreaz**

🎓 BCA Graduate
📊 Aspiring Data Analyst
🐍 Learning Python, SQL, Excel, Power BI, and Machine Learning

### GitHub

https://github.com/Anikenxd

---

⭐ If you found this project useful, consider giving it a star!
