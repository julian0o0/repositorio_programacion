import random as rd
def main():
    aleatorios = [rd.randint(0,1000) for _ in range(14)]
    print(aleatorios)
    aleatorios.sort()
    print("Lista Ordenada: ", aleatorios)

if __name__=="__main__":
    main()