package com.tarea4.tarea4.controllers;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.tarea4.tarea4.models.Actividad;
import com.tarea4.tarea4.models.ActividadRepository;
import com.tarea4.tarea4.models.Nota;
import com.tarea4.tarea4.models.NotaRepository;

@RestController
public class ApiController {
    private final ActividadRepository actividadRepository;
    private final NotaRepository notaRepository;
    
    public ApiController(ActividadRepository actividadRepository, NotaRepository notaRepository) {
        this.actividadRepository = actividadRepository;
        this.notaRepository = notaRepository;
    }

    @PostMapping("/calificar")
    public ResponseEntity<?>calificarActividad(@RequestParam Long id, @RequestParam int nota) {
        if (nota < 1 || nota > 7) {
            return ResponseEntity.badRequest().body("La nota debe estar entre 1 y 7.");
        
        }

        Optional<Actividad> optActividad = actividadRepository.findById(id);
        if (optActividad.isEmpty()) {
            return ResponseEntity.notFound().build();
        }
        Actividad actividad=optActividad.get();
        Nota nuevaNota = new Nota();
        nuevaNota.setNota(nota);
        nuevaNota.setActividad(optActividad.get());
        notaRepository.save(nuevaNota);
        
        float promedio=actividad.getPromedioNota();
        Map<String, Object> response = new HashMap<>();
        response.put("promedio", promedio);

        
        return ResponseEntity.ok(response);
    }

}
