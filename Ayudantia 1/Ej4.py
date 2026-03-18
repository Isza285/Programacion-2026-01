#Guardia de acceso

edad = int(input("Ingrese edad: "))

if edad < 18:
    print("Acceso denegado")
else:
    print("Acceso autorizado")