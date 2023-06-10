class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos =[]

    def agregar_producto(self, nuevo_producto):
        self.productos.append(nuevo_producto)

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos:
                producto.print_info()

    def inflacion(self, aumento_porcentaje):
        for producto in self.productos:
            producto.actualizar_precio(aumento_porcentaje, está_elevado=True)    

    def hacer_liquidacion(self, categoria, porcentaje_descuento):
        for producto in self.productos:
            if producto.categoria == categoria:
                producto.actualizar_precio(porcentaje_descuento, está_elevado=False)

    def vender_producto(self, id_producto):
        for producto in self.productos:
            if producto.id == id_producto:
                self.productos.remove(producto)
                print("Producto vendido:")
                producto.print_info()
                return
        print("No se encontró ningún producto con el ID proporcionado.")

