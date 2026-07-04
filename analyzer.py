from skills import skills
from src.utils import clean_text, calculate_score


def analyze_resume(resume_text):
    """
    Analyze the resume and return score, skills, and suggestions.
    """

    # Clean the extracted text
    resume_text = clean_text(resume_text)

    # Find matching skills
    found_skills = []

    for skill in skills:
        if skill.lower() in resume_text:
            found_skills.append(skill)

    # Calculate score
    score = calculate_score(found_skills, len(skills))

    # Generate suggestions
    suggestions = []

    if score < 30:
        suggestions.append("Add more technical skills.")
        suggestions.append("Include projects in your resume.")
        suggestions.append("Mention internships or work experience.")
        suggestions.append("Add certifications if available.")

    elif score < 60:
        suggestions.append("Include more relevant technical skills.")
        suggestions.append("Improve project descriptions.")
        suggestions.append("Highlight achievements with numbers.")

    else:
        suggestions.append("Your resume looks strong.")
        suggestions.append("Keep your resume updated.")

    return {
        "score": score,
        "skills": found_skills,
        "suggestions": suggestions
    }