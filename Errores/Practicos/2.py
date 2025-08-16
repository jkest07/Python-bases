try:
    lista = [1, 2, 3]
    print(lista[5])  
except IndexError:
    print("Error: índice inválido.")
except Exception as e:
    print("Otro error:", e)
