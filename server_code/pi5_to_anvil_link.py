import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# lecture de la table Produits chez Anvil et écriture sur tables locales
def open_anvil_connection():
    anvil.server.connect("server_X4KQFEN7FOJZABUTXN2Q4YTJ-TKG7FZR3ZP7CNQYJ")
    liste_produits = produits_reading()
    anvil.server.disconnect() # déconnexion d'Anvil
    produits_writing(liste_produits)

def produits_reading():
    # table produits
    liste_produits = app_tables.produits.search()
    print("Produits:")
    for row in liste_produits:
        code = row["code"]
        prestation = row["prestation"]
        tarif_1_jour = row["tarif_1_jour"]
        tarif_1demi_jour = row["tarif_1demi_jour"]
        visible = row["visible"]
        
        print(f"{code}, {prestation}, {tarif_1_jour}, {tarif_1demi_jour}, {visible}")
    return liste_produits

def produits_writing(liste_produits):
    for row in liste_produits:
        app_tables.produits.add_row(
                                    code =             row["code"],
                                    prestation =       row["prestation"],
                                    tarif_1_jour =     row["tarif_1_jour"],
                                    tarif_1demi_jour = row["tarif_1demi_jour"],
                                    visible =          row["visible"]
                                   )
    

        

    
        
