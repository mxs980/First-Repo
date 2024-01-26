from chat_pdf.modules.pdf_processor import extract_text_from_pdfs
from chat_pdf.modules.qdrant_manager import QdrantManager

class DatabaseManager:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def refresh_database(self):
        pdf_texts = extract_text_from_pdfs(folder_path='C:\Users\Mo7am\Downloads\PDF Chat Files 2') 
        qdrant_manager = QdrantManager()
        for file_path, text in pdf_texts:
            pdf_data = PDFData(text_vectors=text, name=file_path.stem, path=str(file_path))
            qdrant_manager.store_pdf_data(pdf_data)
        print(f"Processed and updated {len(pdf_texts)} PDFs in the database")
