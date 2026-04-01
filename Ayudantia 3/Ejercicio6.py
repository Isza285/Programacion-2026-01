total = 0
numeroIngresado = 0

while True:
    
    numeroIngresado = int(input("Ingresar numero: "))

    if numeroIngresado == -1:
        break

    total += numeroIngresado

print(f"Resultado total: {total}")
