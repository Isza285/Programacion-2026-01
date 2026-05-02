#Ejercicio 5: Carrera 100 puntos

sumaTotal = 0
contador = 0

while sumaTotal < 100:
    numero = int(input("Ingrese un numero: "))
    sumaTotal += numero
    contador += 1

print(f"Suma total: {sumaTotal}")
print(f"Se necesitaron {contador} numeros")