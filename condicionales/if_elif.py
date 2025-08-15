a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
print("Calculadora")
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")

opc = int(input("Ingrese una opcion: "))

if opc == 1:
    print("El resultado de la suma es: ", a + b)
elif opc == 2:
    print("El resultado de la resta es: ", a - b)
elif opc == 3:
    print("El resultado de la multiplicacion es: ", a * b)
elif opc == 4:
    if b != 0:
        print("El resultado de la division es: ", a / b)
    else:
        print("Error: No se puede dividir por cero")
