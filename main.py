import os
import re
from PyQt6.QtWidgets import QApplication, QTextEdit, QMainWindow
from PyQt6.QtCore import Qt, QPoint
import sys
import logging
import time
import threading

from utilities import *
from java import Java
from AffichagePOO import *
from Config import Config

info = {
	"pour:": "Java",
	"version": 1.0
}

DOSSIER = '/Users/baptiste/Documents/dev/UMLify/fichiers' # dossier contenant tout le code à analyser
UTILISATION = Config().getLangage()

fichiers_trouves = {
	"Java": [],
	"Python": [],
	"Html": []
}

def lister_fichiers_par_extension(repertoire):    
    liste = []

    for racine, repertoires, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            if fichier.endswith(".java"):
                fichiers_trouves["Java"].append(os.path.join(fichier))
            elif fichier.endswith(".py"):
            	fichiers_trouves["Python"].append(os.path.join(fichier))
            elif fichier.endswith(".html"):
            	fichiers_trouves["Html"].append(os.path.join(fichier))

lister_fichiers_par_extension(DOSSIER)

done = False

def spinner(affichage):
	while not done:
		for char in "-\\|/":
			if affichage == "fichiers":
				sys.stdout.write(f"\rAnalyse des fichiers... {char}")
				sys.stdout.flush()
				time.sleep(0.1)
			elif affichage == "affichage":
				sys.stdout.write(f"\rAffichage des resultats dans une fenetre... {char}")
				sys.stdout.flush()
				time.sleep(0.1)

t = threading.Thread(target=spinner, args=("fichiers",))
t.start()

if fichiers_trouves[UTILISATION] != []:
	if UTILISATION == "Java":
		logging.basicConfig(
			filename="logs/java.log",  # Nom du fichier de logs
			level=logging.INFO,   # Niveau de log minimum
			format="%(asctime)s - %(levelname)s - %(message)s",  # Format des logs
			datefmt="%Y-%m-%d %H:%M:%S"  # Format de la date
		)
		logging.info("Lancement de l'application pour Java")

		try:
			donnees = Java(fichiers_trouves[UTILISATION]).resultat_a_afficher()
			logging.info("Fichiers Java traités avec succés")
			done = True
			sys.stdout.write("\rFichiers traités avec succés\n")
			sys.stdout.flush()
			t.join()
		except:
			logging.error("Les fichiers Java n'ont pas pus être traités")

		try:
			done = False
			t = threading.Thread(target=spinner, args=("affichage",))
			t.start()
			logging.info("Fenêtre lancée")
			app = QApplication(sys.argv)

			fenetre = AffichagePOO(donnees)
			fenetre.show()
			done = True
			sys.stdout.write("\rFichiers affichés avec succés\n")
			sys.stdout.flush()
		except:
			logging.error("L'application n'a pas pu être lancée")
		
		logging.info("Fermeture de l'application")
		sys.exit(app.exec())
else:
	print("Dossier", DOSSIER, "vide ou ne contenant pas de fichiers", UTILISATION + ".")
	print("Modifiez vos préférences avec le fichier setup.py afin de modifier le language voulu")
	print("l'application à trouvé les fichiers suivant dans l'arborescence:", fichiers_trouves)
	print("Info de l'app:", info)