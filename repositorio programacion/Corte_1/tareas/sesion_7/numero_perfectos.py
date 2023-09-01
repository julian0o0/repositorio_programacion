def main():
    for i in range(1,9900000000000):
        j=2
        suma=0
        while j<=i:
            if i%j==0:
                suma+= i//j
            j+=1
        if suma==i:
            print(i)
if __name__=="__main__":
    main()