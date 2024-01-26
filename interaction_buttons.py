from kivy.uix.boxlayout import BoxLayout
from .buttons.refresh_button import RefreshButton
from .buttons.process_button import ProcessNewPDFsButton
from chat_pdf.modules.db_manager import DatabaseManager

class InteractionButtons(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.refresh_button = RefreshButton()
        self.refresh_button.bind(on_press=self.refresh_database)
        self.add_widget(self.refresh_button)
        self.add_widget(ProcessNewPDFsButton())

    def refresh_database(self, instance):
        with DatabaseManager() as db_manager:
            db_manager.refresh_database()
        print("Database refresh triggered & completed")
