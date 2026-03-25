#Creamos el archivo menu.csv
""""
%%writefile menu.csv
Empanada,1500
Completo,2000
Chorrillana,4000
"""
#Codigo del ejercicio

with open("menu.csv") as archivo:
  for i in archivo:
    linea = i.strip().split(',')
    comida = linea[0]
    precio = linea[1]
    print(f"El precio de un(a): {comida} es de {precio}")