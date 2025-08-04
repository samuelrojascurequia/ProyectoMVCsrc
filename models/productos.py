from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from src.models import session, Base
from src.models.categorias import Categorias

class Productos(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    codigo = Column(String(9), unique=True, nullable=False)
    descripcion = Column(String(300), unique=True)
    unidad_medida = Column(String(3), nullable=False)
    cantidad_inventario = Column(String(100), nullable=False)
    precio_unitario = Column(String(300), nullable=False)
    categoria = Column(Integer, ForeignKey('categorias.id'), nullable=False)

    def __init__(self, codigo, descripcion, unidad_medida, cantidad_inventario, precio_unitario, categoria):
        self.codigo = codigo
        self.descripcion = descripcion
        self.unidad_medida = unidad_medida
        self.cantidad_inventario = cantidad_inventario
        self.precio_unitario = precio_unitario
        self.categoria = categoria
   
    def crear_producto(producto):
        producto = session.add(producto)
        session.commit()
        return producto
    
    def traer_productos():
       productos = session.query(Productos).all()
       return productos 
    
    def traer_producto_por_descripcion(descripcion):
        producto = session.query(Productos).filter(Productos.descripcion == descripcion).first()
        return producto
    
    def traer_producto_por_codigo(codigo):
        producto = session.query(Productos).filter(Productos.codigo == codigo).first()
        return producto
    
    def actualizar_producto(self):
        session.commit()

    def eliminar_producto(producto):
        session.delete(producto)
        session.commit()

    

