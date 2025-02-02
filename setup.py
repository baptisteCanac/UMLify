import tkinter as tk
from tkinter import ttk

from Config import Config

window = tk.Tk()
window.geometry('300x200')
window.title('configuration')

usages_supportes = ["Java", "Html"]

def langage_choisit(choix):
	# écrire dans le fichier de configuration le bon langage
	fichier = open('config.txt', 'w')
	fichier.write(choix)
	fichier.close()

	# update la classe config
	Config().update_config()

def close_setup():
	window.destroy()

titre = tk.Label(text="Configuration")

choix = ttk.Combobox(window, values=usages_supportes)
choix.current(0)

choix.bind("<<ComboboxSelected>>", lambda e: langage_choisit(choix.get()))

close_button = tk.Button(window, text="Fermer et valider mon setup", command=close_setup)

titre.pack()
choix.pack()
close_button.pack()

window.mainloop()