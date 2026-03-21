package com.mycompany.musicos.singleton;

import com.mycompany.musicos.model.Agrupacion;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


public class AgrupacionManager {

    private final List<Agrupacion> agrupaciones;

    // Constructor privado: nadie fuera puede hacer `new AgrupacionManager()`
    private AgrupacionManager() {
        this.agrupaciones = new ArrayList<>();
    }

    private static class Holder {
        private static final AgrupacionManager INSTANCIA = new AgrupacionManager();
    }
    public static AgrupacionManager getInstance() {
        return Holder.INSTANCIA;
    }

    public void registrar(Agrupacion agrupacion) {
        agrupaciones.add(agrupacion);
        System.out.println("  ✅ [AgrupacionManager] '" + agrupacion.getNombre()
                + "' registrada. Total bandas: " + agrupaciones.size());
    }


    public Agrupacion buscarPorNombre(String nombre) {
        return agrupaciones.stream()
                .filter(a -> a.getNombre().equalsIgnoreCase(nombre))
                .findFirst()
                .orElse(null);
    }

    public List<Agrupacion> getAgrupaciones() {
        return Collections.unmodifiableList(agrupaciones);
    }

    public void mostrarResumen() {
        System.out.println("REGISTRO GLOBAL DE AGRUPACIONES");
        if (agrupaciones.isEmpty()) {
            System.out.println("  (sin agrupaciones registradas)");
        } else {
            for (Agrupacion a : agrupaciones) {
                System.out.println("" + a.getNombre()
                        + " [" + a.getGenero() + "] — "
                        + a.getMusicos().size() + " miembro(s)");
            }
        }
    }
}