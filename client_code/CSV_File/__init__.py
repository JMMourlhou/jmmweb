from ._anvil_designer import CSV_FileTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class CSV_File(CSV_FileTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def file_loader_1_change(self, file, **event_args):
        """This method is called when a new file is loaded into this FileLoader"""
        verif, nb = anvil.server.call('csv_file_reader', file)
        msg = f"{verif}, {nb} lignes écrites"
        alert(msg)
