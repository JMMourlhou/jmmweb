from ._anvil_designer import ContactTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Contact(ContactTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #TODO: put items in designer
    self.topic_drop.items = ['Question', 'Besoins', 'Tarif', 'Site web', 'Autre']

  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.name_box.text
    email = self.email_box.text
    topic = self.topic_drop.selected_value
    message = self.message_area.text
    tel = self.tel_box.text
    check = False
    """self.checkbox_assigned.checked = True"""
    if self.check_box_1.checked == True:
      check = True
    if name and email and topic and message and tel:
      anvil.server.call('add_contact_info', name, tel, email, topic, message, check)
      
      alert("Message envoyé, merci!")
      self.name_box.text = ""
      self.email_box.text = ""
      self.tel_box.text = ""
      self.topic_drop.selected_value = None
      self.message_area.text = ""
      self.check_box_1.ckecked = False
    else:
      alert("Remplissez ce formulaire entierrement avant de l'envoyer !")

    #Return to acceuil  
    self.card_1.clear()
    open_form('Main')
    #self.content_panel.add_component(Home(), full_width_row=True)






