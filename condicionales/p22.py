operaciones = ["Suma", "Resta", "Multiplicación", "División"]

print("\nOperaciones disponibles:")
for i, operacion in enumerate(operaciones, 1):
    print(f"{i}. {operacion}")

numeros = []

numeros.append(int(input("\nIngrese el primer número: ")))
numeros.append(int(input("Ingrese el segundo número: ")))
opc = int(input("Ingrese el número de la operación que desea realizar: "))

resultados = []

if opc == 1:
    resultado = numeros[0] + numeros[1]
    resultados.append(resultado)
    print(f"\nLa suma de {numeros[0]} + {numeros[1]} es: {resultados[0]}")
    
elif opc == 2:
    resultado = numeros[0] - numeros[1]
    resultados.append(resultado)
    print(f"\nLa resta de {numeros[0]} - {numeros[1]} es: {resultados[0]}")
    
elif opc == 3:
    resultado = numeros[0] * numeros[1]
    resultados.append(resultado)
    print(f"\nLa multiplicación de {numeros[0]} * {numeros[1]} es: {resultados[0]}")
    
elif opc == 4:
    if numeros[1] != 0:
        resultado = numeros[0] / numeros[1]
        resultados.append(resultado)
        print(f"\nLa división de {numeros[0]} / {numeros[1]} es: {resultados[0]}")
    else:
        print("\nError: No se puede dividir por cero")
        
else:
    print("\nOpción no válida")
