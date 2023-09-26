import random as rd
def main():
    comision=rd.randrange(10,50)
    usd=4108
    eur=4454
    cny=563
    jpy=28
    pen=1106
    print('opciones disponibles:\n\
        ,1.conversion de cop a cualquier divisa disponible\n 2.ver tasas de cambio y su comision')
    n=input('seleccione una opcion')
    if (n.lower()=='uno') or (n=='1'):
        print('las divisas disponibles son:\n\
              1.USD\n, 2. EUR\n, 3.CNY\n, 4. JPY\n, 5.PEN')
        dov=input('seleecione una opcion')
        if (dov.lower()=='uno') or (dov=='1'):
            cantidad=float(input('que cantidad desea convertir?'))
            total=cantidad/usd+(usd*comision*0.01)
            total=round(total,2)
            print('cambio:',total,'cambio:')
        if (dov.lower()=='dos') or (dov=='2'):
            cantidad=float(input('que cantidad desea convertir?'))
            total=cantidad/eur+(eur*comision*0.01)
            total=round(total,2)
            print('cambio:',total,'cambio:')
        if (dov.lower()=='tres') or (dov=='3'):
            cantidad=float(input('que cantidad desea convertir?'))
            total=cantidad/cny+(cny*comision*0.01)
            total=round(total,2)
            print('cambio:',total,'cambio:')
        if (dov.lower()=='cuatro') or (dov=='4'):
            cantidad=float(input('que cantidad desea convertir?'))
            total=cantidad/jpy+(jpy*comision*0.01)
            total=round(total,2)
            print('cambio:',total,'cambio:')
        if (dov.lower()=='cinco') or (dov=='5'):
            cantidad=float(input('que cantidad desea convertir?'))
            total=cantidad/pen+(pen*comision*0.01)
            total=round(total,2)
            print('cambio:',total,'cambio:')
    if (n.lower()=='dos') or (n=='2'):
        print('divisa:USD, tasa: 4108, Comision:',comision,'\n\
               divisa:EUR, tasa: 4454, Comision:',comision,'\n\
                divisa:CNY, tasa: 563, Comision:',comision,'\n\
                divisa:JPY, tasa: 28, Comision:',comision,'\n\
                divisa:PEN, tasa: 1106, Comision:',comision,)
    else:
        print('opcion invalida')
if __name__=='__main__':
    main()