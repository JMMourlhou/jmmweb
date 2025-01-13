import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables

import anvil.files
from anvil.files import data_files

"""
**************************************************** LECTURE FICHIER CSV (BGTask à prévoir)
"""
@anvil.server.callable
def csv_file_reader(csv_file):
    f = open(data_files[csv_file.name])    # csv_file est : file du file loader. RAJOUTER .name ici pour obtenir son nom
    x = True
    nb = 0 # Nb de lignes ajoutés
    print("Ouverture du fichier")
    while x:
        ligne = []
        text=f.readline()  # lecture en-tête, ligne 1
        text=text.strip()  # on retire les espaces éventuels
        print(text)
        if not text:                                        # FIN DE FICHIER TEXT           #rep = rep + dernier_caract
            print('Fin du fichier')
            break      # on sort de la boucle while
            
        if nb==0:
            nb += 1
            continue   # en tête non lu, passe à la prochaine itération du while
        
        # création d'une liste, à partir du séparateur "," (CSV file en sortie de l'IDE d'anvil)
        ligne=[]
        new_ligne = text.split(',')
        for element in new_ligne:
            ligne.append(element.strip('"'))   

        
        #ligne = [elem.strip('"') for elem in text.split(',')]
        
        col0=ligne[0]                 # extraction de l'id sous la forme [xxx,xxx] donc 2 col de lues
        col1=ligne[2]                 # extraction du code produit 
        col2=ligne[3]      # extraction prestation
        # traitement True/False
        col=ligne[4]                 # extraction 1 ou 0
        if col == "1":
            col3 = True
        else:
            col3 = False
        
        col4=ligne[5]     # extraction du tarif 1 jour
        col5=ligne[6]     # extraction du tarif 1 jour
        
        msg = f"ligne {nb} : {col1} - {col2} - {col3} - {col4} - {col5}"
        print(msg)
        print()
        # je recherche si un doublon existe déjà
        row = app_tables.produits.get(code=int(col1))
        if not row:                             # mail innexistant, je l'ajoute                   
            nb += 1
            app_tables.produits.add_row(
                                        code=int(col1),          # code  num
                                        prestation=col2,         # prestation   tesxt
                                        visible=col3,            # visible ? True, false
                                        tarif_1_jour=col4,       # text
                                        tarif_1demi_jour=col5    # text
                                        )
        
        
    return('Fin du fichier',nb-1)

        
