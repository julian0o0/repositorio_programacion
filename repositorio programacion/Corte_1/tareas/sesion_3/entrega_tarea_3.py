import math as m
print('opciones disponibles:\n'\
    ,'1.ingresar una letra del alfabeto\n 2.Tarifa del parqueadero\n 3.construccion de triangulos')

a=input('Seleccione una opcion: ')

if (a.lower()=='uno') or (a=='1'):
    letra=input('ingrese una letra del alfabeto: ')
    if(letra.lower()=='a')or(letra.lower()=='e')or(letra.lower()=='i')or(letra.lower()=='u')or(letra.lower()=='o')or(letra.lower()=='A')or(letra.lower()=='E')or(letra.lower()=='I')or(letra.lower()=='U')or(letra.lower()=='O'):
        print('vocal')
    else: 
        print('consonante')
elif(a.lower()=='dos') or (a=='2'):
    tiempo=int(input('¿cuanto tiempo se demoro en el parqueadero?'))
    valor=tiempo*139
    iva=valor*0.19
    total=iva+valor
    final=round(total)
    print(' precio del servicio:',valor,'\n'\
    ,'el valor del iva es:',iva,'\n El valor total seria:',total,'\n El valor total a pagar seria',final)
    
elif(a.lower()=='tres') or (a=='3'):
    lado1=float(input('Ingrese el lado a: '))
    lado2=float(input('Ingrese el lado b: '))
    lado3=float(input('Ingrese el lado c: '))
    suma1=lado1+lado2
    suma2=lado2+lado3
    suma3=lado3+lado1
    if suma1>lado3:
        print('si se puede hacer un triangulo')
        if lado1==lado2==lado3:
            print('el triangulo es equilatero')
        elif (lado1==lado2)or(lado1==lado3)or(lado2==lado3):
            print('el triangulo es isosceles')
        else:
            print('el triangulo es escaleno')
    elif suma2>lado1:
        print('si se puede hacer un triangulo')
        if lado1==lado2==lado3:
            print('el triangulo es equilatero')
        elif (lado1==lado2)or(lado1==lado3)or(lado2==lado3):
            print('el triangulo es isosceles')
        else:
            print('el triangulo es escaleno')
    elif suma3>lado2:
        print('si se puede hacer un triangulo')
        if lado1==lado2==lado3:
            print('el triangulo es equilatero')
        elif (lado1==lado2)or(lado1==lado3)or(lado2==lado3):
            print('el triangulo es isosceles')
        else:
            print('el triangulo es escaleno')
    else:
        print('no se puede hacer un triangulo')
else:
    print('seleccione una opcion valida')