from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label

class ResultsDisplay(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.result_label = Label(size_hint_y=None)
        self.add_widget(self.result_label)

    def update_results(self, text):
        self.result_label.text = text
