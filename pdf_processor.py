import os
from .pdf_utils import extract_pdfminer_text, extract_pymupdf_text
from .ocr_processor import ocr_pdf_to_text

def extract_pdf_text(file_path):
    """
    Try extracting text from a given PDF file with pdfminer, then fallback to PyMuPDF if necessary,
    finally use Tesseract OCR if other methods fail.
    """
    text = extract_pdfminer_text(file_path)
    if not text:  # First fallback to PyMuPDF
        text = extract_pymupdf_text(file_path)

    if not text:  # Last resort OCR
        text = ocr_pdf_to_text(file_path)

    return text

def process_folder(folder_path):
    """
    Iterate through all PDF files in the folder and subfolders, and extract text from each.
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
