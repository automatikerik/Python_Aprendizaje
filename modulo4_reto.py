def saludar(nombre):
    print(f"Hola, {nombre}")

def es_mayor(edad):
    return edad >= 18

def calcular_area(base, altura):
    area = base * altura / 2
    return area
    
nombre = input("Por favor ingresa tu nombre: ")
edad = int(input("Ahora ingresa tu edad: "))

saludar(nombre)
if es_mayor(edad):
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

base = int(input("Muy bien, para calcular el area del triangulo dime la base: "))
altura = int(input("Ahora dime la altura: "))

print("El area del triangulo es:", calcular_area(base, altura))