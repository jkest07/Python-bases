# Manejo de errores
try:
    numero = int(input("Ingresa un número: "))
    division = 10 / numero
    print("Resultado:", division)
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
except ValueError:
    print("Debes ingresar un número válido.")
finally:
    print("Fin del programa.")
