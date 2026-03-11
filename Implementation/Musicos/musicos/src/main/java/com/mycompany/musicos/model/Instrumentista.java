package com.mycompany.musicos.model;

// DIP: depende de Instrumento (abstracción de datos), no de implementaciones concretas
// LSP: puede usarse donde se espera un Musico
public class Instrumentista extends Musico {

    private Instrumento instrumento;
    private int calidad; // 1-10

    public Instrumentista(String nombre, int edad, Instrumento instrumento, int calidad) {
        super(nombre, edad);
        this.instrumento = instrumento;
        this.calidad = calidad;
    }

    public Instrumento getInstrumento() {
        return instrumento;
    }

    public int getCalidad() {
        return calidad;
    }

    @Override
    public void tocar() {
        System.out.println(nombre + " está tocando " + instrumento.getNombre()
                + " con calidad " + calidad + "/10.");
    }

    @Override
    public void afinar() {
        System.out.println(nombre + " está afinando el " + instrumento.getNombre() + ".");
    }

    @Override
    public String presentarse() {
        return super.presentarse() + " Toco el " + instrumento.getNombre() + ".";
    }
}