#Calculadora área

ancho = int(input("Ingrese ancho: "))
alto = int(input("Ingrese alto: "))

area = ancho * alto

if area < 20:
    print("Rectángulo pequeño")
elif area >= 20 and area <= 50: #utilizando operadores lógicos
    print("Rectángulo mediano")
else:
    print("Rectángulo grande")