# 📄 AI Resume Analyzer

An AI-powered resume analysis web application built with Python and Streamlit.

The application allows users to upload a resume in PDF format and compare it with a job description. It analyzes technical skills, calculates job compatibility, performs basic ATS checks, and provides resume improvement suggestions.

---

## 🚀 Features

- 📤 Upload resume in PDF format
- 🔎 Extract text from digital and scanned resumes
- 🧠 OCR support using Tesseract
- 🛠️ Extract technical skills from resumes
- 💼 Extract technical skills from job descriptions
- 📊 Calculate skill match percentage
- 🤖 Calculate resume-job text similarity using TF-IDF
- 📋 Perform basic ATS compatibility checks
- ✅ Identify matching skills
- ❌ Identify missing skills
- 📌 Calculate job keyword coverage
- 💡 Generate resume improvement recommendations
- 📖 View extracted resume text
- 🌐 Interactive Streamlit web interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- PyPDF
- PyMuPDF
- Tesseract OCR
- Pytesseract
- Pillow
- NLTK

---

## 🧠 How It Works

The application follows these steps:

### 1. Resume Upload

The user uploads a resume in PDF format.

### 2. Text Extraction

The application first attempts normal PDF text extraction.

If the PDF does not contain readable text, OCR is used to extract text from scanned pages.

### 3. Skill Extraction

Technical skills are detected from both:

- Resume
- Job description

### 4. Skill Matching

The application compares resume skills with job-required skills.

It identifies:

- Matching skills
- Missing skills
- Skill match percentage

### 5. Text Similarity

TF-IDF vectorization and cosine similarity are used to calculate the similarity between the resume and job description.

### 6. ATS Analysis

The application performs basic ATS-friendly checks including:

- Contact information
- Education
- Skills section
- Projects
- Experience / Internship
- Certifications
- Quantifiable achievements
- Action-oriented content
- Resume length

### 7. Recommendations

The application generates suggestions based on missing skills and failed ATS checks.

---

## 📁 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── job_matcher.py
├── ats_analyzer.py
├── recommendations.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── venv/