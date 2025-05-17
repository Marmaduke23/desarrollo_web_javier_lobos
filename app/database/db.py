from sqlalchemy.orm import sessionmaker,declarative_base, relationship,joinedload
from sqlalchemy import create_engine, Column, String, BigInteger, ForeignKey,DateTime,Enum


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
