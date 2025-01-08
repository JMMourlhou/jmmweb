from ._anvil_designer import ProduitsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
global dico_prestation
dico_prestation = {} 


class Produits(ProduitsTemplate):
    def __init__(self, condition="", **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.timer = 1
        global dico_prestation
        dico_prestation = app_tables.produits.search(tables.order_by("code", ascending=True))    # tte la table produits lue
        if len(dico_prestation)>0:
            # Prestation 1
            if dico_prestation[0]['visible'] is True:
                self.button_1.text = dico_prestation[0]['prestation']
            else:
                self.button_1.visible = False
                
            # Prestation 2
            if dico_prestation[1]['visible'] is True:
                self.button_2.text = dico_prestation[1]['prestation']
            else:
                self.button_2.visible = False
            
            # Prestation 3            
            if dico_prestation[2]['visible'] is True:
                self.button_3.text = dico_prestation[2]['prestation']
            else:
                self.button_3.visible = False
    
            # Prestation 4
            if dico_prestation[3]['visible'] is True:
                self.button_4.text = dico_prestation[3]['prestation']
            else:
                self.button_4.visible = False
    
            # Prestation 5
            if dico_prestation[4]['visible'] is True:
                self.button_5.text = dico_prestation[4]['prestation']
            else:
                self.button_5.visible = False
 
    
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
        self.column_panel_bt_04.visible = False
        self.column_panel_bt_05.visible = False
        """
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
        self.column_panel_bt_04.visible = False
        self.column_panel_bt_05.visible = False
        """
        self.column_panel_bt_06.visible = False
        """
        self.affiche_prix("SST-M%")
        

    def code3_click(self, **event_args):               #PSE1
        """This method is called when the button is clicked"""
        global dico_prestation
        self.label_en_tete.text = dico_prestation[2]['prestation']   
        self.label_en_tete.visible = True
        self.label_mes_tarifs.visible = True
        
        self.column_panel_bt_01.visible = False
        self.column_panel_bt_02.visible = False
        self.column_panel_bt_03.visible = True
        self.column_panel_bt_04.visible = False
        self.column_panel_bt_05.visible = False
        """
        self.column_panel_bt_06.visible = False
        """
        self.affiche_prix("PSE1%")

    def code4_click(self, **event_args):            #PSE2
        """This method is called when the button is clicked"""
        global dico_prestation
        self.label_en_tete.text = dico_prestation[3]['prestation']   
        self.label_en_tete.visible = True
        self.label_mes_tarifs.visible = True
        
        self.column_panel_bt_01.visible = False
        self.column_panel_bt_02.visible = False
        self.column_panel_bt_03.visible = False
        self.column_panel_bt_04.visible = True
        """self.column_panel_bt_05.visible = False
        self.column_panel_bt_06.visible = False
        """
        self.affiche_prix("PSE%")

    def code5_click(self, **event_args):
        """This method is called when the button is clicked"""
        global dico_prestation
        self.label_en_tete.text = dico_prestation[4]['prestation']   
        self.label_en_tete.visible = True
        self.label_mes_tarifs.visible = True
        
        self.column_panel_bt_01.visible = False
        self.column_panel_bt_02.visible = False
        self.column_panel_bt_03.visible = False
        self.column_panel_bt_04.visible = False
        self.column_panel_bt_05.visible = True
        
        self.affiche_prix("PSE%")


    def timer_1_tick(self, **event_args):
        """This method is called Every [0,5] seconds. Does not trigger if [interval] is 0."""
        if self.timer == 1:
            self.button_1.foreground = "red"
            self.button_5.foreground = "theme:background bleu foncé"
        if self.timer == 2:
            self.button_2.foreground = "red"
            self.button_1.foreground = "theme:background bleu foncé"
        if self.timer == 3:
            self.button_3.foreground = "red"
            self.button_2.foreground = "theme:background bleu foncé"
        if self.timer == 4:
            self.button_4.foreground = "red"
            self.button_3.foreground = "theme:background bleu foncé"
        if self.timer == 5:
            self.button_5.foreground = "red"
            self.button_4.foreground = "theme:background bleu foncé"

        self.timer += 1
        if self.timer == 6:
            self.timer = 1






        