nombres = ["Erik", "Alan", "Kevin", "Miroslava", "Jose"]

for nombre in nombres:
    print("Hola,", nombre)
    
opcion = ""
contador = 0

while opcion != "salir":
    opcion = input("Para salir del programa escribe salir: ")
    if opcion != "salir":
        print("Sigo aqui...")
        contador += 1
        
print(f"Escribiste {contador} antes de salir.")