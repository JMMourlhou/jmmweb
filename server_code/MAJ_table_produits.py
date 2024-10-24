import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# MAJ Table Produits

# Destruction d'une ligne table produits
@anvil.server.callable
def destruction(row):
    row.delete()
