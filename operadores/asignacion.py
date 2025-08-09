
print("Calculadora de Operadores de Asignación")
print("1. Asignación simple")
print("2. Asignación con suma")
print("3. Asignación con resta")
print("4. Asignación con multiplicación")
print("5. Asignación con división")
print("6. Salir")
opc = int(input("Seleccione una opción (1-6): "))
x = float(input("Ingrese un número: "))
if opc == 1:
    y = x
    print(f"Asignación simple: y = {y}")
elif opc == 2:
    y = x
    y += 5
    print(f"Asignación con suma: y = {y}")
elif opc == 3:
    y = x
    y -= 3
    print(f"Asignación con resta: y = {y}")
elif opc == 4:
    y = x
    y *= 2
    print(f"Asignación con multiplicación: y = {y}")
elif opc == 5:
    y = x
    y /= 2  
    print(f"Asignación con división: y = {y}")
elif opc == 6:
    print("Saliendo del programa.")
else:
    print("Opción no válida. Por favor, seleccione una opción entre 1 y 6.")