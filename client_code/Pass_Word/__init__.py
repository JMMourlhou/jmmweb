from ._anvil_designer import Pass_WordTemplate
from anvil import *
import anvil.server


class Pass_Word(Pass_WordTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def button_valid_click(self, **event_args):
        """This method is called when the button is clicked"""
        pw = self.text_box_pw.text
        result = anvil.server.call('pw', pw)              
        if result:                           
            open_form("Produits_maj")
        else:
            alert("Mot de passe erroné !")

    def text_box_pw_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        self.button_valid_click()
