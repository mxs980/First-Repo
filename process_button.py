from kivy.uix.button import Button
from chat_pdf.modules.pdf_processor import extract_text_from_pdfs
from chat_pdf.modules.db_manager import DatabaseManager

class ProcessNewPDFsButton(Button):
    def __init__(self, **kwargs):
        super().__init__(text='Process New PDFs', **kwargs)
        self.bind(on_release=self.process_new_pdfs)

    def process_new_pdfs(self, instance):
        with DatabaseManager() as db_manager:
            db_manager.refresh_database()
        print("Processing of new PDFs initiated") // INPUT_REQUIRED {Implement additional logic here if needed}
