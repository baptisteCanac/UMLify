from PyQt6.QtWidgets import QApplication, QTextEdit, QMainWindow, QMenu, QMessageBox, QScrollArea, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QMouseEvent  
from PyQt6.QtGui import QAction

import re
import os

def supprimer_doublons(liste):
	return list(set(liste))

def supprimer_entre_parentheses(chaine): # supprime tout ce qui est entre parenthese ainsi qu'elles même
	return re.sub(r'\(.*?\)', '', chaine)

def remove_space(liste): # enlever les espaces dans toutes les str d'une liste
	res = []
	for el in liste:
		if el.strip() != "":  # Vérifie que la chaîne n'est pas vide après suppression des espaces
			res.append(el.lstrip())  # Supprime les espaces au début de la chaîne
	return res

def remove_empty_val(liste):
	res = []

	for el in liste:
		if el != "":
			res.append(el)

	return res

from graphviz import Digraph

def assigner_niveaux(data):
    """Détermine un niveau pour chaque classe en fonction des dépendances"""
    niveau_classes = {}
    
    # Assigner un niveau de base (0) à toutes les classes
    for classe in data["classes"]:
        niveau_classes[classe] = 0
    
    # Augmenter le niveau pour chaque classe qui est référencée par une autre
    for _, _, classe in data["variables"] + data["methodes"]:
        if classe in niveau_classes:
            niveau_classes[classe] += 1
    
    return niveau_classes

compteur_nb_export = 0

def exportPOO(data, window):
    dossier_resultat = "resultat"
    os.makedirs(dossier_resultat, exist_ok=True)

    for i, classe in enumerate(data["classes"], start=1):
        # Créer un nouveau diagramme pour chaque classe
        dot = Digraph(comment=f"Diagramme UML - {classe}", strict=True)
        dot.attr(rankdir="TB")  # Disposition du diagramme de haut en bas

        # Ajouter la classe principale
        dot.node(classe, classe, shape="box")

        # Ajouter les variables associées à la classe
        for var in data["variables"]:
            if var[2] == classe:
                dot.node(var[0], f"- {var[0]}: {var[1]}", shape="ellipse")
                dot.edge(var[2], var[0])

        # Ajouter les méthodes associées à la classe
        for meth in data["methodes"]:
            if meth[2] == classe:
                dot.node(meth[0], f"+ {meth[0]} : {meth[1]}", shape="ellipse")
                dot.edge(meth[2], meth[0])

        # Enregistrer chaque diagramme sous un nom unique
        filename = os.path.join(dossier_resultat, f"diagramme_{classe}")
        dot.render(filename, format="png", cleanup=True)
        print(f"Diagramme UML généré : {filename}.png")

    QMessageBox.information(window, "Succés", "Vos fichiers UML ont été créés avec succés")
