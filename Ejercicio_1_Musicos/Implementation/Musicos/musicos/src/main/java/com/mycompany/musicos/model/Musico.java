package com.mycompany.musicos.model;

import com.mycompany.musicos.interfaces.Ejecutar;

// OCP: abierta para extensión (subclases), cerrada para modificación
// SRP: solo gestiona datos y comportamiento base de un músico
public abstract class Musico implements Ejecutar {

    protected String nombre;
    protected int edad;

    public Musico(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    // Las subclases definen cómo se presentan (OCP)
    public String presentarse() {
        return "Hola, soy " + nombre + " y tengo " + edad + " años.";
    }

    // Obligadas a implementar tocar() y afinar() de Ejecutar
}