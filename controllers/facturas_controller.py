from flask import render_template, request, redirect
from flask_controller import FlaskController 
from src.models.facturas import Facturas
from src.models.productos import Productos
from src.app import app

class FacturasController(FlaskController):    
    @app.route ('/lista_facturas')
    def lista_facturas():
        try:
            facturas = Facturas.traer_facturas()
            return render_template('lista_facturas.html',titulo='Lista facturas', facturas = facturas)
        except:
            return render_template('lista_facturas.html',titulo='Error de conexión a la base de datos')
    
    @app.route ('/facturas', methods=['GET','POST'])
    def facturas_html():
        productos = Productos.traer_productos()
        if request.method == 'POST':
            producto_id = request.form.get('producto_id')
            codigo = request.form.get('codigo')
            precio_unitario = request.form.get('precio_unitario')
            nombre_vendedor = request.form.get('nombre_vendedor')
            metodo_pago = request.form.get('metodo_pago')
            nombre_comprador = request.form.get('nombre_comprador')
            documento_identidad = request.form.get('documento_identidad')
            telefono = request.form.get('telefono')
            factura_almacenar = Facturas(producto_id,codigo,precio_unitario,nombre_vendedor,metodo_pago,nombre_comprador,documento_identidad,telefono)
            factura_repetida =  Facturas.traer_factura_por_codigo(codigo)
            if factura_repetida:
                return render_template('facturas.html'
                                    ,titulo='Crear Factura'
                                    ,errorFactura = 'El codigo no se puede repetir'
                                    ,factura_almacenar = factura_almacenar
                                    ,productos=productos)
            try:
                Facturas.crear_factura(factura_almacenar)
            except:            
                return render_template('facturas.html',titulo='Error al registrar en la base de datos')    
        return render_template('facturas.html', titulo='Crear Factura', productos=productos)
    
    