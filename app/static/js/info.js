document.querySelectorAll(".img-div").forEach(img => {
    const mensaje=document.createElement("span")
    img.appendChild(mensaje);
    mensaje.textContent="Haz click en la imagen para volver";
    mensaje.style.position="absolute";
    mensaje.style.top="40px";
    mensaje.style.left="50%";
    mensaje.style.transform="translate(-50%, -50%)";
    mensaje.style.backgroundColor="rgba(255, 255, 255, 0.8)";
    mensaje.style.padding="10px";

    mensaje.style.fontSize="16px";
    

    mensaje.style.display="none";
    
    img.addEventListener("click", function() {
        if (img.dataset.emergente){
            img.style.height="240px";
            img.style.width="320px";
            img.style.transition="0.5s";
            delete img.dataset.emergente;
            img.style.position="relative";
            img.style.zIndex="0";
            img.style.left="0";
            img.style.transform="none";
            img.style.boxShadow="none";
            mensaje.style.display="none";
        }
        else{
        img.style.height="600px";
        img.style.width="800px";
        img.dataset.emergente=true;
        img.style.position="absolute";
        img.style.zIndex="1000";
        img.style.left="50%";
        img.style.transform="translateX(-50%)";
        img.style.transition="0.5s";
        img.style.boxShadow="0 0 10px #000000";
        mensaje.style.display="block";


    }
        

        
    });

});

const validateName = (name) => {
    if (!name || name.length < 3 || name.length > 80) {
        return false;
    }else { return true; }
}

const validateText = (text) => {
    if (!text || text.length < 5 || text.length > 500) {
        return false;
    } else { return true; }
}

const validarFormulario = () => {
    const myForm = document.forms["Agregar"];
    const name = myForm["nombre"];
    const text = myForm["comentario"];
    
    let valid = true;
    name.classList.remove("input-error");
    text.classList.remove("input-error");
    document.getElementById("error-nombre").innerText = "";
    document.getElementById("error-comentario").innerText = "";
    if (!validateName(name.value.trim())) {
        name.classList.add("input-error");
        document.getElementById("error-nombre").innerText = "El nombre debe tener entre 3 y 80 caracteres.";
        valid = false;
    }
    if (!validateText(text.value.trim())) {
        text.classList.add("input-error");
        document.getElementById("error-comentario").innerText = "El comentario debe tener entre 5 y 500 caracteres.";
        valid = false;
    }
    console.log("Validación del formulario:", valid);
   return valid;
}

document.getElementById("Agregar").addEventListener("submit", async function(event) {
    event.preventDefault(); 
    
    if (!validarFormulario()) return; 
    
    const formData = new FormData(this);

    try {
        
        const response = await fetch(this.action, {
            method: this.method,
            body: formData,
            credentials: 'include' 
        });

        if (response.ok) {
            
            cargarComentarios(actividadId)
             
            
        } else {
            
            const data = await response.json();
            mostrarErrorServidor(data.error || "Error al enviar el comentario");
        }

    } catch (error) {
        mostrarErrorServidor("Error de conexión, intenta más tarde.");
    }
});


function mostrarErrorServidor(mensaje) {
    let divError = document.getElementById("error-servidor");
    if (!divError) {
        divError = document.createElement("div");
        divError.id = "error-servidor";
        divError.style.color = "red";
        divError.style.marginTop = "10px";
        document.getElementById("Agregar").appendChild(divError);
    }
    divError.innerText = mensaje;
}

async function cargarComentarios(actividad_id) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/comentarios?actividad_id=${actividadId}`, {
            method: 'GET',
           
        });

        if (response.ok) {
            const comentarios = await response.json();
            const listaComentarios = document.getElementById("lista-comentarios");
            listaComentarios.innerHTML = ""; // Limpiar lista actual

             Object.entries(comentarios)
    .sort((a, b) => Number(b[0]) - Number(a[0]))  // ordena por clave numérica descendente
    .forEach(([_, comentario]) => {
        const contenedor = document.createElement("div");
        contenedor.classList.add("comentario");

        const fecha = comentario.fecha.split(" ")[0];

        contenedor.innerHTML = `
            <div class="comentario-header">
                <strong>${comentario.nombre}</strong> <span class="comentario-fecha">${fecha}</span>
            </div>
            <div class="comentario-texto">${comentario.texto}</div>
        `;

        listaComentarios.appendChild(contenedor);
    });
        } else {
            console.error("Error al cargar los comentarios:", response.statusText);
        }
    } catch (error) {
        console.error("Error de conexión:", error);
    }
}
cargarComentarios(actividadId);