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