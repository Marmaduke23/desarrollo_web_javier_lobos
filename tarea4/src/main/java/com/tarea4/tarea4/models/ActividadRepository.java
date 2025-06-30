package com.tarea4.tarea4.models;

import java.util.List;


import org.springframework.data.jpa.repository.JpaRepository;

public interface ActividadRepository extends JpaRepository<Actividad, Long> {
    List<Actividad> findAllByOrderByIdDesc();
    

}
