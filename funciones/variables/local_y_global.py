x = 10  # variable global

def mi_funcion():
    x = 5  # variable local
    print("Dentro:", x)

mi_funcion()
print("Fuera:", x)
