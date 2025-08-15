calc = ["1 suma", "2 resta", "3 multiplicacion", "4 division"]
for i in calc:
    print(i)

opc = input("ingrese la opcion: ")
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))


if opc == "1":
    print("El resultado de la suma es: ", a + b)
elif opc == "2":
    print("El resultado de la resta es: ", a - b)
elif opc == "3":
    print("El resultado de la multiplicacion es: ", a * b)
elif opc == "4":
    if b != 0:
        print("El resultado de la division es: ", a / b)
    else:
        print("Error: No se puede dividir por cero")

