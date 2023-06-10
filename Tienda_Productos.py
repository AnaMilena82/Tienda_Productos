class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos =[]

    def agregar_producto(self, nuevo_producto):
        self.productos.append(nuevo_producto)

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos:
                print(producto.nombre)

    def inflacion(self, aumento_porcentaje):
        for producto in self.productos:
            producto.actualizar_precio(aumento_porcentaje, está_elevado=True)    

    def hacer_liquidacion(self, categoria, porcentaje_descuento):
        for producto in self.productos:
            if producto.categoria == categoria:
                producto.actualizar_precio(porcentaje_descuento, está_elevado=False)


class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio =precio
        self.categoria = categoria

    def print_info(self):
        print(f"Nombre: self.nombre")
        print(f"Precio: self.precio")
        print(f"Categoria: self.categoria")

    def actualizar_precio(self, cambio_porcentaje, está_elevado):
        if está_elevado:
            self.precio += self.precio * (cambio_porcentaje/100)
        else:
            self.precio += self.precio * (cambio_porcentaje/100)

#  creando una instancia de Tienda.
tienda = Tienda("Hites")

#  y algunas instancias de la clase Producto
producto1 = Producto("Camiseta", 20, "Ropa")
producto2 = Producto("Zapatos", 50, "Calzado")
producto3 = Producto("Libro", 15, "Libros")



#  Agrega esas instancias a la instancia de tienda 
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

#BONUS NINJA: Agrega el método inflación a la clase Tienda
tienda.inflacion(5)  # Aumenta los precios en un 5%

#Agrega el método hacer_liquidación a la clase Tienda
tienda.hacer_liquidacion("Ropa", 10)  # Aplica un descuento del 10% a los productos de la categoría "Ropa"


# Mostrar productos de la tienda
tienda.mostrar_productos()







