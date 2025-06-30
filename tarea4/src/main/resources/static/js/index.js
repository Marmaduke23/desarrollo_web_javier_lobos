const validarNota = (nota) => {
    if (!nota || isNaN(nota) || nota < 1 || nota > 7 || !Number.isInteger(Number(nota))) {
        return false;
    } else {
        return true;
    }
};

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("form.calificacion-form").forEach((form) => {
        form.addEventListener("submit", function (event) {
            event.preventDefault();
            console.log("Formulario interceptado por JS ✅");

            const nota = form.nota.value;
            const id = form.dataset.id;

            if (!validarNota(nota)) {
                alert("La nota debe ser un número entero entre 1 y 7.");
                return;
            }

            fetch("/calificar", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: new URLSearchParams({ id, nota })
            })
            .then(response => response.json())
            .then(data => {
                const promedio = data.promedio;

                // ✅ Actualiza la celda con el nuevo promedio
                const notaElement = document.getElementById(`nota-${id}`);
                if (notaElement) {
                    notaElement.textContent = promedio.toFixed(1);
                }

                // ✅ Reemplaza el formulario por "Actividad calificada"
                const td = form.parentElement;
                td.textContent = "Actividad calificada";
            })
            .catch(error => {
                console.error("Error:", error);
                alert("Ocurrió un error al calificar la actividad.");
            });
        });
    });
});




