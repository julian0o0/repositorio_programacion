class Producto:
    def __init__(self, nombre, precio, cantidad_disponible=0):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad_disponible

    def obtener_info(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Cantidad Disponible: {self.cantidad}"

    def restar_cantidad(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return True
        else:
            print(f"No hay suficientes unidades de {self.nombre} disponibles.")
            return False

    def verificar_disponibilidad(self, cantidad):
        return cantidad <= self.cantidad


class Snack(Producto):
    def __init__(self, nombre, precio, cantidad_disponible, tipo):
        super().__init__(nombre, precio, cantidad_disponible)
        self.tipo = tipo

    def obtener_info(self):
        return super().obtener_info() + f", Tipo: {self.tipo}"


class Bebida(Producto):
    def __init__(self, nombre, precio, cantidad_disponible, tamano):
        super().__init__(nombre, precio, cantidad_disponible)
        self.tamano = tamano

    def obtener_info(self):
        return super().obtener_info() + f", Tamaño: {self.tamano}"


class Maquina:
    def __init__(self):
        self.productos = []
        self.ventas_totales = 0

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def realizar_venta(self, producto, cantidad):
        if producto.verificar_disponibilidad(cantidad):
            total_venta = producto.precio * cantidad
            producto.restar_cantidad(cantidad)
            self.ventas_totales += total_venta
            print(f"Venta realizada: {producto.nombre} x {cantidad}. Total: ${total_venta:.2f}")
        else:
            print(f"No se puede realizar la venta de {producto.nombre}.")

    def total_ventas(self):
        return f"Total de ventas: ${self.ventas_totales:.2f}"
snack1 = Snack("Galletas", 2.50, 10, "Salado")
bebida1 = Bebida("Refresco", 1.50, 20, "Grande")

maquina = Maquina()
maquina.agregar_producto(snack1)
maquina.agregar_producto(bebida1)

print(snack1.obtener_info())
print(bebida1.obtener_info())

maquina.realizar_venta(snack1, 3)
maquina.realizar_venta(bebida1, 2)

print(snack1.obtener_info())
print(bebida1.obtener_info())

print(maquina.total_ventas())