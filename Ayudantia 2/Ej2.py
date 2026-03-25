#Creamos el archivo invitados.txt
""""
%%writefile invitados.txt
Ana
Juan
Carlos
"""
#Codigo del ejercicio

with open("invitados.txt") as documento:
  for i in documento:
    nombre = i.strip()
    print(f"Nombre: {nombre}")
