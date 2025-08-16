def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b

try:
    print(dividir(10, 0))
except ZeroDivisionError as e:
    print("Error:", e)
