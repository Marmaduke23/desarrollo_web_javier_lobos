package com.tarea4.tarea4.models;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Enumerated;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import jakarta.persistence.GenerationType;
import jakarta.persistence.SequenceGenerator;
import jakarta.persistence.EnumType;

@Entity
@Table(name = "actividad_tema")
public class ActividadTema {
    @Id
    @SequenceGenerator(
        name="actividadtema_sequence",
        sequenceName="actividadtema_sequence",
        allocationSize=1
    )
    @GeneratedValue(
        strategy=GenerationType.SEQUENCE,
        generator="actividadtema_sequence"
    )
    private int id;
    
    @Column(nullable = false)
    private String tema;

    @Column(name = "glosa_otro", length = 15)
    private String glosaOtro;

    
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "actividad_id", nullable = false)
    private Actividad actividad;

   
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getTema() {
        return tema;
    }
  
    public String getGlosaOtro() {
        return glosaOtro;
    }
    public void setGlosaOtro(String glosaOtro) {
        this.glosaOtro = glosaOtro;
    }
    public Actividad getActividad() {
        return actividad;
    }
    public void setActividad(Actividad actividad) {
        this.actividad = actividad;
    }
    

   

}
