import fitz
import os
from pdfminer.high_level import extract_text

def extract_pdf_text(file_path):
    """
    Extract text from a given PDF file using pdfminer and PyMuPDF.
    """
    try:
        text = extract_text(file_path)
    except Exception as e:
        print(f"Error extracting text with pdfminer from {file_path}: {e}")
        text = None

    # Fallback to PyMuPDF if pdfminer fails
    if not text:
        try:
            with fitz.open(file_path) as pdf:
                text = ""
                for page in pdf:
                    text += page.get_text()
        except Exception as e:
            print(f"Error extracting text with PyMuPDF from {file_path}: {e}")
            text = None

    return text


def process_folder(folder_path):
    """
    Iterate through all PDF files in the folder and subfolders,
    and extract text from each.
    """
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith('.pdf'):
                file_path = os.path.join(root, filename)
                text = extract_pdf_text(file_path)
                if text:
                    yield file_path, text


def extract_text_from_pdfs(folder_path):
    """
    Process a root folder and extract text from all PDF files.
    """
    pdf_texts = list(process_folder(folder_path))
    for file_path, text in pdf_texts:
        print(f"Extracted {len(text)} characters from {file_path}")

    return pdf_texts
