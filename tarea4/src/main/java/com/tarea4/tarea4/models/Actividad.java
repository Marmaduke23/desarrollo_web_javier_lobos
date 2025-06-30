package com.tarea4.tarea4.models;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

import jakarta.persistence.GenerationType;
import jakarta.persistence.SequenceGenerator;


@Entity
@Table
public class Actividad {
    @Id
    @SequenceGenerator(
        name="actividad_sequence",
        sequenceName="actividad_sequence",
        allocationSize=1
    )
    @GeneratedValue(
        strategy=GenerationType.SEQUENCE,
        generator="actividad_sequence"
    )
    private int id;
    private String sector;
    private String nombre;
    private String email;
    private String celular;
    private LocalDateTime dia_hora_inicio;
    private LocalDateTime dia_hora_termino;
    @OneToMany(mappedBy = "actividad", cascade=CascadeType.ALL, orphanRemoval = true)
    private List<ActividadTema> actividadTemas;
    @OneToMany(mappedBy = "actividad", cascade=CascadeType.ALL, orphanRemoval = true)
    private List<Nota> notas;


    Actividad(String sector, String nombre, String email, String celular, LocalDateTime dia_hora_inicio, LocalDateTime dia_hora_termino) {
        this.sector = sector;
        this.nombre = nombre;
        this.email = email;
        this.celular = celular;
        this.dia_hora_inicio = dia_hora_inicio;
        this.dia_hora_termino = dia_hora_termino;
    }

    public int getId() {
        return id;
    }

    public String getSector() {
        return sector;
    }
    public String getNombre() {
        return nombre;
    }
    public String getEmail() {
        return email;
    }
    public String getCelular() {
        return celular;
    }
    public LocalDateTime getDiaHoraInicio() {
        return dia_hora_inicio;
    }
    public LocalDateTime getDiaHoraTermino() {
        return dia_hora_termino;
    }
    public List<String> getActividadTemas() {
        List<String> temasList = new ArrayList<>();
        for (ActividadTema tema:this.actividadTemas) {
            if ("otro".equals(tema.getTema())) {
                temasList.add(tema.getGlosaOtro());
            } else {
                temasList.add(tema.getTema().toString());
            }
        }
        return temasList;
    }
    public float getPromedioNota() {
        if (notas.isEmpty()) {
            return 0; // Si no hay notas, retornar 0
        }
        int suma = 0;
        for (Nota nota : notas) {
            suma += nota.getNota();
        }
        return Math.round((float) suma / notas.size() * 10) / 10.0f;
    }
    public void setId(int id) {
        this.id = id;
    }

    public void setSector(String sector) {
        this.sector = sector;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    public void setCelular(String celular) {
        this.celular = celular;
    }
    public void setDiaHoraInicio(LocalDateTime dia_hora_inicio) {
        this.dia_hora_inicio = dia_hora_inicio;
    }
    public void setDiaHoraTermino(LocalDateTime dia_hora_termino) {
        this.dia_hora_termino = dia_hora_termino;
    }



    public Actividad() {
        // Constructor vacío requerido por JPA
    }
    @Override
    public String toString() {
        return "Actividad{" +
                "id=" + id +
                ", sector='" + sector + '\'' +
                ", nombre='" + nombre + '\'' +
                ", email='" + email + '\'' +
                ", celular='" + celular + '\'' +
                ", dia_hora_inicio=" + dia_hora_inicio +
                ", dia_hora_termino=" + dia_hora_termino +
                '}';
    }
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Actividad)) return false;
        Actividad actividad = (Actividad) o;
        return id == actividad.id &&
                sector.equals(actividad.sector) &&
                nombre.equals(actividad.nombre) &&
                email.equals(actividad.email) &&
                celular.equals(actividad.celular) &&
                dia_hora_inicio.equals(actividad.dia_hora_inicio) &&
                dia_hora_termino.equals(actividad.dia_hora_termino);
    }



}
