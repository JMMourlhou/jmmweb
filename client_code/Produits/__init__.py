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
        dico_prestation = app_tables.produits.search()    # tte la table produits lue
        
        if dico_prestation[0]['visible'] == True:
            self.button_1.text = dico_prestation[0]['prestation']+"    V"
        else:
            self.button_1.visible = False
        
        if dico_prestation[1]['visible'] == True:
            self.button_2.text = dico_prestation[1]['prestation']+"    V"
        else:
            self.button_2.visible = False
             
        if dico_prestation[2]['visible'] == True:
            self.button_3.text = dico_prestation[2]['prestation']+"    V"
        else:
            self.button_3.visible = False
            
        if dico_prestation[3]['visible'] == True:
            self.button_4.text = dico_prestation[3]['prestation']+"    V"
        else:
            self.button_4.visible = False
            
        if dico_prestation[4]['visible'] == True:
            self.button_5.text = dico_prestation[4]['prestation']+"    V"
        else:
            self.button_5.visible = False
             
        if dico_prestation[5]['visible'] == True:
            self.button_6.text = dico_prestation[5]['prestation']+"    V"
        else:
            self.button_6.visible = False
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
        self.affiche_prix("SST%")

    def code2_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.affiche_prix("SST%")

    def code3_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.affiche_prix("PSC%")

    def code4_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.affiche_prix("PSE%")

    def code5_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.affiche_prix("PSE%")

    def code6_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.affiche_prix("Ang%")






        