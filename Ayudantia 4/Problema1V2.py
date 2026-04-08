#Problema 1 con for
total = 0
max = 0
for i in range(30):

  ahorro = int(input(f"Ingrese dinero a ahorra dia {i+1}: "))
  total += ahorro

  if ahorro > max:
    max = ahorro


print(f"Total ahorrado en el mes: {total}")
print(f"Promedio de ahorro diario: {total/30}")
print(f"Mayor monto ahorrado en un dia {max}")