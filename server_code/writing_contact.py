import anvil.secrets
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
from .french_zone import french_zone_time

@anvil.server.callable
def add_contact_info(name,tel, email, topic, message, check):
  if check is True:  
    time = french_zone_time()
    app_tables.contact.add_row(name=name, tel=tel, email=email, topic=topic, message=message, date_time=time)
    sov = "A accepté d'être référencé."   
  else:
        sov = "N'a pas accepté d'être référencé."
       
  anvil.email.send(to="jmmourlhou@gmail.com",                            # avait mis 'jmweb34.net'
                   from_name="Contact/Site Web 'jmweb34.net'", 
                   subject="Nouveau contact Web",
                   
                   text=f"Nouveau contact Web de {name}\n {tel}\n ({email})\n Sujet: {topic}\n Msg: {message}\n {sov}")