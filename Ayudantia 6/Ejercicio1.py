#Ejercicio 1
numeros = []

for i in range(5):

    num = int(input("Ingrese numero: "))
    numeros.append(num)

buscar = int(input("Numero a buscar: "))

if buscar in numeros:
    print("El numero existe en la lista")
else:
    print("El numero no existe")