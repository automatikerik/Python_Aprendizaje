edad = int(input("Ingresa por favor tu edad: "))
estudiante = input("¿Eres estudiante? ").strip().lower()

if edad < 12:
    print("\nEres un niño.")
elif edad >= 12 and edad <= 17:
    print("\nEres un adolescente.")
elif edad >= 18 and edad <= 64:
    print("\nEres adulto.")
else:
    print("\nEres adulto mayor.")

if estudiante == "si":
    print("Tienes descuento de estudiante.")