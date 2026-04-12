package com.mycompany.musicos.model;

import java.time.LocalDate;

// SRP: solo representa un evento musical
public class Evento {

    private String lugar;
    private LocalDate fecha;
    private Agrupacion entretenimiento;
    private int aforo;
    private boolean cancelado;

    public Evento(String lugar, LocalDate fecha, int aforo) {
        this.lugar = lugar;
        this.fecha = fecha;
        this.aforo = aforo;
        this.cancelado = false;
    }

    public void registrarAgrupacion(Agrupacion a) {
        this.entretenimiento = a;
        System.out.println("Agrupación '" + a.getNombre() + "' registrada en el evento de " + lugar);
    }

    public void cancelarEvento() {
        this.cancelado = true;
        System.out.println("Evento en " + lugar + " el " + fecha + " ha sido cancelado.");
    }

    public LocalDate getFecha() {
        return fecha;
    }

    public String getLugar() {
        return lugar;
    }

    public int getAforo() {
        return aforo;
    }

    public boolean isCancelado() {
        return cancelado;
    }

    public Agrupacion getEntretenimiento() {
        return entretenimiento;
    }
}