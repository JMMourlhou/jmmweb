import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# Pour le calcul de l'heure en France
from anvil import *  #pour les alertes
import anvil.tz
from datetime import datetime

#Get the time now, local time.
def french_zone_time():
    date_time = datetime.now(anvil.tz.tzlocal()) #recup browser time
    return date_time
