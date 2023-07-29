from ._anvil_designer import ProduitsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class Produits(ProduitsTemplate):
    def __init__(self, condition="", **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # selects the prestations starting with "SST"
        condition="SST%"
        self.repeating_panel_1.items = app_tables.produits.search(prestation=q.ilike(condition))
        
        # Any code you write here will run when the form opens.
        