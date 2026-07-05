AI Resume Analyzer Agent

Overview

AI Resume Analyzer Agent is an Agentic AI project developed using Python, Streamlit, and the Google Gemini API. The application analyzes PDF resumes, identifies skills, evaluates strengths and weaknesses, provides a resume score, and suggests improvements to help users create better resumes.

Features

- Upload PDF resumes
- Extract text from resumes
- AI-powered resume analysis
- Resume score generation
- Skills extraction
- Strengths and weaknesses analysis
- Resume improvement suggestions
- User-friendly Streamlit interface

Technologies Used

- Python
- Streamlit
- Google Gemini API
- PyPDF2
- Prompt Engineering
- Agentic AI
- Git & GitHub

Project Structure

AI_Resume_Analyzer/
│── app.py
│── agent.py
│── requirements.txt
│── README.md
│── .gitignore
└── sample_resume.pdf

Installation

1. Clone the repository.
2. Install the required packages:

pip install -r requirements.txt

3. Create a ".env" file and add your Gemini API key:

GEMINI_API_KEY=YOUR_API_KEY

4. Run the application:

streamlit run app.py

Workflow

1. Upload a PDF resume.
2. Extract text from the resume.
3. Send the extracted text to the Gemini AI model.
4. Analyze the resume.
5. Display the resume score, skills, strengths, weaknesses, and improvement suggestions.

Future Enhancements

- ATS Resume Score
- Job Description Matching
- Interview Question Generator
- Downloadable Analysis Report
- Multi-language Support

Author

Sai Sri

Computer Science and Data Science Engineering

Dadi Institute of Engineering and Technology
