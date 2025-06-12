# desarrollo_web_javier_lobos

Se siguio el enunciado general de la tarea.


### Características

Las principales consideraciones se realizaron en las validaciones de las redes sociales de contacto, considerando como validos para cada red social (Un ID se considero de la forma "@nombre de usuario"):


- Whastapp: Numero de Celular o url.
- Instagram: ID o URL.
- Telegram: Numero de celular o url.
- X: ID o URL.
- Tiktok: ID o URL.
- Otros: ID o URL.

Para las validaciones se implemento un cuadro de aviso para el usuario cuando quiere confirmar el formulario que le indica cuales son los campos con errores.

Otros criterios adoptados, para la informacion de las actividades se trato de implementar algo similar a una galeria, donde la imagen se expande con una pequeña animacion al hacer click y puede volver a su tamaño original haciendo click nuevamente.

##Tarea 2

Se corrigen los errores observados durante la entrega 1.

##Consideraciones:

La revision de los archivos HTML con el validador se hizo despues de que flask procesara las plantillas Jinja, es decir, usando el codigo de fuente de cada una de las paginas.

##Tarea 3

Se construyen los graficos de las actividades solicitados, para el grafico de torta se consideran como tipos de actividades las dadas por defecto y adicionalemente las que ingresan en el campo de "Otros".
Las Franjas horarias para el grafico de barras se consideran las 12 y 14 horas como divisores entre la franja de mañana, media y tarde.
##Consideraciones:
Se utilizo highcharts para la construccion de los graficos.
Para la conexion con el backend se utilizaron consultas fetch, y se implemento un sistema de manejo de errores para las respuestas del servidor, mostrando un mensaje de error al usuario en caso de que la consulta falle.

Para identificar los mensajes de error en el formulario enviados por el backend se les añadio un prefijo "Server:" para indicar que el mensaje de error proviene del servidor y no del frontend.

## 🧰 Requisitos del Proyecto

Este proyecto requiere las siguientes dependencias, las cuales están definidas en el archivo [`requirements.txt`](./requirements.txt):

### 📦 Lista de dependencias

| Paquete           | Versión   |
|-------------------|-----------|
| blinker           | 1.9.0     |
| cffi              | 1.17.1    |
| click             | 8.1.8     |
| colorama          | 0.4.6     |
| cryptography      | 44.0.3    |
| filetype          | 1.2.0     |
| Flask             | 3.1.0     |
| flask-cors        | 6.0.0     |
| greenlet          | 3.2.1     |
| itsdangerous      | 2.2.0     |
| Jinja2            | 3.1.6     |
| MarkupSafe        | 3.0.2     |
| pycparser         | 2.22      |
| PyMySQL           | 1.1.1     |
| SQLAlchemy        | 2.0.40    |
| typing_extensions | 4.13.2    |
| Werkzeug          | 3.1.3     |

