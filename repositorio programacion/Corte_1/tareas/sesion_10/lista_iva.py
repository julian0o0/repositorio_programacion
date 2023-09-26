def leer_productos():
    productos = {}
    with open("sesion_10/Alimentos.txt", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split(',')
            if len(partes) == 3:
                codigo, producto, iva = partes[0], partes[1], float(partes[2])
                productos[codigo] = (producto, iva)
    return productos

def calcular_iva(productos, codigo, valor_neto):
    if codigo in productos:
        producto, iva = productos[codigo]
        valor_base = valor_neto / (1 + iva)
        valor_del_iva = valor_neto - valor_base
        return valor_base, valor_del_iva, producto
    else:
        return None, None, None

productos = leer_productos()
print("Lista de productos y sus valores de IVA:")
for codigo, (producto, iva) in productos.items():
    print(f"Código: {codigo}, Producto: {producto}, IVA: {iva}")

while True:
    codigo = input("Ingrese el código del producto (o escriba 'salir' para terminar): ")
    if codigo.lower() == 'salir':
        break
    valor_neto = float(input("Ingrese el valor neto del producto: "))
    valor_base, valor_del_iva, producto = calcular_iva(productos, codigo, valor_neto)
    if valor_base is not None:
        print(f"Producto: {producto}")
        print(f"Valor Base: {valor_base:.2f}")
        print(f"Valor del IVA: {valor_del_iva:.2f}")
    else:
        print("El código del producto no se encuentra en la lista.")