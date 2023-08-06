from ._anvil_designer import ProduitsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
global dico_prestation
dico_prestation = app_tables.produits.search() 

class Produits(ProduitsTemplate):
    def __init__(self, condition="", **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        #dico_prestation = app_tables.produits.search()    # tte la table produits lue
        
        global dico_prestation
        if dico_prestation[0]['visible'] == True:
            self.button_1.text = dico_prestation[0]['prestation']
        else:
            self.button_1.visible = False
        
        if dico_prestation[1]['visible'] == True:
            self.button_2.text = dico_prestation[1]['prestation']
        else:
            self.button_2.visible = False
             
        if dico_prestation[2]['visible'] == True:
            self.button_3.text = dico_prestation[2]['prestation']
        else:
            self.button_3.visible = False
            
        if dico_prestation[3]['visible'] == True:
            self.button_4.text = dico_prestation[3]['prestation']
        else:
            self.button_4.visible = False
            
        if dico_prestation[4]['visible'] == True:
            self.button_5.text = dico_prestation[4]['prestation']
        else:
            self.button_5.visible = False
             
        if dico_prestation[5]['visible'] == True:
            self.button_6.text = dico_prestation[5]['prestation']
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
        
    def code1_click(self, **event_args):     #SST i
        """This method is called when the button is clicked"""
        global dico_prestation
        self.label_en_tete.text = dico_prestation[0]['prestation']   
        self.label_en_tete.visible = True
        self.label_mes_tarifs.visible = True
        
        self.column_panel_bt_01.visible = True
        self.column_panel_bt_02.visible = False
        self.column_panel_bt_03.visible = False
        """self.column_panel_bt_04.visible = False
        self.column_panel_bt_05.visible = False
        self.column_panel_bt_06.visible = False
        """
        self.affiche_prix("SST-i%")

    def code2_click(self, **event_args):              #MAC SST
        """This method is called when the button is clicked"""
        global dico_prestation
        self.label_en_tete.text = dico_prestation[1]['prestation']   
        self.label_en_tete.visible = True
        self.label_mes_tarifs.visible = True
        
        self.column_panel_bt_01.visible = False
        self.column_panel_bt_02.visible = True
        self.column_panel_bt_03.visible = False
        """self.column_panel_bt_04.visible = False
        self.column_panel_bt_05.visible = False
        self.column_panel_bt_06.visible = False
        """
        self.affiche_prix("SST-M%")
        

    def code3_click(self, **event_args):
        """This method is called when the button is clicked"""
        global dico_prestation
        self.label_en_tete.text = dico_prestation[2]['prestation']   
        self.label_en_tete.visible = True
        self.label_mes_tarifs.visible = True
        
        self.column_panel_bt_01.visible = False
        self.column_panel_bt_02.visible = False
        self.column_panel_bt_03.visible = True
        """self.column_panel_bt_04.visible = False
        self.column_panel_bt_05.visible = False
        self.column_panel_bt_06.visible = False
        """
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






        