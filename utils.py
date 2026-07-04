import re


def clean_text(text):
    """
    Clean extracted resume text.
    """
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def calculate_score(found_skills, total_skills):
    """
    Calculate resume score.
    """
    if total_skills == 0:
        return 0

    score = (len(found_skills) / total_skills) * 100
    return round(score, 2)