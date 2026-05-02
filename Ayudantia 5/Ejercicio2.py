#Ejercicio 2: Conteo temperaturas

bajoCero = 0
tempMin = 3000000 #Para comparar

for i in range(7):

  temperatura = int(input(f"Ingrese temperatura {i+1}:"))

  if temperatura < 0:

    bajoCero += 1


  if temperatura < tempMin:

    tempMin = temperatura


print (f"Temperaturas bajo cero: {bajoCero}")
print (f"Temperatura minima: {tempMin}")
