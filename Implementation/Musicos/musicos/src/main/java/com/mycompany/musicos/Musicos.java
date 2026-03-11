package com.mycompany.musicos;

import com.mycompany.musicos.enums.TipoInstrumento;
import com.mycompany.musicos.model.*;
import java.time.LocalDate;

public class Musicos {

    public static void main(String[] args) {

        // Crear instrumentos
        Instrumento guitarra = new Instrumento("Guitarra", TipoInstrumento.CUERDA, "Fender");
        Instrumento bateria = new Instrumento("Batería", TipoInstrumento.PERCUSION, "Pearl");

        // Crear músicos
        Cantante cantante = new Cantante("Laura", 28, "Soprano");
        Instrumentista guitarrista = new Instrumentista("Carlos", 30, guitarra, 9);
        Instrumentista baterista = new Instrumentista("Pedro", 25, bateria, 8);

        // Presentarse
        System.out.println(cantante.presentarse());
        System.out.println(guitarrista.presentarse());

        // Tocar y afinar
        cantante.tocar();
        guitarrista.afinar();
        baterista.tocar();

        // Crear agrupación
        Agrupacion banda = new Agrupacion("Los Sónicos", "Rock");
        banda.agregarMiembro(cantante);
        banda.agregarMiembro(guitarrista);
        banda.agregarMiembro(baterista);

        System.out.println("\nMiembros de " + banda.getNombre() + ":");
        for (Musico m : banda.getMusicos()) {
            System.out.println("  - " + m.getNombre());
        }

        // Crear evento
        Evento evento = new Evento("Teatro Nacional", LocalDate.of(2026, 5, 20), 500);
        evento.registrarAgrupacion(banda);
        System.out.println("Fecha: " + evento.getFecha() + " | Lugar: " + evento.getLugar());
    }
}