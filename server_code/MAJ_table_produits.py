import anvil.files
from anvil.files import data_files
import anvil.tables as tables
from anvil.tables import app_tables
import anvil.server

# MAJ Table Produits, appelé par Poduits_maj et son P.iemTemplate1

# Destruction d'une ligne table produits
@anvil.server.callable
def destruction(row):
    row.delete()

# add d'une ligne table produits
@anvil.server.callable
def add(code, presta, tarif1, tarif1demi, visible):
    app_tables.produits.add_row(
                                code = int(code),
                                prestation = presta,
                                tarif_1_jour = tarif1,
                                tarif_1demi_jour = tarif1demi,
                                visible = visible
                                )

# modif d'une ligne table produits
@anvil.server.callable
def modif(row, code, presta, tarif1, tarif1demi, visible):
    row.update(
                                code = int(code),
                                prestation = presta,
                                tarif_1_jour = tarif1,
                                tarif_1demi_jour = tarif1demi,
                                visible = visible
                                )


