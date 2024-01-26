from kivy.uix.button import Button
from chat_pdf.modules.db_connection import create_database_connection, DatabaseConnectionError

class RefreshButton(Button):
    def __init__(self, **kwargs):
        super().__init__(text='Refresh Database', **kwargs)
        self.bind(on_press=self.refresh_database)

    def refresh_database(self, instance):
        try:
            db_connection = create_database_connection()
            db_connection.refresh()
            db_connection.close()
            print('Database refreshed successfully!')
        except DatabaseConnectionError as e:
            print(f'Failed to refresh database: {e}')
