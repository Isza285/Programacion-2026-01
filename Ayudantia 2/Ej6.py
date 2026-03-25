#Creamos el archivo ventas.txt
"""
%%writefile ventas.txt
40990
54990
150990
8990
"""
#Codigo del ejercicio

ventasTotales = 0
#Importante declarar la variable ventasTotales fuera del ciclo
#Si declaramos ventasTotales dentro del ciclo, en cada
#Iteración del ciclo la variable se volvera a declarar, por ende
#Perdera su valor acumulado anteriormente
with open("ventas.txt") as documento:

    for i in documento:

        venta = int(i.strip())
        ventasTotales += venta

print(f"Ventas totales del dia: {ventasTotales}")