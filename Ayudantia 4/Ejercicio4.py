#Ejercicio 4

i = 0

while True:

  i += 1
  nota = float(input("Ingrese nota: "))

  if nota >= 4.0:
    break

print(f"Intentos requeridos: {i}")
print(f"Nota del intento: {nota}")