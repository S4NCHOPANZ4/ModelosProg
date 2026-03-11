package com.mycompany.musicos.model;

import com.mycompany.musicos.enums.TipoInstrumento;

// SRP: solo representa un instrumento musical
public class Instrumento {

    private String nombre;
    private TipoInstrumento tipo;
    private String marca;

    public Instrumento(String nombre, TipoInstrumento tipo, String marca) {
        this.nombre = nombre;
        this.tipo = tipo;
        this.marca = marca;
    }

    public String getNombre() {
        return nombre;
    }

    public TipoInstrumento getTipo() {
        return tipo;
    }

    public String getMarca() {
        return marca;
    }

    @Override
    public String toString() {
        return marca + " " + nombre + " (" + tipo + ")";
    }
}