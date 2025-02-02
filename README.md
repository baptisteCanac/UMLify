# UMLify

**UMLify** est un outil qui analyse automatiquement le code source d'un projet pour en générer un **diagramme UML détaillé**.

---

## Principe de fonctionnement
1. **Déposez tous vos fichiers** dans le dossier prévu à cet effet.
2. **Lancez le script** principal.

UMLify effectue une **analyse syntaxique et sémantique** du code en fonction des paramètres définis dans le fichier de configuration.

Il génère ensuite un **affichage moderne et épuré** basé sur les résultats de l'analyse.

- avec un clic droit dans une zone vide, vous pourrez exporter votre diagramme en plusieurs fichiers (voir partie export)

---

## Export

Avec un clic droit dans un endroit vide vous aurez accés à la fonction d'export de votre diagramme
<img width="802" alt="Capture d’écran 2025-02-02 à 15 44 06" src="https://github.com/user-attachments/assets/b3ec9b20-7870-49fe-9e9d-6f6923ed8bf4" />

Un fois cliqué retrouvez votre résultat dans le dossier ```resultat```

Avec un fichier Cours.java:
```java
package com.mycompany.td01;

public class Cours{
    final private String intitule;
    private Integer ECTS;
    private Enseignant ens;
    
    public Cours(String intitule, Integer credits){
        this.intitule = intitule;
        this.ECTS = credits;
    }
    
    public String getIntitule(){
        return intitule; 
    }
    
    public Integer getECTS(){
        return ECTS;
    }
    public void setECTS(Integer ECTS) {
        this.ECTS = ECTS;
    }
    
    public Enseignant getEns(){
        return ens;
    }
    public void setEns(Enseignant ens){
        this.ens = ens;
    }
    
    public String toString(){
        return "Cours{" + "intitule=" + intitule + ", ECTS=" + ECTS + "}";
    }
}
```

UMLify va renvoyer comme résultat visuel dans l'application:

<img width="253" alt="Capture d’écran 2025-02-02 à 15 50 12" src="https://github.com/user-attachments/assets/0e8da09c-5b5a-47a8-8f7d-63d069f13157" />

Et comme rendu d'export:

![diagramme_Cours](https://github.com/user-attachments/assets/2e824a50-940d-4dc1-920c-5613d0b24b53)

---

## 🛠️ Langages supportés
UMLify supporte **uniquement les fichiers Java** pour le moment.

**À venir** :
- Ajout du support pour **HTML**.

---

## Installation
1. **Téléchargez** le fichier source.
2. **Placez** tous vos fichiers de code dans le dossier **`fichiers`**.
   (Des fichiers y sont deja présents mais ils ne servent que de démo)
3. Vérifiez que tous les modules sont installés sur votre machine:
   - os
   - logging
   - sys
   - time
   - threading
   - PyQt6
   - tkinter

     Vous pouvez installer les modules manquants avec la commande ```pip3 install nom_du_module```
   
   - graphviz qui nécessite non seulement une installation avec ```pip3``` mais aussi une installation plus classique en l'ajoutant au PATH

5. 🖥**Lancez le script** ```main.py``` dans le terminal:

Exemple de commande pour lancer le fichier ```main.py``` dans le terminal:
```sh
python3 main.py
```
---

## 📞 Contact
Si vous souhaitez me contacter ou si vous trouvez un bug, n'hésitez pas ! Je répondrai au plus vite. 
