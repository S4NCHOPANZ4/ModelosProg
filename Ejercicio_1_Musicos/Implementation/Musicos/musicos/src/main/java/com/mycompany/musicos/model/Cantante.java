package com.mycompany.musicos.model;

// LSP: puede usarse donde se espera un Musico sin romper el comportamiento
public class Cantante extends Musico {

    private String tessitura; // ej: soprano, tenor, barítono

    public Cantante(String nombre, int edad, String tessitura) {
        super(nombre, edad);
        this.tessitura = tessitura;
    }

    public String getTessitura() {
        return tessitura;
    }

    @Override
    public void tocar() {
        System.out.println(nombre + " está cantando (" + tessitura + ").");
    }

    @Override
    public void afinar() {
        System.out.println(nombre + " está afinando su voz.");
    }

    @Override
    public String presentarse() {
        return super.presentarse() + " Soy cantante " + tessitura + ".";
    }
}