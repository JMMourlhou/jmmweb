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
        self.f = get_open_form()   # récupération de la forme mère pour revenir ds la forme appelante

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
            self.f.content_panel.clear()
            self.f.content_panel.add_component(self.f, full_width_row=True)

    def button_modif_click(self, **event_args):
        """This method is called when the button is clicked"""
        pass

    def text_box_prestation_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        pass

    def text_box_code_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        pass

    
