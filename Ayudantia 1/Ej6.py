#Clasificador de velocidad

velocidad = int(input("Ingrese velocidad: "))

if velocidad < 30:
    print("Velocidad lenta")
elif velocidad > 80:
    print("Velocidad rápída")
else:
    print("Velocidad normal")
