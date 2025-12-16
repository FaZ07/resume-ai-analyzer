import pdfplumber

def extract_text_from_pdf(file_path: str) -> str:
    """
    Reads a PDF resume and returns all text as a lowercase string.
    """
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text.lower()
