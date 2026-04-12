package com.mycompany.musicos.factory;

import com.mycompany.musicos.model.Cantante;
import com.mycompany.musicos.model.Instrumentista;
import com.mycompany.musicos.model.Musico;

import java.util.Random;

/**
 * FACTORY PATTERN
 * ---------------
 * Decide qué subclase de Musico crear y encapsula toda la lógica
 * de inicialización (datos aleatorios, rangos válidos, etc.).
 *
 * El cliente sólo llama a:
 *   MusicoFactory.crearAleatorio()
 *   MusicoFactory.crearCantante(nombre, edad, tessitura)
 *   MusicoFactory.crearInstrumentista(nombre, edad, instrumento, calidad)
 *
 * Así se cumple OCP: para agregar un nuevo tipo de músico (p.ej. DJ)
 * solo se extiende esta factory, sin tocar Musicos.java.
 */
public class MusicoFactory {

    private static final String[] NOMBRES = {
        "Laura", "Carlos", "Pedro", "Ana", "Miguel",
        "Sofía", "Diego", "Valentina", "Andrés", "Camila"
    };

    private static final String[] TESSITURAS = {
        "Soprano", "Mezzosoprano", "Contralto",
        "Tenor", "Barítono", "Bajo"
    };

    private static final Random RANDOM = new Random();

    // ── Creación explícita ──────────────────────────────────────────────────

    public static Cantante crearCantante(String nombre, int edad, String tessitura) {
        return new Cantante(nombre, edad, tessitura);
    }

    public static Instrumentista crearInstrumentista(String nombre, int edad,
            com.mycompany.musicos.model.Instrumento instrumento, int calidad) {
        return new Instrumentista(nombre, edad, instrumento, calidad);
    }

    // ── Creación aleatoria ──────────────────────────────────────────────────

    /**
     * Crea un Musico aleatorio: puede ser Cantante o Instrumentista,
     * con nombre, edad, tessitura/instrumento y calidad generados al azar.
     */
    public static Musico crearAleatorio() {
        String nombre    = NOMBRES[RANDOM.nextInt(NOMBRES.length)] + "_" + RANDOM.nextInt(100);
        int    edad      = 18 + RANDOM.nextInt(33); // 18–50

        if (RANDOM.nextBoolean()) {
            // ── Cantante aleatorio
            String tessitura = TESSITURAS[RANDOM.nextInt(TESSITURAS.length)];
            return new Cantante(nombre, edad, tessitura);
        } else {
            // ── Instrumentista aleatorio
            com.mycompany.musicos.model.Instrumento instrumento =
                    InstrumentoFactory.crearAleatorio();
            int calidad = 1 + RANDOM.nextInt(10); // 1–10
            return new Instrumentista(nombre, edad, instrumento, calidad);
        }
    }
}