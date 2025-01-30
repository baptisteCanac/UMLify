import re

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