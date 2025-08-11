from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController 
from src.models.facturas import Facturas
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
        if request.method == 'POST':
            descripcion = request.form.get('descripcion')
            codigo = request.form.get('codigo')
            precio_unitario = request.form.get('precio_unitario')
            nombre_vendedor = request.form.get('nombre_vendedor')
            metodo_pago = request.form.get('metodo_pago')
            nombre_comprador = request.form.get('nombre_comprador')
            documento_identidad = request.form.get('documento_identidad')
            telefono = request.form.get('telefono')
            factura_almacenar = Facturas(descripcion,codigo,precio_unitario,nombre_vendedor,metodo_pago,nombre_comprador,documento_identidad,telefono)
            factura_repetida =  Facturas.traer_factura_por_codigo(codigo)
            if factura_repetida:
                return render_template('facturas.html'
                                    ,titulo='Crear Factura'
                                    ,errorFactura = 'El codigo no se puede repetir'
                                    ,factura_almacenar = factura_almacenar)
            try:
                Facturas.crear_factura(factura_almacenar)
            except:            
                return render_template('facturas.html',titulo='Error al registrar en la base de datos')    
        return render_template('facturas.html', titulo='Crear Factura')
    
    @app.route('/editar_factura/<string:codigo>', methods=['GET', 'POST'])
    def editar_factura(codigo):
        factura = Facturas.traer_factura_por_codigo(codigo)

        if request.method == 'POST':
            factura.descripcion = request.form.get('descripcion')
            factura.precio_unitario = request.form.get('precio_unitario')
            factura.nombre_vendedor = request.form.get('nombre_vendedor')
            factura.metodo_pago = request.form.get('metodo_pago')
            factura.nombre_comprador = request.form.get('nombre_comprador')
            factura.documento_identidad = request.form.get('documento_identidad')
            factura.telefono = request.form.get('telefono')
            try:
                from src.models import session
                session.commit()
                return redirect('/lista_facturas')
            except:
                return render_template('facturas.html', titulo='Error al editar', factura_almacenar=factura)

        return render_template('facturas.html', titulo='Editar factura', factura_almacenar=factura)
    
    @app.route('/borrar_factura/<codigo>', methods=['GET'])
    def borrar_factura(codigo):
        factura = Facturas.traer_factura_por_codigo(codigo)
        if factura:
            Facturas.eliminar_factura(factura)
        return redirect(url_for('lista_facturas'))