# AI Resume Analyzer

## Overview
AI Resume Analyzer is a Python-based application that analyzes resumes in PDF format without using any API keys. It extracts resume text, identifies technical skills, calculates a resume score, and provides suggestions to improve the resume.

## Features
- PDF resume parsing
- Skill extraction
- Resume scoring
- Resume improvement suggestions
- Offline processing (No API required)

## Technologies Used
- Python
- PyMuPDF
- Regular Expressions (Regex)

## Project Structure
```
AI_Resume_Analyzer/
│── app.py
│── skills.py
│── requirements.txt
│── README.md
│── .gitignore
│── sample_resume.pdf
│
└── src/
    ├── resume_parser.py
    ├── analyzer.py
    └── utils.py
```

## Installation

1. Clone the repository.
2. Install the required packages:
```
pip install -r requirements.txt
```

## Run the Project

```
python app.py
```

## How It Works

1. Upload or provide a PDF resume.
2. The parser extracts text from the resume.
3. The analyzer detects skills.
4. The application calculates a resume score.
5. Suggestions are displayed to improve the resume.

## Future Enhancements

- OCR support for scanned resumes.
- Job description matching.
- Resume keyword optimization.
- Web-based interface using Streamlit.

## Author

Sai Sri
B.Tech – Computer Science and Data Science Engineering
Dadi Institute of Engineering and Technology