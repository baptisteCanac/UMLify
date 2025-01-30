package com.mycompany.td01;

public class TD01 {
    public static void main(String[] args) {
        Enseignant enseignant_1 = new Enseignant("Dupont", "Jean");
        Enseignant enseignant_2 = new Enseignant("Martin", "Sophie");
        Enseignant enseignant_3 = new Enseignant("Lemoine", "Alexandre");
        
        Cours cours_algorithme = new Cours("Algorithmique avancée", 4);
        cours_algorithme.setEns(enseignant_1);
        
        Cours cours_reseau = new Cours("Administration réseau", 5);
        cours_reseau.setEns(enseignant_2);
        
        Cours cours_bd = new Cours("Bases de données", 4);
        cours_bd.setEns(enseignant_3);
        
        Etudiant etudiant;
        etudiant = new Etudiant(42, "Morel", "Camille", "Génie Logiciel", cours_algorithme, cours_reseau);
        etudiant.setPrenom("Camila");
        System.out.println(etudiant.mesProfs());
    }
}
