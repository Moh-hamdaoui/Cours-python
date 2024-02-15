ListeChaine = ["Malek", "Nagaakira", "Mitsuakira", "Tsunaakira", "Tsunanaga"]

def Chaine(Liste, Index):
    try :
       return Liste[Index]
    except IndexError :
        return "Erreur : L'index specifie est en dehors des limites de la liste"

CasValide = Chaine(ListeChaine, 3)
print(CasValide)

CasInvalide = Chaine(ListeChaine, 9)
print(CasInvalide)