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
