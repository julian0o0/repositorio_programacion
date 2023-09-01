def main():
    lista=[]
    final=[]
    valor=1
    while valor>=1:
        valor=int(input("Ingrese un valor entero:"))
        if valor>=0:
            lista.append(valor)
        else:  
            print(lista)
    for valor in lista:
        if valor not in final:
            final.append(valor)
    print(final)

if __name__=="__main__":
    main()