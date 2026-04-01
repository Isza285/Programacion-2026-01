cantidad = int(input("Ingrese la cantidad de notas: "))

promedio = 0
i = 0

while i < cantidad:

  nota = float(input(f"Ingrese nota numero {i+1}: "))
  promedio += nota

  i += 1

promedio /= cantidad
print(f"El promedio de notas es de: {promedio}")