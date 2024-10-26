import anvil.server
# Pour le calcul de l'heure en France
from anvil import *  #pour les alertes
from datetime import datetime
import anvil.tz



#Get the time now, local time.
def french_zone_time():
    date_time = datetime.now(anvil.tz.tzlocal()) #recup browser time
    print(type(date_time))
    print(date_time)
    return date_time
