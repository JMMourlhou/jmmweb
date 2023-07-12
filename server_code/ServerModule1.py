import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime


@anvil.server.callable
def add_contact_info(name,tel, email, topic, question, check):
  
  if check == True:  
    app_tables.contact.add_row(name=name, tel=tel, email=email, topic=topic, question=question, time=datetime.now())
    sov = "A accepté d'être référencé."   
  else:
        sov = "N'a pas accepté d'être référencé."
       
  anvil.email.send(from_name="Contact/Site Web 'JMM Mpt secourisme'", 
                   subject="Nouveau contact Web",
                   
                   text=f"Nouveau contact Web de {name}\n {tel}\n ({email})\n Sujet: {topic}\n Msg: {question}\n {sov}")