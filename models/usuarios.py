from sqlalchemy import Column, Integer, String, Numeric
from src.models import session, Base

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombres = Column(String(300), nullable=False)
    apellidos = Column(String(300), nullable=False)
    email = Column(String(300), nullable=False)
    direccion = Column(String(300), nullable=False)
    telefono = Column(String(300), nullable=False)
    puesto = Column(String(300), nullable=False)
    documento_identidad = Column(String(20),unique=True, nullable=False)
    contraseña = Column(String(300), nullable=False)

    def __init__(self, nombres, apellidos, email, direccion, telefono, puesto, documento_identidad, contraseña):
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.puesto = puesto
        self.documento_identidad = documento_identidad
        self.contraseña = contraseña
   
    def crear_usuario(usuario):
        usuario = session.add(usuario)
        session.commit()
        return usuario
    
    def traer_usuarios():
       usuarios = session.query(Usuarios).all()
       return usuarios
    
    def traer_usuario_por_documento_identidad(documento_identidad):
        usuario = session.query(Usuarios).filter(Usuarios.documento_identidad == documento_identidad).first()
        return usuario
    
    def traer_usuario_por_id(id):
        return session.query(Usuarios).get(id)

    def eliminar_usuario(usuario):
        session.delete(usuario)
        session.commit()