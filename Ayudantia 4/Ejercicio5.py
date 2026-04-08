#Ejercicio 5
cantidadCompras = int(input("Ingrese cantidad de compras: "))

total = 0

for i in range(cantidadCompras):

  compra = int(input("Ingrese monto de compra: "))

  if compra > 50000:

    total += compra * 0.9

  elif compra > 20000:

    total += compra * 0.95

  else:

    total += compra

print(f"Total recaudado: {total}")

