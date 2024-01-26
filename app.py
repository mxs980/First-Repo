from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from chat_pdf.ui.query_input import QueryInput
from chat_pdf.ui.results_display import ResultsDisplay
from chat_pdf.ui.interaction_buttons import InteractionButtons

class ChatPdfUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.results_display = ResultsDisplay()
        self.query_input = QueryInput(results_display=self.results_display)
        self.add_widget(self.query_input)
        self.add_widget(self.results_display)
        self.add_widget(InteractionButtons())

class ChatPdfApp(App):
    def build(self):
        return ChatPdfUI()
