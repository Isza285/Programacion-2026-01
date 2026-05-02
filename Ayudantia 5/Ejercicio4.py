#Ejercicio 4: Promedio

suma = 0
cantidad = 0

while True:

    numero = int(input("Ingrese un número (0 para salir): "))

    if numero == 0:
        break

    suma += numero
    cantidad += 1


if cantidad > 0:
    print(f"El promedio es: {suma/cantidad}")
else:
    print("No se ingresaron numeros")