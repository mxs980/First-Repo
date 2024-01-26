import fitz  # PyMuPDF
from pdfminer.high_level import extract_text

def extract_pdfminer_text(file_path):
    """
    Extract text from a PDF file using pdfminer.
    """
    try:
        text = extract_text(file_path)
    except Exception as e:
        print(f"Error extracting text with pdfminer from {file_path}: {e}")
        text = None
    return text

def extract_pymupdf_text(file_path):
    """
    Extract text from a PDF file using PyMuPDF.
    """
    try:
        with fitz.open(file_path) as pdf:
            text = ""
            for page in pdf:
                text += page.get_text()
    except Exception as e:
        print(f"Error extracting text with PyMuPDF from {file_path}: {e}")
        text = None
    return text
