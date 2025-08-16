class EdadInvalidaError(Exception):
    pass

def verificar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser negativa.")
    print("Edad válida:", edad)

try:
    verificar_edad(-5)
except EdadInvalidaError as e:
    print("Error:", e)
