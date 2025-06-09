import re
from datetime import datetime
import filetype

def validar_sector(sector):
    return len(sector) > 0 and len(sector) < 100

def validar_email(email):
    reg=r'^[\w.]+@([\w-]+\.)+[a-zA-Z]{2,}$'
    if not re.match(reg, email):
        return False
    return True

def validar_url(url):
    reg=r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'
    if not re.match(reg, url):
        return False
    return True

def validar_celular(celular,optional=False):
    if celular=='' and optional:
        return True
    elif celular=='' and not optional:
        return False,print(celular)
    reg=r'^\+[0-9]{3}\.[0-9]{8}$'
    if not re.match(reg, celular):
        return False,print(celular)
    return True


def validate_date(date, optional):
    if not date and optional:
        return True
    elif not date and not optional:
        return False

    pattern = r'^\d{4}-\d{2}-\d{2}T([01]?[0-9]|2[0-3]):([0-5]?[0-9])$'
    return re.match(pattern, date) is not None

def validate_end_date(start_date, end_date):
    if not end_date:
        return True
    if not start_date:
        return False
    if validate_date(start_date, False) and validate_date(end_date, False):
        # Convertir las fechas a objetos datetime
        start = datetime.strptime(start_date, "%Y-%m-%dT%H:%M")
        end = datetime.strptime(end_date, "%Y-%m-%dT%H:%M")
        # Validar que la fecha de inicio sea anterior a la fecha de término
        return start < end
    return False

def validate_id(id):
    if not id:
        return False
    length_valid = 4 <= len(id) <= 50
    pattern = r'\B@[a-zA-Z][a-zA-Z0-9_.]{2,49}\b'
    format_valid = re.search(pattern, id) is not None
    return length_valid and format_valid


def validate_img(img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if img is None:
        return False
    

    # check if the browser submitted an empty file
    if img.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(img)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True

def validate_img_list(imgs):
    if not imgs:
        return False
    if len(imgs) < 1 or len(imgs) > 5:
        return False
    for img in imgs:
        if not validate_img(img):
            return False
    return True

def validar_temas_actividad(temas_actividad):
    temas_validos = ['musica', 'deporte', 'ciencias', 'religion', 'politica', 'tecnologia', 'juegos', 'baile', 'comida', 'otro']
    
    if not temas_actividad:
        return False

    for item in temas_actividad:
        tema = item.get("tema")
        glosa_otro = item.get("glosa_otro")

        if tema not in temas_validos:
            return False

        if tema == "otro":
            if not glosa_otro or len(glosa_otro.strip()) < 3 or len(glosa_otro.strip()) > 15:
                return False
    
    return True

def validar_medios(medios):
    medios=['whatsapp','telegram','x','instagram','tiktok','otra']
    
    if not medios:
        return False

    for medio in medios:
        if medio== "whatsapp":
            if not validar_url(medios[medio]) or not validar_celular(medios[medio],True):
                return False
        elif medio== "telegram":
            if not validar_url(medios[medio]) or not validate_id(medios[medio]):
                return False
        elif medio== "x":
            if not validar_url(medios[medio]) or not validate_id(medios[medio]):
                return False
        elif medio== "instagram":
            if not validar_url(medios[medio]) or not validate_id(medios[medio]):
                return False
        elif medio== "tiktok":
            if not validar_url(medios[medio]) or not validate_id(medios[medio]):
                return False
        elif medio== "otra":
            if not validar_url(medios[medio]) or not validate_id(medios[medio]):
                return False
    return True

def validar_actividad(nombre,sector,comuna,fecha_inicio,fecha_termino,descripcion,temas,fotos,email,celular,medios):
    if not nombre or len(nombre) < 1 or len(nombre) > 200:
        return False
    if len(sector) > 100:
        return False
    if not comuna or len(comuna) < 1:
        return False
    if not validar_email(email):
        return False
    if not validar_celular(celular, True):
        return False
    if not validate_date(fecha_inicio, False):
        return False
    if not validate_end_date(fecha_inicio, fecha_termino):
        return False
    if not descripcion or len(descripcion) < 1 or len(descripcion) > 500:
        return False
    if not temas or len(temas) < 1 or len(temas) > 10:
        return False
    if not validate_img_list(fotos):
        return False
    if len(medios) > 5:
        return False
    return True
    
def validar_comentario(nombre, comentario,actividad_id):
    mensaje=""
    if nombre is None or len(nombre) < 3 or len(nombre) > 80:
        mensaje += "Servidor: El nombre debe tener entre 3 y 80 caracteres.\n"
    if comentario is None or len(comentario) < 5 or len(comentario) > 200:
        mensaje += "Servidor :El comentario debe tener entre 5 y 200 caracteres.\n"
    if actividad_id is None or len(str(actividad_id)) < 1:
        mensaje += "Servidor: Error interno, intentelo mas tarde. \n"
    if mensaje == "":
        return "", True  # todo OK
    else:
        return mensaje, False  # errores encontrados