lista1 = [3, 5, 7, 2, 8, 1, 4, 6]
lista2 = ["juan", "pedro", "maria", "ana", "luis", "carlos", "sofia", "lucia"]
lista3 = [lista1, lista2]

lista1.sort()
print("Lista 1 ordenada:", lista1)
for i in lista2:
    print(i)
    
print("Lista 3:", lista3)

lista3.append(["nuevo", "elemento"])
print("Lista 3 después de append:", lista3)
lista3.remove(lista1)
lista1.clear()
lista2.extend(["nuevo1", "nuevo2"])
print("Lista 2 después de extend:", lista2) 
lista2.insert(2, "insertado")
print("Lista 2 después de insert:", lista2)
lista2.pop()
print("Lista 2 después de pop:", lista2)
lista2.reverse()
print("Lista 2 después de reverse:", lista2)