package com.mycompany.musicos.factory;

import com.mycompany.musicos.enums.TipoInstrumento;
import com.mycompany.musicos.model.Instrumento;

import java.util.Random;


public class InstrumentoFactory {

    // Catalogo de instrumentos disponibles: {nombre, tipo, marca}
    private static final Object[][] CATALOGO = {
        { "Guitarra",    TipoInstrumento.CUERDA,    "Fender"   },
        { "Bajo",        TipoInstrumento.CUERDA,    "Gibson"   },
        { "Violín",      TipoInstrumento.CUERDA,    "Stradivarius" },
        { "Batería",     TipoInstrumento.PERCUSION,  "Pearl"    },
        { "Cajón",       TipoInstrumento.PERCUSION,  "Meinl"    },
        { "Trompeta",    TipoInstrumento.VIENTO,    "Bach"     },
        { "Saxofón",     TipoInstrumento.VIENTO,    "Yamaha"   },
        { "Flauta",      TipoInstrumento.VIENTO,    "Gemeinhardt" },
        { "Piano",       TipoInstrumento.TECLADO,   "Steinway" },
        { "Teclado",     TipoInstrumento.TECLADO,   "Roland"   },
    };

    private static final Random RANDOM = new Random();



    public static Instrumento crear(String nombre, TipoInstrumento tipo, String marca) {
        return new Instrumento(nombre, tipo, marca);
    }

    public static Instrumento crearAleatorio() {
        Object[] datos = CATALOGO[RANDOM.nextInt(CATALOGO.length)];
        return new Instrumento(
            (String) datos[0],
            (TipoInstrumento) datos[1],
            (String) datos[2]
        );
    }
}