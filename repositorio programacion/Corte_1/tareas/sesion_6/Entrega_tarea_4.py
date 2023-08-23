import math as m
while True:
    print('opciones disponibles:\n'\
        ,'1.ingresar un numero para saber sus divisores\n 2.mostrar el producto de dos numeros\n 3.serie de fibbonacci')

    a=input('Seleccione una opcion: ')

    if (a.lower()=='uno') or (a=='1'):
        num=int(input('ingrese un numero: '))
        i=1
        for i in range (1,num):
            res=num%i
            if num==0:
                print('ningun numero es divisible entre 0')
            elif res==0:
                print(i)
        print(num)
        
    elif(a.lower()=='dos') or (a=='2'):
        i=0
        producto=0
        n1=int(input('ingrese el primer numero: '))
        n2=int(input('ingrese el segundo numero: '))
        for i in range(i,n1):
            producto=producto+n2
            if n1< 0 or n2<0:
                print('el producto es:','-',producto)
        print('el producto es:',producto)
    
    elif(a.lower()=='tres') or (a=='3'):
        x=0
        y=1
        z=0
        n=int(input('ingrese cuantos numeros desea generar '))
        print("1",end=" ")
        for i in range(1,n):
            z=x+y
            print(f"{z}",end=" ")
            x=y
            y=z
        print("")
    else:
        print('seleccione una opcion valida')