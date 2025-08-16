try:
    numero = int(input("Ingresa un número: "))
except ValueError:
    print("Eso no es un número válido.")
else:
    print("Número válido:", numero)
finally:
    print("Fin del programa.")
