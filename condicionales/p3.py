calc = { 
    0: "CALCULADORA",
    1: "1. Suma",
    2: "2. Resta",
    3: "3. Multiplicacion",
    4: "4. Division"
}
for key, value in calc.items():
    print(f"{key}: {value}")

opc = int(input("Ingrese el numero de la operacion que desea realizar: "))
print(calc[opc])

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

if opc == 1:
    print("La suma de los dos numeros es: ", a + b)
elif opc == 2:
    print("El resultado de la resta es: ", a - b)
elif opc == 3:
    print("El resultado de la multiplicacion es: ", a * b)
elif opc == 4:
    if b != 0:
        print("El resultado de la division es: ", a / b)
    else:
        print("Error: No se puede dividir por cero")
