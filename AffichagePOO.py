from PyQt6.QtWidgets import QApplication, QTextEdit, QMainWindow, QMenu, QMessageBox, QScrollArea, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QMouseEvent  
from PyQt6.QtGui import QAction

import sys
from utilities import *

class DraggableTextEdit(QTextEdit):
    """Une QTextEdit déplaçable avec la souris"""
    def __init__(self, text="", height=150, parent=None):
        super().__init__(parent)
        self.setText(text)  
        self.setFixedSize(250, height)
        self.setStyleSheet("background-color: white; border-radius: 5px; padding: 5px; color: black")

        self._drag_active = False
        self._drag_position = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_active = True
            self._drag_position = event.globalPosition().toPoint() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._drag_active and event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self._drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._drag_active = False
        event.accept()

class AffichagePOO(QMainWindow):
    """Affiche les classes sous forme de QTextEdit avec une barre de défilement horizontale et un espacement vertical"""
    def __init__(self, a_afficher):
        super().__init__()

        self.a_afficher = a_afficher

        self.setWindowTitle("UML")
        self.setGeometry(100, 100, 800, 400)

        # Créer une zone de défilement
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)  # Activer le défilement horizontal
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # Désactiver le défilement vertical

        # Widget principal qui contient tout
        self.central_widget = QWidget()
        self.scroll_area.setWidget(self.central_widget)

        # Layout horizontal contenant des colonnes de texte
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setSpacing(20)  # Espace horizontal entre chaque colonne

        self.text_areas = []
        for i, classe in enumerate(a_afficher["classes"]):
            a_afficher_par_fenetre = {
                "classes": classe,
                "variables": [v for v in a_afficher['variables'] if v[2] == classe],
                "methodes": [m for m in a_afficher['methodes'] if m[2] == classe]
            }

            # Construction du texte affiché
            affichage = f"{a_afficher_par_fenetre['classes']}\n" + "-" * 36 + "\n"
            affichage += "\n".join(f"- {v[0]}: {v[1]}" for v in a_afficher_par_fenetre["variables"]) + "\n"
            affichage += "-" * 36 + "\n"
            affichage += "\n".join(f"+ {m[0]}: {m[1]}" for m in a_afficher_par_fenetre["methodes"])
            affichage += "\n" + "-" * 36

            # Calcul de la hauteur en fonction du nombre de lignes
            hauteur = max(150, (2 + len(a_afficher_par_fenetre["variables"]) + len(a_afficher_par_fenetre["methodes"])) * 24)

            # Layout vertical pour empiler les QTextEdit avec espace
            column_layout = QVBoxLayout()
            column_layout.setSpacing(20)  # Espacement vertical entre les QTextEdit

            text_area = DraggableTextEdit(affichage, height=hauteur, parent=self)
            column_layout.addWidget(text_area)
            self.text_areas.append(text_area)

            # Ajouter cette colonne au layout horizontal principal
            self.main_layout.addLayout(column_layout)

        # Définir la zone de défilement comme widget central
        self.setCentralWidget(self.scroll_area)

    def export_diagram(self):
        exportPOO(self.a_afficher, self)

    def contextMenuEvent(self, event):
        """Affiche un menu contextuel personnalisé au clic droit"""
        menu = QMenu(self)

        export_button = QAction("Exporter le diagramme", self)
        action_info = QAction("Informations", self)
        action_quit = QAction("Quitter", self)

        export_button.triggered.connect(self.export_diagram)
        action_info.triggered.connect(self.export_diagram)
        action_quit.triggered.connect(self.close)

        menu.addAction(export_button)
        menu.addAction(action_info)
        menu.addSeparator()
        menu.addAction(action_quit)

        menu.exec(event.globalPos())
