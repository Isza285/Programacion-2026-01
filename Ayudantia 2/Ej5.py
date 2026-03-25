#Creamos el archivo notas.txt
"""
%%writefile notas.txt
5.5
3.2
6.0
3.9
"""
#Codigo del ejercicio

with open("notas.txt") as documento:

    for i in documento:
     
        nota = float(i.strip()) 
        #Leyendo una linea por cada iteración del ciclo
        if nota >= 4.0:
            print(f"Nota {nota} aprobada")
        else:
            print(f"Nota {nota} reprobada")
#Casteamos como float el texto de cada línea, de esta manera
#podremos comparar los valores como numeros