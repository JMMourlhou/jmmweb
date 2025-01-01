import anvil.secrets
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

import anvil.server
#anvil.server.connect("server_X4KQFEN7FOJZABUTXN2Q4YTJ-TKG7FZR3ZP7CNQYJ")

# lecture de la table Produits chez Anvil et écriture sur tables locales
@anvil.server.callable
def up_link_connection():
    liste_produits = app_tables.produits.search()
    nb_rows = len(liste_produits)
    #anvil.server.disconnect() # déconnexion d'Anvil

    # écriture table produits
    for row in liste_produits:
        app_tables.produits.add_row(
                                    code =             row["code"],
                                    prestation =       row["prestation"],
                                    tarif_1_jour =     row["tarif_1_jour"],
                                    tarif_1demi_jour = row["tarif_1demi_jour"],
                                    visible =          row["visible"]
                                   )
    return(nb_rows)




    

        

    
        
