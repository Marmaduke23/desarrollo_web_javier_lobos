from flask import Flask,render_template,request
from database import db
from werkzeug.utils import secure_filename
import os
import filetype
import hashlib
from utils.validations import validar_actividad

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET"])
def index():
    data=[]
    for act in db.get_actividades(page_size=5):
        data.append({
            "id": act.id,
            "nombre": act.nombre,
            "sector": act.sector,
            "comuna": act.comuna.nombre,
            "region": act.comuna.region.nombre,
            "dia_hora_inicio": act.dia_hora_inicio.strftime("%d/%m/%Y %H:%M"),
            "dia_hora_termino": act.dia_hora_termino.strftime("%d/%m/%Y %H:%M") if act.dia_hora_termino else None,
            "descripcion": act.descripcion,
            "tema": [tema.glosa_otro if tema.tema == "otro" else tema.tema for tema in act.actividad_tema 
                     ] if act.actividad_tema else None,
            "foto": f"{act.foto[0].ruta_archivo}" if act.foto else None
        })
  
    return render_template("index.html",data=data)

@app.route("/agregar_actividad", methods=["GET","POST"])
def agregar_actividad():
    if request.method == "POST":
        # get data from form
        region = request.form.get("select-region")
        comuna = request.form.get("select-comuna")
        sector = request.form.get("sector")
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        celular = request.form.get("celular")
        medios=['whatsapp','telegram','x','instagram','tiktok','otra']
        medios_contacto = {
            medio: request.form.get(f"{medio}-id")
            for medio in medios
            if medio in request.form}
        dia_hora_inicio = request.form.get("inicio")
        dia_hora_termino = request.form.get("termino")
        if dia_hora_termino == "":
            dia_hora_termino = None
        descripcion = request.form.get("descripcion")
        temas=['musica','deporte','ciencias','religion','politica','tecnologia','juegos','baile','comida','otro']
        temas_actividad = [
            {
                "tema": tema,
                "glosa_otro": (request.form.get("otro-text") if tema == "otro" else None)
            }
            for tema in temas
            if tema in request.form.getlist("tema")]
        print(request.form.getlist)
        fotos= request.files.getlist("fotos")
        print(fotos)
        lista_fotos = []

        if validar_actividad(
            nombre=nombre,
            sector=sector,
            comuna=comuna,
            fecha_inicio=dia_hora_inicio,
            fecha_termino=dia_hora_termino,
            descripcion=descripcion,
            temas=temas_actividad,
            fotos=fotos,
            email=email,
            celular=celular,
            medios=medios_contacto):

            for foto in fotos:
                # 1. generate random name for img
                _filename = hashlib.sha256(
                    secure_filename(foto.filename) # nombre del archivo
                    .encode("utf-8") # encodear a bytes
                    ).hexdigest()
                _extension = filetype.guess(foto).extension
                print(_extension)
                img_filename = f"{_filename}.{_extension}"

                # 2. save img as a file
                ruta=os.path.join(app.config["UPLOAD_FOLDER"], img_filename)
                print(f"Guardando imagen en: {ruta}")
                foto.save(ruta)

                lista_fotos.append({
                    "ruta_archivo": f"uploads/{img_filename}",
                    "nombre_archivo": foto.filename
                })

            db.crear_actividad(
                nombre=nombre,
                sector=sector,
                comuna_id=comuna,
                dia_hora_inicio=dia_hora_inicio,
                dia_hora_termino=dia_hora_termino,
                descripcion=descripcion,
                temas=temas_actividad,
                fotos=lista_fotos,
                email=email,
                celular=celular,
                medios=medios_contacto

            )   
            return '',204
        else:
            error = "Error en los datos ingresados. Por favor, verifica los campos."
            return render_template("agregar_actividad.html",error=error)
    
    elif request.method == "GET":
        error=None
        return render_template("agregar_actividad.html",error=error)
    
@app.route("/lista_actividades", methods=["GET"])
def lista_actividades():
    page= request.args.get("page", 1, type=int)
    total_pages=db.get_pages(5)
    data=[]
    for act in db.get_actividades(page_size=5,page=page):
        data.append({
            "id": act.id,
            "email": act.email,
            "nombre": act.nombre,
            "sector": act.sector,
            "comuna": act.comuna.nombre,
            "region": act.comuna.region.nombre,
            "dia_hora_inicio": act.dia_hora_inicio.strftime("%d/%m/%Y %H:%M"),
            "dia_hora_termino": act.dia_hora_termino.strftime("%d/%m/%Y %H:%M") if act.dia_hora_termino else None,
            "descripcion": act.descripcion,
            "tema": [tema.glosa_otro if tema.tema == "otro" else tema.tema for tema in act.actividad_tema 
                     ] if act.actividad_tema else None,
            "fotos": [f"{foto.ruta_archivo}" for foto in act.foto] if act.foto else None,
            "page": page,
            
        })
        
    return render_template("lista_actividades.html",data=data,page=page,total_pages=total_pages)

@app.route("/informacion_actividad",methods=["GET","POST"])    
def informacion_actividad():
    if request.method == "POST":
        descripcion = request.form.get("descripcion")
        fecha_inicio = request.form.get("fecha_inicio")
        fecha_termino = request.form.get("fecha_termino")
        sector = request.form.get("sector")
        comuna = request.form.get("comuna")
        nombre = request.form.get("nombre")
        id= request.form.get("id")
        email = request.form.get("email")
        page= request.form.get("page", 1, type=int)
        print(page)
        fotos= db.listar_fotos_actividad(id)
        fotos = [f"{foto.ruta_archivo}" for foto in fotos] if fotos else None
      
        temas = db.listar_temas_actividad(id)
        temas= [tema.glosa_otro if tema.tema == "otro" else tema.tema for tema in temas 
                     ] if temas else None


        data={
            "descripcion": descripcion,
            "fecha_inicio": fecha_inicio,
            "fecha_termino": fecha_termino,
            "sector": sector,
            "comuna": comuna,
            "nombre": nombre,
            "fotos": fotos,
            "email": email,
            "temas": temas,
            "page": page,
        }



        return render_template("informacion_actividad.html",data=data)

@app.route("/estadisticas", methods=["GET"])
def estadisticas():
    return render_template("estadisticas.html")

if __name__ == "__main__":
    app.run(debug=True)
