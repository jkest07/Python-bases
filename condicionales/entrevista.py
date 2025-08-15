print("\t¿Te gustaria empezar la entrevista? (si/no)")
if input().lower() == "si":
    print("¡Genial! Comencemos con algunas preguntas.")
    
p2_entrevista = ["¿Como te llamas?",
                "¿Cuantos años tienes?",
                "¿Donde vives?",
                "¿A qué te dedicas?",
                "¿Cuál es tu pasatiempo favorito?",
                "¿Tienes mascotas?",
                "¿Cuál es tu comida favorita?",
                "¿Qué música te gusta escuchar?",
                "¿Tienes algún sueño o meta en la vida?",
                "¿Qué te gustaría aprender en el futuro?"]

print("=== ENTREVISTA ===")

for pregunta in d_entrevista:
    respuesta = input(pregunta + " ")
    print(f"Respuesta: {respuesta}")
        print("Gracias por tu respuesta, que tengas buen dia\n")
else:
    print("No hay problema, si cambias de opinión, aquí estaré para ayudarte.")
    exit()






