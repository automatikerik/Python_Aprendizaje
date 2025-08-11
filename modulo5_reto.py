tareas = []

def ver_tareas(lista):
    if not tareas:
        print("No hay tareas")
    else:
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def agregar_tarea(lista):
    tarea = input("Ingresa la tarea para agregarla: ")
    lista.append(tarea)
    print("Tarea Agregada.")

def eliminar_tarea(lista):
    ver_tareas(tareas)
    if tareas:
        eliminar = int(input("Ingresa el numero de la tarea para eliminarla: "))
        if 1 <= eliminar <= len(tareas):
            tareas.pop(eliminar - 1)
            print("Tarea Eliminada.")
        else:
            print("NUmero INvalido.")

opcion = 0
while opcion != 4:
    print("--- MENU ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")
    opcion = int(input("Eligue una opcion: "))

    if opcion == 1:
        ver_tareas(tareas)
    elif opcion == 2:
        agregar_tarea(tareas)
    elif opcion == 3:
        eliminar_tarea(tareas)
    elif opcion == 4:
        print("Hasta luego.")
    else:
        print("Opcion invalida.")