from src.resume_parser import extract_text_from_pdf
from src.analyzer import analyze_resume


def main():

    print("=" * 50)
    print("        AI RESUME ANALYZER")
    print("=" * 50)

    pdf_path = input("Enter Resume PDF Path: ")

    resume_text = extract_text_from_pdf(pdf_path)

    if resume_text.startswith("Error"):
        print(resume_text)
        return

    result = analyze_resume(resume_text)

    print("\nResume Analysis")
    print("-" * 50)

    print(f"Resume Score : {result['score']}%")

    print("\nSkills Found:")
    if result["skills"]:
        for skill in result["skills"]:
            print(f"✔ {skill}")
    else:
        print("No skills detected.")

    print("\nSuggestions:")
    if result["suggestions"]:
        for suggestion in result["suggestions"]:
            print(f"• {suggestion}")
    else:
        print("Excellent Resume!")


if __name__ == "__main__":
    main()