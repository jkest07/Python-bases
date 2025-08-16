try:
    a = int(input("Número: "))
    b = int(input("Divisor: "))
    print(a / b)
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
