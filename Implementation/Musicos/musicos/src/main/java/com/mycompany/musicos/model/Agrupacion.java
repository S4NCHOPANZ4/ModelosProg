package com.mycompany.musicos.model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

// SRP: solo gestiona una agrupación musical y sus miembros
public class Agrupacion {

    private String nombre;
    private String genero;
    private List<Musico> miembros;

    public Agrupacion(String nombre, String genero) {
        this.nombre = nombre;
        this.genero = genero;
        this.miembros = new ArrayList<>();
    }

    public void agregarMiembro(Musico m) {
        miembros.add(m);
        System.out.println(m.getNombre() + " agregado a " + nombre);
    }

    public void retirarMiembro(Musico m) {
        if (miembros.remove(m)) {
            System.out.println(m.getNombre() + " retirado de " + nombre);
        }
    }

    // Retorna lista inmutable: protege el estado interno
    public List<Musico> getMusicos() {
        return Collections.unmodifiableList(miembros);
    }

    public String getNombre() {
        return nombre;
    }

    public String getGenero() {
        return genero;
    }
}