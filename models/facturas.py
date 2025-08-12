from sqlalchemy import Column, Integer, String, Numeric
from src.models import session, Base

class Facturas(Base):
    __tablename__ = 'facturas'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(300), nullable=False)
    codigo = Column(String(300), unique=True, nullable=False)
    precio_unitario = Column(String(300), nullable=False)
    nombre_vendedor = Column(String(300), nullable=False)
    metodo_pago = Column(String(300), nullable=False)
    nombre_comprador = Column(String(300), nullable=False)
    documento_identidad = Column(String(20), nullable=False)
    telefono = Column(String(20), nullable=False)

    def __init__(self, descripcion, codigo, precio_unitario, nombre_vendedor, metodo_pago, nombre_comprador, documento_identidad, telefono):
        self.descripcion = descripcion
        self.codigo = codigo
        self.precio_unitario = precio_unitario
        self.nombre_vendedor = nombre_vendedor
        self.metodo_pago = metodo_pago
        self.nombre_comprador = nombre_comprador
        self.documento_identidad = documento_identidad
        self.telefono = telefono
   
    def crear_factura(factura):
        factura = session.add(factura)
        session.commit()
        return factura
    
    def traer_facturas():
       facturas = session.query(Facturas).all()
       return facturas
    
    def traer_factura_por_codigo(codigo):
        factura = session.query(Facturas).filter(Facturas.codigo == codigo).first()
        return factura
    
    def eliminar_factura(factura):
        session.delete(factura)
        session.commit()