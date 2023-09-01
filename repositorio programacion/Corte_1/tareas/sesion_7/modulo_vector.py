import math as m
def coordenadas():
    x1=float(input('escriba la coordenada en eje x del primer punto '))
    y1=float(input('escriba la coordenada en eje y del primer punto '))
    x2=float(input('escriba la coordenada en eje x del segundo punto '))
    y2=float(input('escriba la coordenada en eje y del segundo punto '))
    mod=m.sqrt(((x2-x1)**2)-((y2-y1)**2))
    compox=(x2-x1)
    compoy=(y2-y1)
    print('el modulo del vector que ingreso es:',mod)
    print('sus componente rectangular en x es',compox,'y su componente en y es',compoy)




if __name__=="__main__":
    coordenadas()