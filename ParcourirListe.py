Liste = [5,8,7,"Salut",5,"Azul",5,"Salut","Azul",7,8,"Salam"]

ListeTrier = []

for element in Liste :
    if element not in ListeTrier :
        ListeTrier.append(element)

print(f"La liste trier est : {ListeTrier}") 