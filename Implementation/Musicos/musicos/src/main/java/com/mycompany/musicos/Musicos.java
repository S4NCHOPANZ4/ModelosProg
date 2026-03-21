package com.mycompany.musicos;

import com.mycompany.musicos.factory.MusicoFactory;
import com.mycompany.musicos.model.Agrupacion;
import com.mycompany.musicos.model.Cantante;
import com.mycompany.musicos.model.Evento;
import com.mycompany.musicos.model.Instrumentista;
import com.mycompany.musicos.model.Musico;
import com.mycompany.musicos.singleton.AgrupacionManager;

import java.time.LocalDate;
import java.util.Random;


public class Musicos {

    // Nombres y géneros para generar bandas al azar
    private static final String[] PREFIJOS  = { "Los", "Las", "The", "Super", "Ultra" };
    private static final String[] SUFIJOS   = { "Sónicos", "Rockeros", "Jazzistas", "Furiosos", "Místicos" };
    private static final String[] GENEROS   = { "Rock", "Jazz", "Pop", "Salsa", "Metal", "Cumbia" };
    private static final Random   RANDOM    = new Random();

    public static void main(String[] args) {

        System.out.println("══════════════════════════════════════════");
        System.out.println("   SISTEMA DE GESTIÓN MUSICAL  v2.0      ");
        System.out.println("   Patrones: Factory + Singleton           ");
        System.out.println("══════════════════════════════════════════\n");

        // SINGLETON
        AgrupacionManager manager = AgrupacionManager.getInstance();

        // ambas referencias apuntan al mismo objeto
        AgrupacionManager otraReferencia = AgrupacionManager.getInstance();
        System.out.println("¿Manager es Singleton? "
                + (manager == otraReferencia) + "\n");  // true

        // agrupaciones con miembros aleatorios (FACTORY)
        int totalBandas   = 3;
        int miembrosPorBanda = 4;

        for (int b = 0; b < totalBandas; b++) {
            String nombreBanda = PREFIJOS[RANDOM.nextInt(PREFIJOS.length)]
                               + " " + SUFIJOS[RANDOM.nextInt(SUFIJOS.length)];
            String genero      = GENEROS[RANDOM.nextInt(GENEROS.length)];

            Agrupacion banda = new Agrupacion(nombreBanda, genero);

            System.out.println("─────────────────────────────────────────");
            System.out.println("Banda: " + nombreBanda + "  |  Genero: " + genero);
            System.out.println("─────────────────────────────────────────");

            // Crear músicos aleatorios con la FACTORY
            for (int i = 0; i < miembrosPorBanda; i++) {
                Musico musico = MusicoFactory.crearAleatorio(); // ← Factory en acción
                banda.agregarMiembro(musico);

                // Mostrar tipo concreto sin castear en Musicos.java
                if (musico instanceof Cantante c) {
                    System.out.println("  + Cantante    : " + c.getNombre()
                            + " | " + c.getTessitura()
                            + " | " + c.getEdad() + " años");
                } else if (musico instanceof Instrumentista inst) {
                    System.out.println("  + Instrumentista: " + inst.getNombre()
                            + " | " + inst.getInstrumento()
                            + " | calidad " + inst.getCalidad() + "/10"
                            + " | " + inst.getEdad() + " años");
                }
            }

            // Registrar en el Singleton
            manager.registrar(banda);

            // Demostrar polimorfismo: tocar y afinar
            System.out.println("\n  🎵 Ensayo:");
            for (Musico m : banda.getMusicos()) {
                m.tocar();
            }

            // Crear y vincular un evento
            LocalDate fechaEvento = LocalDate.now().plusMonths(1 + b);
            Evento evento = new Evento("Escenario " + (b + 1), fechaEvento, 200 + b * 100);
            evento.registrarAgrupacion(banda);
            System.out.println("  Fecha: " + evento.getFecha()
                    + " | Aforo: " + evento.getAforo() + " personas\n");
        }

        // 3. Mostrar resumen global desde el Singleton 
        manager.mostrarResumen();

        // 4. Búsqueda en el Singleton
        if (!manager.getAgrupaciones().isEmpty()) {
            String nombreBuscado = manager.getAgrupaciones().get(0).getNombre();
            Agrupacion encontrada = manager.buscarPorNombre(nombreBuscado);
            System.out.println("Búsqueda por nombre '" + nombreBuscado + "': "
                    + (encontrada != null ? "encontrada" : "no encontrada"));
        }
    }
}