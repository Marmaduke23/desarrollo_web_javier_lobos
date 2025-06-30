package com.tarea4.tarea4.controllers;

import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import com.tarea4.tarea4.services.AppService;

@Controller
public class AppController {
    private final AppService appService;
    public AppController(AppService appService) {
        this.appService = appService;
    }
    @GetMapping("/")
    public String index(Model model) {
        List<Map<String, String>> modelData = appService.getActividadData();
        model.addAttribute("data", modelData);

        return "index";
    }

}
