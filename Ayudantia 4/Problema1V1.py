#Problema 1 con while
i = 1
total = 0
max = 0
while i < 31:
  ahorro = int(input(f"Ingrese dinero a ahorrar dia {i}: "))
  total += ahorro

  if ahorro > max:
    max = ahorro

  i+=1

print(f"Total ahorrado en el mes: {total}")
print(f"Promedio de ahorro diario: {total/30}")
print(f"Mayor monto ahorrado en un dia {max}")