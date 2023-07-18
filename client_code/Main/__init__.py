from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..Mes_formations import Mes_formations
from ..Contact import Contact
from ..Pricing import Pricing
from ..Mon_CV import Mon_CV


class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(Home(), full_width_row=True)
    bt = Label(align="center", bold=False, foreground="white", background="b", text="Essai", role="raised", tag="", )
    self.column_panel_1.add_component(bt)
    bt.enabled = True
    
  def contact_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
     
    self.content_panel.add_component(Contact(), full_width_row=True)

  def home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Home(), full_width_row=True)

  def bottom_contact_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form(self)
    self.contact_link_click()

  def pricing_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Pricing(), full_width_row=True)

  def acceuil_link_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    open_form(self)
    self.content_panel.add_component(Home(), full_width_row=True)
      
  def mes_formations_link_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Mes_formations(), full_width_row=True)

  def mon_cv_link_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    open_form(self)  
    self.content_panel.add_component(Mon_CV(), full_width_row=True)

  def test_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Form1(), full_width_row=True)



 







