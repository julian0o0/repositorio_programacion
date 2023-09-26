def mayor(lista):
    if len(lista) == 1:
        return lista[0]
    mitad = len(lista) // 2
    izq = lista[:mitad]
    der = lista[mitad:]
    max_izq = mayor(izq)
    max_der = mayor(der)
    return max(max_izq, max_der)
mi_lista = [12, 34, 56, 78, 90, 123, 45, 67]
mayor = mayor(mi_lista)
print("El mayor elemento en la lista es:", mayor)