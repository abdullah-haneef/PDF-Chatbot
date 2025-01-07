import PyPDF2
from io import BytesIO


def extract_text_from_pdf(file) -> str:
    """
    Extracts all text from an uploaded PDF file.

    Args:
        file: A file-like object representing the PDF (e.g. from Streamlit uploader).

    Returns:
        text (str): All extracted text from the PDF.
    """
    pdf_reader = PyPDF2.PdfReader(BytesIO(file.read()))
    extracted_text = ""

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        extracted_text += page.extract_text() + "\n"

    return extracted_text
