#Ejercicio 2

estudiantes = int(input("Ingrese cantidad de estudiantes: "))

aprobados = 0
reprobados = 0

i = 0
while i < estudiantes:
  nota = float(input(f"Ingrese nota estudiante numero {i+1}:"))

  if nota >= 4.0:

    aprobados += 1

  else:

    reprobados += 1

  i+=1

print(f"Estudiantes aprobados: {aprobados}")
print(f"Estudiantes reprobrados: {reprobados}")

