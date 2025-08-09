print("Calcudadora de Operadores Aritméticos")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Potencia")
print("6. Módulo")
print("7. Salir")
opc = int(input("Seleccione una opción (1-7): "))

if opc == 1:
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    print(f"La suma de {a} y {b} es: {a + b}")
elif opc == 2:  
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    print(f"La resta de {a} y {b} es: {a - b}") 
elif opc == 3:
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    print(f"La multiplicación de {a} y {b} es: {a * b}")
elif opc == 4:
    print("Desea 1. Division normal 2. Division entera: ")
    op = int(input("Ingrese una opción: "))
    if op == 1:
        a = float(input("Ingrese el dividendo: "))
        b = float(input("Ingrese el divisor: "))
        if b != 0:
            print(f"La división de {a} entre {b} es: {a / b}")
        else:
            print("Error: División por cero no permitida.") 
    elif op == 2:
        a = int(input("Ingrese el dividendo: "))
        b = int(input("Ingrese el divisor: "))
        if b != 0:
            print(f"La división entera de {a} entre {b} es: {a // b}")
elif opc == 5:
    a = float(input("Ingrese la base: "))
    b = float(input("Ingrese el exponente: "))
    print(f"{a} elevado a {b} es: {a ** b}")
    
elif opc == 6:  
        a = int(input("Ingrese el dividendo: "))
        b = int(input("Ingrese el divisor: "))
        if b != 0:
            print(f"El módulo de {a} entre {b} es: {a % b}")
elif opc == 7:
    print("Saliendo del programa.")
else:
    print("Opción no válida. Por favor, seleccione una opción entre 1 y 7.")



