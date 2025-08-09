a = True
b = False

print("Calculadora de Operadores Lógicos")
print("1. AND")
print("2. OR")
print("3. NOT")
print("4. XOR")
print("5. Salir")
opc = int(input("Seleccione una opción (1-5): "))

if opc == 1:
    print(f"{a} AND {b} es: {a and b}")
elif opc == 2:
    print(f"{a} OR {b} es: {a or b}")
elif opc == 3:
    print(f"NOT {a} es: {not a}")
    print(f"NOT {b} es: {not b}")
elif opc == 4:
    print(f"{a} XOR {b} es: {a ^ b}")
elif opc == 5:
    print("Saliendo del programa.")
else:
    print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")