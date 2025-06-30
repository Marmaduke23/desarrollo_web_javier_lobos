package com.tarea4.tarea4.services;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.cglib.core.Local;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;
import org.springframework.util.ResourceUtils;

import com.tarea4.tarea4.models.Actividad;
import com.tarea4.tarea4.models.ActividadRepository;
import java.time.LocalDateTime;



@Service
public class AppService {
    private final String pathStatic;
    private final ActividadRepository actividadRepository;

    public AppService(ActividadRepository actividadRepository) throws IOException {
        this.actividadRepository = actividadRepository;
        // Dynamically resolve the absolute path for the static directory
        //Path staticDir = Paths.get(ResourceUtils.getFile("classpath:static").getAbsolutePath());
        //this.pathStatic = staticDir.toString();
        this.pathStatic="";
        System.out.println("Static path resolved to: " + this.pathStatic);
    }
    public List<Map<String,String>> getActividadData(){
        List<Actividad> actividades = actividadRepository.findAllByOrderByIdDesc();
        List<Map<String,String>> actividadData=new ArrayList<>();
        LocalDateTime localDateTime = LocalDateTime.now();
        for (Actividad actividad : actividades){
            if (actividad.getDiaHoraTermino() != null && actividad.getDiaHoraTermino().isBefore(localDateTime)){
            Map<String,String> actData=new HashMap<>();
            actData.put("id", String.valueOf(actividad.getId()));
            actData.put("dia_hora_inicio", actividad.getDiaHoraInicio().toString());
            actData.put("sector", actividad.getSector());
            actData.put("nombre", actividad.getNombre());         
            actData.put("temas", String.join(", ", actividad.getActividadTemas()));
            actData.put("nota", actividad.getPromedioNota() == 0 ? "-" : String.valueOf(actividad.getPromedioNota()));
            actividadData.add(actData);
            }
        }
        return actividadData;
    }



}
