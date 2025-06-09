from sqlalchemy.orm import sessionmaker,declarative_base, relationship,joinedload
from sqlalchemy import create_engine, Column, String, BigInteger, ForeignKey,DateTime,Enum,desc
import datetime


DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# --- Models ---

class Region(Base):
    __tablename__ = 'region'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre= Column(String(200), nullable=False)
    comuna = relationship("Comuna", back_populates="region")

class Comuna(Base):
    __tablename__ = 'comuna'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre= Column(String(200), nullable=False)
    region_id= Column(BigInteger, ForeignKey('region.id'), nullable=False)
    actividad = relationship("Actividad", back_populates="comuna")
    region = relationship("Region", back_populates="comuna")    

class Actividad(Base):
    __tablename__ = 'actividad'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    comuna_id= Column(BigInteger, ForeignKey('comuna.id'), nullable=False)
    sector= Column(String(100), nullable=False)
    nombre= Column(String(200), nullable=False)
    email= Column(String(100), nullable=False)
    celular= Column(String(15))
    dia_hora_inicio=Column(DateTime, nullable=False)
    dia_hora_termino=Column(DateTime)
    descripcion= Column(String(500))
    comuna=relationship("Comuna", back_populates="actividad")
    foto = relationship("foto", back_populates="actividad")
    contactar_por = relationship("contactar_por", back_populates="actividad")
    actividad_tema = relationship("actividad_tema", back_populates="actividad")
    comentario = relationship("Comentario", back_populates="actividad", cascade="all, delete-orphan")


class foto(Base):
    __tablename__ = 'foto'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    ruta_archivo= Column(String(300), nullable=False)
    nombre_archivo= Column(String(300), nullable=False)
    actividad_id= Column(BigInteger, ForeignKey('actividad.id'), nullable=False)
    actividad = relationship("Actividad", back_populates="foto")

class contactar_por(Base):
    __tablename__ = 'contactar_por'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre= Column(Enum('whatsapp', 'telegram', 'X', 'instagram', 'tiktok', 'otra'), nullable=False)
    identificador= Column(String(150), nullable=False)
    actividad_id= Column(BigInteger, ForeignKey('actividad.id'), nullable=False)
    actividad = relationship("Actividad", back_populates="contactar_por")


class actividad_tema(Base):
    __tablename__ = 'actividad_tema'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    tema= Column(Enum('música', 'deporte', 'ciencias', 'religión', 'política', 'tecnología', 'juegos', 'baile', 'comida', 'otro') , nullable=False)
    glosa_otro= Column(String(15))
    actividad_id= Column(BigInteger, ForeignKey('actividad.id'), nullable=False)
    actividad = relationship("Actividad", back_populates="actividad_tema")

class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    actividad_id = Column(BigInteger, ForeignKey('actividad.id'), nullable=False)
    nombre = Column(String(80), nullable=False)
    texto = Column(String(200), nullable=False)
    fecha = Column(DateTime, nullable=False)
    actividad = relationship("Actividad", back_populates="comentario")

def get_actividades(page_size,page=1):
    session = SessionLocal()
    offset = (page - 1) * page_size
    actividades = session.query(Actividad).options(
        joinedload(Actividad.comuna).joinedload(Comuna.region),
        joinedload(Actividad.foto),
        joinedload(Actividad.actividad_tema)  # Cargar comuna y region
    ).order_by(Actividad.id.desc()).offset(offset).limit(page_size).all()
    session.close()
    return actividades

def crear_actividad(nombre, sector, comuna_id, dia_hora_inicio, dia_hora_termino, descripcion,temas,fotos, email, celular,medios):
    session = SessionLocal()
    nueva_actividad = Actividad(nombre=nombre, sector=sector, comuna_id=comuna_id, dia_hora_inicio=dia_hora_inicio, dia_hora_termino=dia_hora_termino, descripcion=descripcion, email=email, celular=celular)
    for tema in temas:
        nuevo_actividad_tema = actividad_tema(tema=tema['tema'], glosa_otro=tema['glosa_otro'])
        nueva_actividad.actividad_tema.append(nuevo_actividad_tema)
    for medio, identificador in medios.items():
        nuevo_contactar_por = contactar_por(nombre=medio, identificador=identificador)
        nueva_actividad.contactar_por.append(nuevo_contactar_por)
    for foto_dict in fotos:
        nueva_foto = foto(ruta_archivo=foto_dict["ruta_archivo"], nombre_archivo=foto_dict["nombre_archivo"])
        nueva_actividad.foto.append(nueva_foto)
            
    session.add(nueva_actividad)
    session.commit()
    print(f"Actividad {nombre} creada")
    session.close()

def listar_fotos_actividad(actividad_id):
    session = SessionLocal()
    fotos = session.query(foto).filter_by(actividad_id=actividad_id).all()
    session.close()
    return fotos
def listar_temas_actividad(actividad_id):
    session = SessionLocal()
    temas = session.query(actividad_tema).filter_by(actividad_id=actividad_id).all()
    session.close()
    return temas

def get_pages(page_size):
    session = SessionLocal()
    count = session.query(Actividad).count()
    session.close()
    return count // page_size + (1 if count % page_size > 0 else 0)

def get_actividades_por_dia():
    session=SessionLocal()
    actividades = session.query(Actividad).all()
    actividades_por_dia = {}
    for actividad in actividades:
        dia = actividad.dia_hora_inicio.date().strftime("%Y-%m-%d")
        if not actividades_por_dia.get(dia):
            actividades_por_dia[dia] = 0
        actividades_por_dia[dia] += 1
    session.close()
    resultado = [
        {"date": dia, "cantidad": cantidad}
        for dia, cantidad in actividades_por_dia.items()
    ]
    return resultado

def get_actividades_por_tipo():
    session=SessionLocal()
    tipos=set()
    actividades_por_tipo = {}
    actividades = session.query(actividad_tema).all()
    for actividad in actividades:
        if actividad.tema == "otro":
            tema = actividad.glosa_otro if actividad.glosa_otro else "otro"
        else:
            tema = actividad.tema  
        if tema not in tipos:
            tipos.add(tema)
            actividades_por_tipo[tema] = 0
        actividades_por_tipo[tema] += 1
    session.close()
    return actividades_por_tipo

def get_actividades_por_mes_hora():
    session= SessionLocal()
    meses= list(range(1, 13))
    horas=["mañana", "mediodia", "tarde"]
    actividades_por_mes_hora = {mes: {hora: 0 for hora in horas} for mes in meses}
    actividades = session.query(Actividad).all()
    for actividad in actividades:
        mes = actividad.dia_hora_inicio.month
        hora = actividad.dia_hora_inicio.hour
        if hora < 12:
            hora_key = "mañana"
        elif hora < 14:
            hora_key = "mediodia"
        else:
            hora_key = "tarde"
        actividades_por_mes_hora[mes][hora_key] += 1    
    session.close()
    return actividades_por_mes_hora

def crear_comentario(actividad_id,nombre,texto):
    session= SessionLocal()
    fecha = datetime.datetime.now()
    nuevo_comentario = Comentario(actividad_id=actividad_id, nombre=nombre, texto=texto, fecha=fecha)
    session.add(nuevo_comentario)
    session.commit()
    session.close()
    print(f"Comentario creado para la actividad {actividad_id} por {nombre}")

def listar_comentarios(actividad_id):
    session=SessionLocal()
    comentarios = session.query(Comentario).filter_by(actividad_id=actividad_id).order_by(desc(Comentario.id)).all()
    session.close()
    comentarios_actividad={}
    for comentario in comentarios:
        comentarios_actividad[comentario.id] = {
            "nombre": comentario.nombre,
            "texto": comentario.texto,
            "fecha": comentario.fecha.strftime("%Y-%m-%d %H:%M:%S")
        }
    return comentarios_actividad

