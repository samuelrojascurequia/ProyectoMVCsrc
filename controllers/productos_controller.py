from flask import render_template, request, redirect
from flask_controller import FlaskController 
from src.models.productos import Productos
from src.models.categorias import Categorias
from src.app import app

class ProductosController(FlaskController):
    @app.route ('/lista_productos')
    def lista_productos_html():
        try:
            productos = Productos.traer_productos()
            return render_template('lista_productos.html', titulo='lista Productos', productos = productos)
        except:
            return render_template('lista_productos.html', titulo='Error de conexion a la base de datos')
    
    @app.route ('/formulario_producto', methods=['GET','POST'])
    def formulario_producto_html():
        categorias = Categorias.traer_categorias() 
        if request.method == 'POST':
            codigo = request.form.get('codigo')
            descripcion = request.form.get('descripcion')
            unidad_medida = request.form.get('unidad_medida')
            cantidad_inventario = request.form.get('cantidad_inventario')
            precio_unitario = request.form.get('precio_unitario')
            categoria = request.form.get('categoria')
            producto_almacenar = Productos(codigo,descripcion,unidad_medida,cantidad_inventario,precio_unitario,categoria)
            producto_repetido_desc =  Productos.traer_producto_por_descripcion(descripcion)
            if producto_repetido_desc:
                return render_template('formulario_producto.html'
                                    ,titulo='Crear Producto'
                                    ,errorProducto = 'La descripcion no se puede repetir'
                                    ,categorias = categorias
                                    ,producto_almacenar = producto_almacenar)
            producto_repetido_cod =  Productos.traer_producto_por_codigo(codigo)
            if producto_repetido_cod:
                return render_template('formulario_producto.html'
                                    ,titulo='Crear Producto'
                                    ,errorCodigo = 'El codigo no se puede repetir'
                                    ,categorias = categorias
                                    ,producto_almacenar = producto_almacenar)
            try:
                Productos.crear_producto(producto_almacenar)
            except:            
                return render_template('formulario_producto.html',titulo='Error al registrar en la base de datos',categorias = categorias)    
        return render_template('formulario_producto.html', titulo='Crear Producto',categorias = categorias)
    
    @app.route('/editar_producto/<string:codigo>', methods=['GET', 'POST'])
    def editar_producto(codigo):
        producto = Productos.traer_producto_por_codigo(codigo)
        categorias = Categorias.traer_categorias()

        if request.method == 'POST':
            producto.descripcion = request.form['descripcion']
            producto.codigo = request.form['codigo']
            producto.unidad_medida = request.form['unidad_medida']
            producto.cantidad_inventario = request.form['cantidad_inventario']
            producto.precio_unitario = request.form['precio_unitario']
            producto.categoria = request.form['categoria']
            try:
                from src.models import session
                session.commit()
                return redirect('/lista_productos')
            except:
                return render_template('formulario_producto.html', titulo='Error al editar', producto_almacenar=producto)

        return render_template('formulario_producto.html', titulo='Editar producto', producto_almacenar=producto, categorias=categorias)

    @app.route('/borrar_producto/<codigo>', methods=['GET'])
    def borrar_producto(codigo):
        producto = Productos.traer_producto_por_codigo(codigo)
        if producto:
            Productos.eliminar_producto(producto)
        return redirect('/lista_productos')