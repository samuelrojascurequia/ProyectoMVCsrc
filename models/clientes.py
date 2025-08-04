from sqlalchemy import Column, Integer, String
from src.models import session, Base

class Clientes(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(300), nullable=False)
    apellidos = Column(String(300), nullable=False)
    email = Column(String(300))
    ciudad = Column(String(300), nullable=False)
    departamento = Column(String(300), nullable=False)
    direccion = Column(String(300), nullable=False)
    documento_identidad = Column(String(20),unique=True, nullable=False)
    telefono = Column(String(20), nullable=False)

    def __init__(self, nombres, apellidos, email, ciudad, departamento, direccion, documento_identidad, telefono):
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.ciudad = ciudad
        self.departamento = departamento
        self.direccion = direccion
        self.documento_identidad = documento_identidad
        self.telefono = telefono
   
    def crear_cliente(cliente):
        cliente = session.add(cliente)
        session.commit()
        return cliente
    
    def traer_clientes():
       clientes = session.query(Clientes).all()
       return clientes 

    def traer_cliente_por_documento_identidad(documento_identidad):
        cliente = session.query(Clientes).filter(Clientes.documento_identidad == documento_identidad).first()
        return cliente
    
    def traer_cliente_por_id(id):
        return session.query(Clientes).get(id)

    def eliminar_cliente(cliente):
        session.delete(cliente)
        session.commit()

    
    