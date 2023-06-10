from Tienda import Tienda
from Producto import Producto

#  creando una instancia de Tienda.
tienda = Tienda("Hites")

#  y algunas instancias de la clase Producto
producto1 = Producto("Camiseta", 20, "Ropa")
producto1.id = 1 #Actualiza la clase de producto para dar a cada producto un id único.
producto2 = Producto("Zapatos", 50, "Calzado")
producto2.id =2
producto3 = Producto("Libro", 15, "Libros")
producto3.id=3



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
producto1.print_info()

#Actualiza el método vender_producto para aceptar el id único.
tienda.vender_producto(2)  # Vender el producto con ID 2





