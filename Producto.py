class Producto:
    def __init__(self, nombre, precio, categoria):
        self.id = None
        self.nombre = nombre
        self.precio =precio
        self.categoria = categoria

    def print_info(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Categoria: {self.categoria}")

    def actualizar_precio(self, cambio_porcentaje, está_elevado):
        if está_elevado:
            self.precio += self.precio * (cambio_porcentaje/100)
        else:
            self.precio += self.precio * (cambio_porcentaje/100)

