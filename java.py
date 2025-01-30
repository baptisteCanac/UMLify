import re
from utilities import *

import logging

logging.basicConfig(
	filename="logs/java.log",  # Nom du fichier de logs
	level=logging.INFO,   # Niveau de log minimum
	format="%(asctime)s - %(levelname)s - %(message)s",  # Format des logs
	datefmt="%Y-%m-%d %H:%M:%S"  # Format de la date
)

""" 
	S'occupe de l'analyxe syntaxique et sémantique du code
"""

class Java:
	def __init__(self, liste):
		self.fichiers = liste
		self.code_liste = []
		self.res = {
			"to_analyse": [], # fichiers convertit en liste
			"without_comment": [], # fichiers avec les commentaires enlevés
			"without_empty_val": [], # fichiers sans les valeurs nulles
			"without_space_in_val": [] # fichiers avec aucun espace dans les données
		}
		self.tempo_methodes = []
		self.resultat_analyse = {
			"package": [],
			"classes": [],
			"methodes": [],
			"signature_methodes": [],
			"variables": []
		}
		self.diagramme = {
			"titre": ""
		}
		self.clef_variables = ["Integer", "int", "String", "void", "boolean", "double", "float", "long", "short", "byte", "char"]
		self.modificateurs_acces = ["private", "public", "protected", "static", "final"]
		self.resultat_final = {
			"classes": self.resultat_analyse["classes"],
			"methodes": [],
			"variables": [] 
		}

	def afficher_res(self):
		self.resultat()
		for clef in self.resultat_analyse:
			print(clef + ":", self.resultat_analyse[clef], end="\n\n")

	def to_list(self, nom_fichier):
		res = []

		with open("fichiers/" + nom_fichier, 'r') as file:
			#ligne = file.readlines()
			for l in file:
				res.append(l.rstrip("\n"))

		return res

	def remove_comment(self, liste):
		debut_commentaire = "/*"
		debut_java_doc = "/**"
		fin_commentaire = "*/"

		res = []

		compteur_commentaire = 0

		for el in liste:
			if debut_commentaire in el or debut_java_doc in el:
				compteur_commentaire += 1

			if compteur_commentaire == 0:
				res.append(el)

			if fin_commentaire in el:
				compteur_commentaire -= 1

		return [re.sub(r'//.*', '', line).rstrip() for line in res]

	def code_to_liste(self, liste):
		"""
		Transforme le code donné en une liste sans commentaires ni chaines vides,
		prêt à être analysé
		procédé:
			- convertit toutes les lignes en une chaine de caractere
			- supprime les commentaires afin de ne garder que le code effectif
			cette partie créé des chaines vides dans la liste puisque si le contenu d'une chaine
			n'est uniquement que des commentaires alors l'element va rester mais vide alors:
			- supprimmer les chaines vides
		"""
		for fichier in self.fichiers:
			self.res["to_analyse"].append(self.to_list(fichier))

		for fichier in self.res["to_analyse"]:
			self.res["without_comment"].append(self.remove_comment(fichier))

		for fichier in self.res["without_comment"]:
			self.res['without_empty_val'].append(remove_empty_val(fichier))

		for fichier in self.res["without_empty_val"]:
			self.res["without_space_in_val"].append(remove_space(fichier))

	def extract_class_name(self, chaine):
		match = re.search(r'\bclass\s+(\w+)', chaine)
		return match.group(1) if match else None

	def extract_method_name(self, liste):
		method_names = []
		res = []

		pattern = re.compile(r'\b(?:public|private|protected)\s+(?:static\s+)?(?:<[^>]+>\s+)?(?:\w+\s+)?(\w+)\s*\(')
    
		for line in liste:
			match = pattern.search(line)
			if match:
				method_names.append(match.group(1))

		""" 
			Supprimer les constructeurs en supprimants les choses qui ressemblent
			à des methodes mais qui ont le même nom que des classes
		"""
		for el in method_names:
			if not any(el in nom_class for nom_class in self.resultat_analyse["classes"]):
				res.append(el)

		return supprimer_doublons(res)

	def extract_methods(self, liste):
		a_parse = []
		sans_parenthese = []
		clean = []
		res = []

		for el in liste:
			if any(methode in el for methode in self.tempo_methodes):
				a_parse.append(el)

		for el in a_parse:
			sans_parenthese.append(supprimer_entre_parentheses(el))

		for methode in sans_parenthese:
			methode = methode.replace("{", "")
			methode = methode.split()
			clean.append(methode)

		for i in range(len(clean)):
			res.append(((clean[i][-1]), clean[i][-2]))

		self.resultat_analyse["signature_methodes"] = clean

		return res

	def extract_var(self, lines):
		variable_types = {}
    
		# Regex pour capturer les déclarations de variables
		declaration_pattern = re.compile(r'\b(?:final\s+)?(?:private|public|protected)?\s*(\w+)\s+(\w+)\s*(?:=.*)?;')
    
		# Regex pour capturer les instanciations de variables avec 'new'
		instantiation_pattern = re.compile(r'(\w+)\s+(\w+)\s*=\s*new\s+(\w+)')
    
		# Regex pour capturer les affectations de valeurs aux variables
		assignment_pattern = re.compile(r'this\.(\w+)\s*=\s*(\w+);')
    
		# Regex pour ignorer les lignes contenant 'return'
		return_pattern = re.compile(r'\breturn\b')
    
		for line in lines:
			line = line.strip()
        
			# Ignorer les retours de méthode
			if return_pattern.search(line):
				continue
        
        	# Vérifier les déclarations explicites
			decl_match = declaration_pattern.search(line)
			if decl_match:
				var_type, var_name = decl_match.groups()
				variable_types[var_name] = var_type
				continue
        
        	# Vérifier les instanciations avec 'new'
			inst_match = instantiation_pattern.search(line)
			if inst_match:
				declared_type, var_name, assigned_type = inst_match.groups()
				variable_types[var_name] = declared_type
				continue
        
        	# Vérifier les affectations de valeurs aux variables
			assign_match = assignment_pattern.search(line)
			if assign_match:
				var_name, assigned_value = assign_match.groups()
            
				# Vérifier si la valeur assignée est déjà une variable connue
				if assigned_value in variable_types:
					variable_types[var_name] = variable_types[assigned_value]
            
		return list(variable_types.items())

	def analyse_data(self, liste):
		""" 
			procédé:
			- récupération du nom du package qui servira de titre au diagrame UML
				- ce package est toujours la premiere ligne de code
				- récupération et mettre ensemble toutes les lignes qui concernent les packages
		"""

		methodes_a_trier = []
		chercher_var = []

		for fichier in liste:
			for el in fichier:
				if "package" in el: # extraire les packages
					self.resultat_analyse["package"].append(el)
				elif "class" in el and ("public" in el or "private" in el): # extraire class
					self.resultat_analyse["classes"].append(self.extract_class_name(el))
				elif ("public" in el or "private" in el) and any(mot_clef in el for mot_clef in self.clef_variables) and "(" in el and ";" not in el:
					methodes_a_trier.append(el)
				else:
					chercher_var.append(el)

		for el in self.extract_method_name(methodes_a_trier):
			self.tempo_methodes.append(el)

		self.resultat_analyse["methodes"] = self.extract_methods(methodes_a_trier)

		self.resultat_analyse["variables"] = self.extract_var(chercher_var)

		return self.resultat_analyse

	def remove_comment_slash(self, liste):
		return [re.sub(r'//.*', '', liste).rstrip() for line in liste]

	def resultat(self):
		"""
		Récupère le code dans les fichiers fournis et pratique une analyse syntaxique
		"""
		self.code_to_liste(self.fichiers)
		return self.analyse_data(self.res["without_space_in_val"])

		for el in tempo_methodes:
			self.clef_variables.append(el)

	def trouver_methode_par_classes(self):
		for i in range(len(self.fichiers)):
			data = self.to_list(self.fichiers[i])
			#print(data)
			for compteur in range(len(self.resultat_analyse["signature_methodes"])):
				find_signature = ""

				for el in self.resultat_analyse["signature_methodes"][compteur]:
					find_signature += str(el)
					find_signature += " "

				if any(find_signature[:-1] in donnee for donnee in data):
					#print(self.resultat_analyse["signature_methodes"][compteur], "trouvée")
					#print(self.resultat_analyse["methodes"][compteur][0], self.resultat_analyse["methodes"][compteur][1])
					self.resultat_final["methodes"].append((self.resultat_analyse["methodes"][compteur][0], self.resultat_analyse["methodes"][compteur][1], self.fichiers[i][:-5]))

	def trouver_var_par_classe(self):

		for i in range(len(self.fichiers)):
			data = self.to_list(self.fichiers[i])

			for compteur in range(len(self.resultat_analyse["variables"])):
				if any(str(self.resultat_analyse['variables'][compteur][0] + " ") in el for el in data) and any(str(self.resultat_analyse['variables'][compteur][1] + " ") in el for el in data):
					#print(self.resultat_analyse['variables'][compteur], "trouvé")
					self.resultat_final['variables'].append((self.resultat_analyse['variables'][compteur][0], self.resultat_analyse['variables'][compteur][1], self.resultat_analyse['classes'][i]))

	def resultat_a_afficher(self):
		"""
		Fonction a appeller qui renvoie dans un dictionnaire:
			- toutes les classes trouvées suite à l'analyse,
			- toutes les méthodes trouvées suite à l'analyse au format (nom_de_la_methode, type_de_renvoie_de_la_methode, classe_a_laquelle_appartiens_la_methode),
			- toutes les variables trouvées suite à l'analyse au format (nom_de_la_variable, type_de_la_variable, classe_a_laquelle_appartiens_la_variable)
		"""
		self.resultat()
		self.trouver_methode_par_classes()
		self.trouver_var_par_classe()
		return self.resultat_final
