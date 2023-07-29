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
        liste_prestation = app_tables.produits.search()
        """for row in liste_prestations:
            if row["code"]==1:
                self.button_1.text = row['prestation']
            if produit["code"]==2:
                self.button_2.text = row['prestation']
            if produit["code"]==3:
                self.button_3.text = row['prestation']
        """
        self.button_1.text = liste
    
        # selects the prestations starting with "SST"
        # condition="SST%"
        # self.repeating_panel_1.items = app_tables.produits.search(prestation=q.ilike(condition))
        
        # Any code you write here will run when the form opens.

    
    def affiche_prix(self, condition):
        # selects the prestations starting with var condition
        # ex condition="SST%"
        self.repeating_panel_1.items = app_tables.produits.search(prestation=q.ilike(condition))
        self.data_grid_1.visible = True
        
    def code1_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.affiche_prix("SST-I%")

    def code2_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.affiche_prix("SST-F%")

    def code3_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.affiche_prix("PSC%")



        