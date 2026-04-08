#Ejercicio 3

cantidad = int(input("Ingrese cantidad de numeros: "))

positivos = 0
negativos = 0

for i in range(cantidad):

  numero = int(input("Ingrese numero: "))

  if numero > 0:

    positivos += numero

  elif numero < 0:

    negativos += numero

  else:
    continue

print(f"Suma de numeros positivos: {positivos}")
print(f"Suma de numeros negativos: {negativos}")