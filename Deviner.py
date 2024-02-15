import random

Nombre = random.randint(1, 100)

NombreSaisie = 0

Tentatives = 1

while (Nombre != NombreSaisie) and (Tentatives != 4) :
    print(f"C'est votre tentative {Tentatives}")
    NombreSaisie = int(input("Essayer de deviner le nombre : "))

    if(Nombre < NombreSaisie) :
        print("le nombre que vous avez saisie est plus grand .")
        Tentatives += 1
    else :
        print("Le nombre que vous avez saisie est plus petit")
        Tentatives += 1
   
if(Nombre == NombreSaisie) :
    print("Vous avez bien trouvee le nombre :) ")
else : 
    print("Malheureusement vous n'avez pas trouvee le nombre ( ")