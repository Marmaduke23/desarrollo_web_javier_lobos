package com.tarea4.tarea4.models;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.SequenceGenerator;
import jakarta.persistence.Table;

@Entity
@Table
public class Nota {
    @Id
    @SequenceGenerator(
        name="nota_sequence",
        sequenceName="nota_sequence",
        allocationSize=1
    )
    @GeneratedValue(
        strategy=GenerationType.SEQUENCE,
        generator="nota_sequence"
    )
    private int id;
    @ManyToOne
    @JoinColumn(name = "actividad_id", nullable = false)
    private Actividad actividad;

    private int nota;

    public Nota() {
    }
    public Nota(Actividad actividad, int nota) {
        this.actividad = actividad;
        this.nota = nota;
    }
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public Actividad getActividad() {
        return actividad;
    }
    public void setActividad(Actividad actividad) {
        this.actividad = actividad;
    }
    public int getNota() {
        return nota;
    }
    public void setNota(int nota) {
        this.nota = nota;
    }
    @Override
    public String toString() {
        return "Nota{" +
                "id=" + id +
                ", actividad=" + actividad +
                ", nota=" + nota +
                '}';
    }
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Nota nota1)) return false;

        if (id != nota1.id) return false;
        if (nota != nota1.nota) return false;
        return actividad != null ? actividad.equals(nota1.actividad) : nota1.actividad == null;
    }

}
