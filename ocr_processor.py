import pytesseract
from PIL import Image
import cv2
import io
import fitz  # PyMuPDF

# INPUT_REQUIRED {Path to the Tesseract executable}
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'


def ocr_image_to_text(image):
    """
    Extract text from an image using Tesseract OCR.
    """
    text = pytesseract.image_to_string(image, lang='eng')
    return text


def extract_images_from_pdf(file_path):
    """
    Extract images from a PDF file using PyMuPDF.
    """
    with fitz.open(file_path) as pdf:
        images = []
        for page in pdf:
            for img_index, img in enumerate(page.get_images(full=True)):
                xref = img[0]
                base_image = pdf.extract_image(xref)
                image_bytes = base_image["image"]
                image = Image.open(io.BytesIO(image_bytes))
                images.append(image)
        return images


def ocr_pdf_to_text(file_path):
    """
    Extract text from a scanned PDF by first extracting images and then performing OCR on them.
    """
    images = extract_images_from_pdf(file_path)
    text = ' '.join(ocr_image_to_text(image) for image in images)
    return text
