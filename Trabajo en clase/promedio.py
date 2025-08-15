estudiantes = {
    "Juan": {"notas": [5, 9, 4, 5, 1]},
    "Ana": {"notas": [6, 7, 8, 9, 10]},
    "Luis": {"notas": [4, 5, 6, 7, 8]},
    "Maria": {"notas": [10, 9, 8, 7, 6]},
    "Carlos": {"notas": [3, 4, 5, 6, 7]}
}

for nombre, datos in estudiantes.items():
    promedio = sum(datos["notas"]) / len(datos["notas"])
    estudiantes[nombre]["promedio"] = promedio

print(estudiantes)