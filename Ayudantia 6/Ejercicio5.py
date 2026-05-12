#Ejercicio 5

numeros = []

for i in range(5):

  valor = int(input("Ingrese número: "))
  numeros.append(valor)

listaFinal = []

for i in numeros:

  if i not in listaFinal:

    listaFinal.append(i)

print(listaFinal)