from kivy.uix.textinput import TextInput
from chat_pdf.modules.qdrant_manager import QdrantManager
from chat_pdf.ui.results_display import ResultsDisplay

class QueryInput(TextInput):
    def __init__(self, results_display=None, **kwargs):
        super().__init__(**kwargs)
        self.results_display = results_display
        self.hint_text = 'Type your query here'
        self.multiline = False
        self.bind(on_text_validate=self.on_enter)

    def on_enter(self, instance):
        search_text = self.text
        print(f"Search initiated for: {search_text}")
        self.text = ''
        if search_text:
            search_results = self.perform_search(search_text)
            self.results_display.update_results(search_results)

    def perform_search(self, search_text):
        qdrant_manager = QdrantManager()
        search_results = qdrant_manager.search_pdf_data(query=search_text)
        formatted_results = "\n".join(str(result) for result in search_results['points'])
        return formatted_results
