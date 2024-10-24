from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..Mes_formations import Mes_formations
from ..Contact import Contact
from ..Produits import Produits
from ..Produits_maj import Produits_maj
from ..Mon_CV import Mon_CV


class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(Home(), full_width_row=True)

    """ -------------------------    Add dynamicly button bt (contact) and space ----------------------------------"""
    #bt = Button(align="center", text="Contact", bold=False, foreground="white", background="##FF000000", enabled=True, role="raised", tag="")
    bt = Button(align="center", text="Contact", bold=False, foreground="white", background="#5396BC", enabled=True, role="raised", tag="")
    self.column_panel_1.add_component(bt)
      
    # Creation of space below the last button  
    
    space = Spacer(height=100, visible=True)
    self.column_panel_1.add_component(space)
      
    bt.set_event_handler('click',self.bt_click)
          
  def bt_click(self, **event_args):
    """This method is called when the bt button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Contact(), full_width_row=True)

    """ ---------------------------------  END --------------------------------------------------"""
    
  def home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Home(), full_width_row=True)

  def bottom_contact_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form(self)
    self.contact_link_click()

  def products_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Produits(), full_width_row=True)

  def acceuil_link_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    open_form(self)
    self.content_panel.add_component(Home(), full_width_row=True)
      
  def mes_formations_link_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Produits(), full_width_row=True)

  def mon_cv_link_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    open_form(self)  
    self.content_panel.add_component(Mon_CV(), full_width_row=True)

  def test_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Form1(), full_width_row=True)

  def image_1_mouse_down(self, x, y, button, keys, **event_args):
      """This method is called when a mouse button is pressed on this component"""
      self.content_panel.clear()
      self.content_panel.add_component(Produits_maj(), full_width_row=True)



 







