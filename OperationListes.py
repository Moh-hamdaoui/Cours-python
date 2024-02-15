Chaine = "Malek est un vrai samourai"

Liste = Chaine.split()

print(f"La liste  : {Liste}")

print(f"Le nombre de mots dans la liste est : {len(Liste)}")

ListeFusionne = " ".join(Liste)

print(f"La liste Fusionne  : {ListeFusionne}")

if "bonjour" in Chaine :
    print("Votre variable contient le mot 'Bonjour'")
else :
    print("Votre variable contient pas le mot 'Bonjour'")    


