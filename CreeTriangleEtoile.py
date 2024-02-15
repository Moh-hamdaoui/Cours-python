NombreEtoile = int(input("Donnez la hauteur de pyramide : "))

for i in range(1, NombreEtoile+1):
    
    for j in range(1,i+1) :
        print("*", end="")
    print()    