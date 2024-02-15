ListeTuple = [(3, 5, 7, 9), (2, 6, 7, 10, 3), (2, 9), (3, 6, 0, 6, 12, 1)]

TupleInverser = [tuple(reversed(element)) for element in ListeTuple]

print(f"Le tuple inverser est : {TupleInverser}")