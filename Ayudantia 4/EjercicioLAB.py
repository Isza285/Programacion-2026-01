#EJERCICIO TIPO LABORATORIO

aceptar = 0
rechazar = 0
empate = 0

cantidadUniversidades = int(input("Número de universidades: "))

for i in range(cantidadUniversidades):

  universidad = input(f"Universidad N{i+1}: ")

  aceptanVoto = 0
  rechazanVoto = 0
  nuloVoto = 0
  blancoVoto = 0

  while True:

    voto = input("Voto: ")

    if voto == "A" or voto == "a":

      aceptanVoto += 1

    elif voto == "R" or voto == "r":

      rechazanVoto += 1

    elif voto == "N" or voto == "n":

      nuloVoto += 1
    
    elif voto == "B" or voto == "b":

      blancoVoto += 1

    elif voto == "X" or voto == "x":

      break

    else:

      print("Input invalido, intente de nuevo.")
  
  print(f"{universidad}: {aceptanVoto} aceptan, {rechazanVoto} rechazan, {blancoVoto} blancos, {nuloVoto} nulos")

  if aceptanVoto > rechazanVoto:

    aceptar += 1
  
  elif rechazanVoto > aceptanVoto:

    rechazar += 1

  else:

    empate += 1

print("Resultados finales: ")
print(f"Universidades que aceptan: {aceptar}")
print(f"Universidades que rechazan: {rechazar}")
print(f"Universidades con empate: {empate}")