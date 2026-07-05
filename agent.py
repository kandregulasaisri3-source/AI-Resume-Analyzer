from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    return text

def analyze_resume(text):
    prompt = f"""
You are an AI Resume Analyzer.

Analyze the following resume and provide:

1. Resume Score (/100)
2. Skills
3. Strengths
4. Weaknesses
5. Missing Skills
6. Suggestions

Resume:
{text}
"""

    response = model.generate_content(prompt)

    return response.text