from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate1(RowTemplate1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        #self.text_box_1.border = "0px"
        self.text_box_1.text = self.item['prestation']
        #self.text_box_1.border = "0px white"
        self.text_box_2.text = self.item['tarif-1-jour']
        self.text_box_3.text = self.item['tarif-1/2-jour']

    


        