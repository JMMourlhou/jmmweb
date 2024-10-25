from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate1(ItemTemplate1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
 

        # Any code you write here will run before the form opens.
        self.text_box_code.text = self.item['code']
        self.text_box_prestation.text = self.item['prestation']
        self.text_box_tarif_1j.text = self.item['tarif_1_jour']
        self.text_box_tarif_1demi_j.text = self.item['tarif_1demi_jour']
        self.check_box_visible.checked = self.item['visible']
    
    def button_annuler_click(self, **event_args):
        """This method is called when the button is clicked"""
        r=alert("Voulez-vous détruire ce produit ?", dismissible=False ,buttons=[("oui",True),("non",False)])
        if r :   # Oui  
            anvil.server.call("destruction",self.item)
        self.f = get_open_form()   # récupération de la forme mère pour appeler la forme appelante
        self.f.affichage()

    def button_modif_click(self, **event_args):
        """This method is called when the button is clicked"""
        r=alert("Voulez-vous modifier ce produit ?", dismissible=False ,buttons=[("oui",True),("non",False)])
        if r :   # Oui
            anvil.server.call("modif",
                                    self.item,
                                    self.text_box_code.text,
                                    self.text_box_prestation.text,
                                    self.text_box_tarif_1j.text,
                                    self.text_box_tarif_1demi_j.text,
                                    self.check_box_visible.checked
                             )
            # Réaffichage 
            self.f = get_open_form()   # récupération de la forme mère pour appeler la forme appelante
            self.f.affichage()

    def text_box_tarif_1j_change(self, **event_args):
        """This method is called when the text in this text box is edited"""
        self.text_box_prestation_change()

    def text_box_tarif_1demi_j_change(self, **event_args):
        """This method is called when the text in this text box is edited"""
        self.text_box_prestation_change()

    def check_box_visible_change(self, **event_args):
        """This method is called when this checkbox is checked or unchecked"""
        self.text_box_prestation_change()

    def text_box_prestation_change(self, **event_args):
        """This method is called when the text in this text box is edited"""
        self.button_modif.visible = True

    

    
