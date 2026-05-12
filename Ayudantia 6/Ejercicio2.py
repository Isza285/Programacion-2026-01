#Ejercicio 2
numeros = []

for i in range(5):

  valor = int(input("Ingrese número: "))
  numeros.append(valor)

positivos = 0
negativos = 0

for i in numeros:

  if i >= 0:
    positivos +=1
  else:
    negativos +=1

print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")