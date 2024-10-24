from ._anvil_designer import Produits_majTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Produits_maj(Produits_majTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        list_produits = app_tables.produits.search(tables.order_by("code", ascending=True))
        self.repeating_panel_1.items = list_produits