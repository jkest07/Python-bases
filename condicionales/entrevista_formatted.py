opc = int(input("¿Te gustaría realizar una entrevista? (1. Sí, 2. No): "))
if opc == 1:
    print("¡Genial! Comencemos con algunas preguntas.")
    
    preguntas_entrevista = [
        "¿Cómo te llamas?",
        "¿Cuántos años tienes?",
        "¿Dónde vives?",
        "¿A qué te dedicas?",
        "¿Cuál es tu pasatiempo favorito?",
        "¿Tienes mascotas?",
        "¿Cuál es tu comida favorita?",
        "¿Qué música te gusta escuchar?",
        "¿Tienes algún sueño o meta en la vida?",
        "¿Qué te gustaría aprender en el futuro?"
    ]

    print("=== ENTREVISTA ===")

    for pregunta in preguntas_entrevista:
        respuesta = input(pregunta + " ")
        print(f"Respuesta: {respuesta}")
    print("Gracias por tu respuesta, que tengas buen día\n") 
elif opc == 2:
    print("No hay problema, si cambias de opinión, aquí estaré para ayudarte.")

else:
    print("Opción no válida, por favor ingresa 1 o 2.")

