# 📄 Tarea 4: Sistema de Calificación de Actividades

##  Descripción

La aplicacion incluye la funcionalidad de calificacion de actividades, la funcionalidad solicitada se implementa en el template index.html (en la ruta de incio "/"). Solo se implementan las entidades de Actividad, tema y nota de la base de datos dado que son las necesarias para la funcionalidad.

El controlador REST solo permite agregar notas a la base de datos y devolver el promedio de las notas actualizadas, todos los otros datos de actividades se manejan en el AppController. 

Para la funcionalidad se asume que las actividades sin fecha de termino aun no han terminado, por lo cual es imposible puntuarlas.Se prefirio que la forma de evaluar las actividades es mediante un select de 1 a 7 para simular un tipo calificacion "Por estrellas".

El template se evalua luego de renderizarse.

---

## Requerimientos

- Java 24
- Spring Boot 3.5.3
- Thymeleaf
- Bootstrap 5
- JavaScript (Fetch API)
- HTML5 + CSS

---



