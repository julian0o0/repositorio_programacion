from random import randint as r

def crear_matriz(filas, columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            num=r(1,1000)
            matriz[i].append(num)
    return matriz
    
def imprimir(matriz):
    for i in matriz:
        print(i)
def numero(matriz):
    mayor=matriz[0][0]
    menor=matriz[0][0]
    for fila in matriz:
        for valor in fila:
            if valor > mayor:
                mayor = valor
            if valor < menor:
                menor = valor
    print('el numero mayor es ', mayor)
    print('el numero menor es ',menor)
def posicion(matriz):
    mayor = matriz[0][0]
    menor = matriz[0][0]
    pos_mayor = (0, 0)
    pos_menor = (0, 0)
    
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            valor = matriz[fila][columna]
            if valor > mayor:
                mayor = valor
                pos_mayor = (fila, columna)
            if valor < menor:
                menor = valor
                pos_menor = (fila, columna)
    print("La posición del número menor es:", pos_menor)
    print("La posición del número mayor es:", pos_mayor)
def ordenar(matriz):
    elementos_ordenados = sorted([valor for fila in matriz for valor in fila])
    for fila in matriz:
        for columna in range(len(fila)):
            fila[columna] = elementos_ordenados.pop(0)
    return matriz

def main():
    matriz= crear_matriz(filas,columnas)
    imprimir(matriz)
    numero(matriz)
    posicion(matriz)
    matriz_ordenada = ordenar(matriz)
    print("Matriz original ordenada de menor a mayor:")
    imprimir(matriz_ordenada)
if __name__=="__main__":
    filas=10
    columnas=5
    main()