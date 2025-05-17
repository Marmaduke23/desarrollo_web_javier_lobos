 

const validateText = (name,maxlen,optional,minlen=1) => {
  if(!name & optional==true) {return true} else if(!name & optional==false) {return false};
  let lengthValid = (name.trim().length <= maxlen && name.trim().length >= minlen);
  
  return lengthValid;
};    

const validateEmail = (email) => {
    if (!email) return false;
    let lengthValid = email.length <= 100;
  
    
    let re = /^[\w.]+@([\w-]+\.)+[a-zA-Z]{2,}$/;
    let formatValid = re.test(email);
  
    
    return lengthValid && formatValid;
};

const validatePhoneNumber = (phoneNumber,optional=true) => {
    if (optional==false & !phoneNumber) return false;
    if (optional==true & !phoneNumber) return true;
     
    // validación de formato
    let re = /^\+[0-9]{3}\.[0-9]{8}$/
;
    let formatValid = re.test(phoneNumber);
  
    // devolvemos la lógica AND de las validaciones.
    return formatValid;
};

const validateDate = (date, optional) => {
    if(!date && optional==true) {return true} else if(!date && optional==false) {return false};
       
    let re = /^\d{4}-\d{2}-\d{2}T([01]?[0-9]|2[0-3]):([0-5]?[0-9])$/;
    let formatValid = re.test(date);
  
    
    return formatValid;
}

const validateEndDate = (startDate, endDate) => {
    if (!endDate) return true;
    if (!startDate) return false;
    if (validateDate(startDate,false)& validateDate(endDate,false)) {
        // Convertir las fechas a objetos Date
    const start = new Date(startDate);
    const end = new Date(endDate);
  
    // Validar que la fecha de inicio sea anterior a la fecha de término
    return start < end;}   
};

const validateFiles = (files) => {
    if (!files) return false;
  
    // validación del número de archivos
    let lengthValid = 1 <= files.length && files.length <= 5;
  
    // validación del tipo de archivo
    let typeValid = true;
  
    for (const file of files) {
      // el tipo de archivo debe ser "image/<foo>" o "application/pdf"
      let fileFamily = file.type.split("/")[0];
      typeValid &&= fileFamily == "image";
    }
  
    // devolvemos la lógica AND de las validaciones.
    return lengthValid && typeValid;
};

const validateSelect = (select) => {
    if(!select) return false;
    return true
};

const validateCheckbox = (checkbox) => {
    if(!checkbox) return false;
    return true
};

const validateCheck=(clasecheck, limiteinf,limitesup) => {
    const checkboxes = document.querySelectorAll(`.${clasecheck}`);
    let isChecked = 0;
    checkboxes.forEach((checkbox) => {
        if (checkbox.checked) {
            isChecked++;
        }
    });
    return isChecked <= limitesup && isChecked >= limiteinf;
};

const validateUrl = (url) => {
    if (!url) return false;
    let lengthValid = url.length <= 50 && url.length >= 4; 
  
    
    let re = /^(https?:\/\/)?([\w\-]+\.)+[\w\-]{2,}(\/[\w\-._~:/?#[\]@!$&'()*+,;=]*)?$/;
    let formatValid = re.test(url);
  
    
    return lengthValid && formatValid;
}
const validateId = (id) => {
    if (!id) return false;
    let lengthValid = id.length <= 50 && id.length >= 4;
    let re=/\B@[a-zA-Z][a-zA-Z0-9_.]{2,49}\b/

    let formatValid = re.test(id);
    return lengthValid && formatValid;
}

const validateForm = () => {
    let myForm = document.forms["Agregar"];
    let region = myForm["select-region"].value;
    let comuna = myForm["select-comuna"].value;
    let sector = myForm["sector"].value;
    let nombre = myForm["nombre"].value;
    let email = myForm["email"].value;
    let telefono = myForm["celuar"].value;
    let whastapp= myForm["whatsapp-id"];
    let telegram= myForm["telegram-id"];
    let instagram= myForm["instagram-id"];
    let x= myForm["x-id"];
    let tiktok= myForm["tiktok-id"];
    let otra= myForm["otra-id"];
    let otroText= myForm["otro-text"];

    let inicio = myForm["inicio"].value;
    let termino = myForm["termino"].value;
    let descripcion = myForm["descripcion"].value;
    let tema = myForm["tema"].value;
    let fotos = myForm["fotos"].files;

    // variables auxiliares de validación y función.
    let invalidInputs = [];
    let isValid = true;
    const setInvalidInput = (inputName) => {
      invalidInputs.push(inputName);
      isValid &&= false;
    };
  
    // lógica de validación
    if (!validateText(sector,100,true)) {
      setInvalidInput("Sector");
    }
    if (!validateEmail(email)) {
      setInvalidInput("Email");
    }
    if (!validatePhoneNumber(telefono)) {
      setInvalidInput("Número");
    }
    if (!validateCheck("check",0,5)) {
      setInvalidInput("Contacto");
    }
    if ((whastapp.style.display== "block" && !(validateUrl(whastapp.value)||validatePhoneNumber(whastapp.value,false)))) {
        setInvalidInput("Whatsapp");
      setInvalidInput("Whatsapp");
    }
    if ((telegram.style.display== "block" && !(validateUrl(telegram.value)||validatePhoneNumber(telegram.value,false)))) {
        setInvalidInput("Telegram");
    }
    if ((instagram.style.display== "block" && !(validateUrl(instagram.value)||validateId(instagram.value)))) {
        setInvalidInput("Instagram");
    }
    if ((x.style.display== "block" && !(validateUrl(x.value)||validateId(x.value)))) {
        setInvalidInput("X");
    }
    if ((tiktok.style.display== "block" && !(validateUrl(tiktok.value)||validateId(tiktok.value)))) {
        setInvalidInput("Tiktok");
    }
    if ((otra.style.display== "block" && !(validateUrl(otra.value)||validateId(otra.value)))) {
        setInvalidInput("Otra red social");
    }

 


    if (!validateFiles(fotos)) {
      setInvalidInput("Fotos");
    }
    if (!validateCheck("tema-check",1,10)) {
      setInvalidInput("Tema");
    }
    if (!validateText(otroText.value,15,false,minlen=3)&&otroText.style.display== "block") {
        setInvalidInput("Otro Texto");
      }

    
    if (!validateText(descripcion,500,false)) {
      setInvalidInput("Descripción");
    }
    if (!validateDate(inicio,false)) {
      setInvalidInput("Fecha de inicio");
    }
    if (!validateEndDate(inicio,termino)) {
      setInvalidInput("Fecha de término");
    }
    if (!validateSelect(region)) {
      setInvalidInput("Región");
    }
    if (!validateSelect(comuna)) {
        setInvalidInput("Comuna");
    }
   

    
    return { isValid, invalidInputs };

    
    };

    document.getElementById("Registrar-Actividad").addEventListener("click", function() {
        if (validateForm().isValid) {
            document.getElementById("ventana").style.display = "flex";
            document.getElementById("ventana-error").style.display = "none";
            document.getElementById("ventana-exito").style.display = "none";
            document.getElementById("ventana-confirma").style.display = "block";
        } else {
            document.getElementById("ventana").style.display = "flex";
            document.getElementById("ventana-exito").style.display = "none";
            document.getElementById("ventana-confirma").style.display = "none";
            document.getElementById("ventana-error").style.display = "block";
            listaErrores = document.getElementById("error-list");
            listaErrores.innerHTML = "";
            validateForm().invalidInputs.forEach(function(error) {
                let li = document.createElement("li");
                li.textContent = error;
                listaErrores.appendChild(li);
            });

        }
    });
    
    document.getElementById("cancela").addEventListener("click", function() {
        document.getElementById("ventana").style.display = "none";
    });
    document.getElementById("volver").addEventListener("click", function() {
        document.getElementById("ventana").style.display = "none";
    });
    document.getElementById("confirma").addEventListener("click", function() {
        let myForm = document.forms["Agregar"];
        myForm.submit();
        document.getElementById("ventana-confirma").style.display = "none";
        document.getElementById("ventana-exito").style.display = "flex";
        document.getElementById("ventana-error").style.display = "none";
        


    });
    function revisaCheck(element){
        if (element.checked) {
          document.getElementById(element.name).style.display = "block";
        } else {
           document.getElementById(element.name).style.display = "none";
        }
    };