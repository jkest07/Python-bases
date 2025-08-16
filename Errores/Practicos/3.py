try:
    numero = int("123")
except ValueError:
    print("Error de conversión.")
else:
    print("Conversión exitosa:", numero)
finally:
    print("Bloque finally ejecutado.")
