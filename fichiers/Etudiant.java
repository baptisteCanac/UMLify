package com.mycompany.td01;

public class Etudiant{
    final private Integer numero;
    final private String nom;
    private String prenom;
    public Cours majeur;
    public Cours mineur;
    private String mention;
    
    public Etudiant(Integer numero, String nom, String prenom){
        this.numero = numero;
        this.nom = nom;
        this.prenom = prenom;
    }
    
    public Etudiant(Integer numero, String nom, String prenom, String mention, Cours majeur, Cours mineur){
        this.numero = numero;
        this.nom = nom;
        this.prenom = prenom;
        this.mention = mention;
        this.majeur = majeur;
        this.mineur = mineur;
    }
    
    public void SInscrire(Cours maj, Cours min){
        this.majeur = maj;
        this.mineur = min;
    }
    
    public void SInscrire(String intituleMaj, Integer creditsMaj, String intituleMin, Integer creditsMin){
        this.majeur = new Cours(intituleMaj, creditsMaj);
        this.mineur = new Cours(intituleMin, creditsMin);
    }
    
    public Boolean memeCours(){
        
        return false;
    }
    
    /*public void SInscrire(String intituleMaj, Integer creditsMAJ, String intituleMin, Integer creditsMin){
        this.majeur = intituleMaj;
        this.mineur = intituleMin;
    }*/
    
    public String mesProfs(){
        return majeur.getEns().getNom() + " " + mineur.getEns().getNom();
    }
    
    public Integer getNumero(){
        return this.numero;
    }
    
    public String getNom(){
        return this.nom;
    }
    
    public String getPrenom(){
        return prenom;
    }
    public void setPrenom(String nouvelleVal){
        this.prenom = nouvelleVal;
    }
    
    public Cours getMajeur(){
        return majeur;
    }
    public void setMajeur(Cours majeur){
        this.majeur = majeur;
    }
       
    public Cours getMineur(){
        return mineur;
    }
    public void setMineur(Cours mineur){
        this.mineur = mineur;
    }
    
    public String getMention(){
        return mention;
    }
    public void setMention(String mention){
        this.mention = mention;
    }
}