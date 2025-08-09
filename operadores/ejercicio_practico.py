print("Calculadora de Operadores")
print("1. Operadores Aritméticos")
print("2. Operadores Lógicos")
print("3. Operadores de Cadena")
print("4. Operadores Racionales")
print("5. Operadores de Asignación")
print("6. Salir")

opc = int(input("Seleccione una opción (1-6): "))

if opc == 1:
    print("Calculadora de Operadores Aritméticos")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Módulo")
    print("7. Salir")
    op_arit = int(input("Seleccione una opción (1-7): "))
    if op_arit == 1:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"La suma de {a} y {b} es: {a + b}")
    elif op_arit == 2:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"La resta de {a} y {b} es: {a - b}")
    elif op_arit == 3:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"La multiplicación de {a} y {b} es: {a * b}")
    elif op_arit == 4:
        print("Desea 1. División normal  2. División entera")
        tipo_div = int(input("Ingrese una opción: "))
        if tipo_div == 1:
            a = float(input("Ingrese el dividendo: "))
            b = float(input("Ingrese el divisor: "))
            if b != 0:
                print(f"La división de {a} entre {b} es: {a / b}")
            else:
                print("Error: División por cero no permitida.")
        elif tipo_div == 2:
            a = int(input("Ingrese el dividendo: "))
            b = int(input("Ingrese el divisor: "))
            if b != 0:
                print(f"La división entera de {a} entre {b} es: {a // b}")
    elif op_arit == 5:
        a = float(input("Ingrese la base: "))
        b = float(input("Ingrese el exponente: "))
        print(f"{a} elevado a {b} es: {a ** b}")
    elif op_arit == 6:
        a = int(input("Ingrese el dividendo: "))
        b = int(input("Ingrese el divisor: "))
        if b != 0:
            print(f"El módulo de {a} entre {b} es: {a % b}")
    elif op_arit == 7:
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Por favor, seleccione una opción entre 1 y 7.")

elif opc == 2:
    a = True
    b = False
    print("Calculadora de Operadores Lógicos")
    print("1. AND")
    print("2. OR")
    print("3. NOT")
    print("4. XOR")
    print("5. Salir")
    op_log = int(input("Seleccione una opción (1-5): "))
    if op_log == 1:
        print(f"{a} AND {b} es: {a and b}")
    elif op_log == 2:
        print(f"{a} OR {b} es: {a or b}")
    elif op_log == 3:
        print(f"NOT {a} es: {not a}")
        print(f"NOT {b} es: {not b}")
    elif op_log == 4:
        print(f"{a} XOR {b} es: {a ^ b}")
    elif op_log == 5:
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")

elif opc == 3:
    t1 = "Hola"
    t2 = "Mundo"
    r = t1 + " " + t2
    print(r)
    print("\nHola mundo " * 3)

elif opc == 4:
    frase = "Operadores racionales"
    print("Operadores" in frase)
    print("Hola" in frase)

elif opc == 5:
    print("Calculadora de Operadores de Asignación")
    print("1. Asignación simple")
    print("2. Asignación con suma")
    print("3. Asignación con resta")
    print("4. Asignación con multiplicación")
    print("5. Asignación con división")
    print("6. Salir")
    op_asig = int(input("Seleccione una opción (1-6): "))
    x = float(input("Ingrese un número: "))
    if op_asig == 1:
        y = x
        print(f"Asignación simple: y = {y}")
    elif op_asig == 2:
        y = x
        y += 5
        print(f"Asignación con suma: y = {y}")
    elif op_asig == 3:
        y = x
        y -= 3
        print(f"Asignación con resta: y = {y}")
    elif op_asig == 4:
        y = x
        y *= 2
        print(f"Asignación con multiplicación: y = {y}")
    elif op_asig == 5:
        y = x
        y /= 2
        print(f"Asignación con división: y = {y}")
    elif op_asig == 6:
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Por favor, seleccione una opción entre 1 y 6.")

elif opc == 6:
    print("Saliendo del programa.")

else:
    print("Opción no válida. Por favor, seleccione una opción entre 1 y 6.")
