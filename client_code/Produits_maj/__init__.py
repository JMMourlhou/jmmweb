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

        # lecture table Produits
        self.list_produits = app_tables.produits.search(tables.order_by("code", ascending=True))
        self.nb_produits = len(self.list_produits)
        if self.nb_produits >= 6:
            self.button_new.visible = False
        self.repeating_panel_1.items = self.list_produits

    def button_new_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.column_panel_add.visible = True
        self.repeating_panel_1.visible = False
        self.text_box_code.text = str(len(self.list_produits)+1)

    def focus(self, **event_args):
        self.text_box_prestation.focus()

    def text_box_code_change(self, **event_args):
        """This method is called when the text in this text box is edited"""
        self.text_box_prestation_pressed_enter()

    def text_box_prestation_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        self.button_valid.visible = True

    def text_box_code_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        self.text_box_prestation_pressed_enter()

    def text_box_tarif_1j_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        self.text_box_prestation_pressed_enter()

    def text_box_tarif_1demi_j_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        self.text_box_prestation_pressed_enter()

    def check_box_visible_change(self, **event_args):
        """This method is called when this checkbox is checked or unchecked"""
        self.text_box_prestation_pressed_enter()

    def button_modif_click(self, **event_args):
        """This method is called when the button is clicked"""
        pass

    def button_annuler_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.text_box_code.text = ""
        self.text_box_prestation.text = ""
        self.text_box_tarif_1j.text = ""
        self.text_box_tarif_1demi_j.text = ""
        self.check_box_visible.checked = ""
        self.column_panel_add.visible = False
        self.button_valid.visible = False
        self.repeating_panel_1.visible = True

    def button_valid_click(self, **event_args):
        """This method is called when the button is clicked"""
        r=alert("Voulez-vous ajouter ce produit ?", dismissible=False ,buttons=[("oui",True),("non",False)])
        if r :   # Oui
            anvil.server.call("add",
                                    self.text_box_code.text,
                                    self.text_box_prestation.text,
                                    self.text_box_tarif_1j.text,
                                    self.text_box_tarif_1demi_j.text,
                                    self.check_box_visible.checked
                             )
            # Réaffichage 
            self.affichage()

    def affichage(self):
        self.list_produits = app_tables.produits.search(tables.order_by("code", ascending=True))
        self.repeating_panel_1.items = self.list_produits
        self.column_panel_add.visible = False
        self.repeating_panel_1.visible = True

    def button_retour_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('Main')

    def button_up_link_click(self, **event_args):
        """This method is called when the button is clicked"""
        import anvil.server
        anvil.server.connect("server_X4KQFEN7FOJZABUTXN2Q4YTJ-TKG7FZR3ZP7CNQYJ")
        rows = app_tables.produits.search()
        anvil.server.
        nb_rows = len(rows)
        print(nb_rows)
        
        anvil.server.call('writing_after_uplink',rows)


# fonction --------------------------------------------------
def get_data_from_anvil():
    rows = app_tables.produits.search()
    nb_rows = len(rows)
    print(nb_rows)
    return rows

# Main -------------------------------------------------------
rows = get_data_from_anvil()
for row in rows:
    print(row["code"],row["prestation"],row["visible"],row["tarif_1_jour"],row["tarif_1demi_jour"])
print("Fin de fichier")
        anvil.server.disconnect() # déconnexion d'Anvil

        msg=str(nb_rows)+" lignes lues"
        alert(msg)

        # ----------------------------------------------------------
import anvil.server
from anvil.tables import app_tables
anvil.server.connect("server_X4KQFEN7FOJZABUTXN2Q4YTJ-TKG7FZR3ZP7CNQYJ")

# fonction --------------------------------------------------
def get_data_from_anvil():
    rows = app_tables.produits.search()
    nb_rows = len(rows)
    print(nb_rows)
    return rows

# Main -------------------------------------------------------
rows = get_data_from_anvil()
for row in rows:
    print(row["code"],row["prestation"],row["visible"],row["tarif_1_jour"],row["tarif_1demi_jour"])
print("Fin de fichier")


