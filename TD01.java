/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.td01;

/**
 *
 * @author baptiste
 */
public class TD01 {
    public static void main(String[] args) {
        Enseignant jfv = new Enseignant("Viaud", "Jean-François");
        Enseignant csj = new Enseignant("Saint-Jean", "Christophe");
        Enseignant rm = new Enseignant("Mullot", "Remi");
        
        Cours cours_java = new Cours("programmation_java", 3);
        cours_java.setEns(jfv);
        
        Cours cours_python = new Cours("Programmation_python", 3);
        cours_python.setEns(csj);
        
        Cours cours_sys_exploitation = new Cours("Systemes d'exploitation", 3);
        cours_sys_exploitation.setEns(rm);
        
        Etudiant bc;
        bc = new Etudiant(1, "Canac", "Batiste", "INFORMATIQUE", cours_java, cours_python);
        bc.setPrenom("Baptiste");
        System.out.println(bc.mesProfs());
        
        
        //System.out.println(jfv.getPrenom());
        
        //Etudiant mathilde = new Etudiant(2, "VACHON", "MATHILDE", "INFORMATIQUE", cours_java, cours_archi);
        
        //jfv.SInscrire(cours_java, cours_python);
        //jfv.SInscrire(cours_java.getIntitule(), cours_java.getECTS, cours_python.getIntitule(), cours_python.getECTS());
        
        /*String affichage;
        affichage = "Nom de l'étudiant : " + jfv.getNom();
        System.out.println(affichage);
        System.out.println(jfv.toString()); *//* = System.out.println(jfv) puisque .toString()
        se met automatiquement dans un println */
    }
}
