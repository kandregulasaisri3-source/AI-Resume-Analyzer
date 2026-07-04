import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF resume.
    """

    text = ""

    try:
        pdf = fitz.open(pdf_path)

        for page in pdf:
            text += page.get_text()

        pdf.close()

        # Clean extra spaces
        text = " ".join(text.split())

        return text

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    pdf_file = "resume.pdf"

    resume_text = extract_text_from_pdf(pdf_file)

    print(repr(resume_text))