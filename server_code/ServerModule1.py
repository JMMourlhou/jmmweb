import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables

import anvil.files
from anvil.files import data_files

"""
**************************************************** LECTURE FICHIER CSV EN BGT 
"""
@anvil.server.background_task
def csv_file_reader(csv_file):
    f = open(data_files[csv_file.name])    # csv_file est : file du file loader. RAJOUTER .name ici pour obtenir on nom
    x = True
    nb = 0 # Nb de mails ajoutés
    print("Ouverture du fichier")
    while x:
        ligne = []
        text=f.readline()  # lecture  1 ligne
        if not text:                                        # FIN DE FICHIER TEXT           #rep = rep + dernier_caract
            print('Fin du fichier')
            return('Fin du fichier',nb)
        
        # création d'une liste, à partir du séparateur ";" (CSV file)
        ligne = text.split(';')
        
        #extraction d'1 fichier créé pour INFO COLL 
        col1=ligne[0]                 # extraction du type de mail ex: 
        col2=ligne[1]                 # extraction prestation
        # traitement True/False
        col3=ligne[2]                 # extraction TRUE FALSE
        
        col4=ligne[3]                 # extraction du tarif 1 jour
        col5=ligne[4]                 # extraction du tarif 1 jour


        """
        # je recherche si un doublon existe déjà
        row = app_tables.stagiaires_histo.get(code=col1)
        if not row:                             # mail innexistant, je l'ajoute                   
            nb += 1
            app_tables.stagiaires_histo.add_row(
                                                code=col1,               # code  num
                                                prestation=col2,         # prestation   tesxt
                                                visible=col3,            # visible ? True, false
                                                tarif_1_jour=col4,       # text
                                                tarif_1demi_jour=col5    # text
                                            )
        """
        
@anvil.server.callable
def run_bg_task_csv_reader(csv_file):
    task = anvil.server.launch_background_task('csv_file_reader',csv_file)
    return task
