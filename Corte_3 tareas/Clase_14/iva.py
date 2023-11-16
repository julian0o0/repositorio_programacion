class Articulo:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_precio_bruto(self):
        return self.precio

    def calcular_iva(self):
        return 0


class AlimentoExento(Articulo):
    def calcular_iva(self):
        return 0


class Alimento5IVA(Articulo):
    def calcular_iva(self):
        return self.precio * 0.05


class Alimento19IVA(Articulo):
    def calcular_iva(self):
        return self.precio * 0.19


def calcular_total_iva(articulos):
    total_precio_bruto = 0
    total_iva = 0

    for articulo in articulos:
        total_precio_bruto += articulo.calcular_precio_bruto()
        total_iva += articulo.calcular_iva()

    return total_precio_bruto, total_iva

alimento1 = AlimentoExento("Arroz", 2500)
alimento2 = Alimento5IVA("Manzanas", 1200)
alimento3 = Alimento19IVA("Galletas", 3000)

canasta = [alimento1, alimento2, alimento3]

total_precio_bruto, total_iva = calcular_total_iva(canasta)

print(f"Total Precio Bruto: ${total_precio_bruto:.2f}")
print(f"Total IVA: ${total_iva:.2f}")