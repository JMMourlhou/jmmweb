import anvil.server
# Pour le calcul de l'heure en France
from anvil import *  #pour les alertes
import anvil.tz
from datetime import datetime
import pytz

#Get the time now, local time.
def french_zone_time():
    #date_time = datetime.now(anvil.tz.tzlocal()) #recup browser time
    tz = pytz.timezone('Europe/Paris')
    date_time = datetime.now(tz=tz)
    return date_time
