#Ejercicio 4

nombres = []

for i in range(5):

    nombre = input("Ingrese nombre: ")
    nombres.append(nombre)

nuevo = input("Nuevo nombre: ")
posicion = int(input("Posicion: "))

nombres.insert(posicion, nuevo)

print(nombres)