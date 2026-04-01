saldoInicial = int(input("Ingrese saldo inicial: "))

while True:

    saldoRetiro = int(input("Ingrese saldo a retirar: "))

    if saldoRetiro == 0:
        break

    if saldoRetiro > saldoInicial:
        print("Retiro rechazado")
        continue

    saldoInicial -= saldoRetiro
    print("Retiro realizado.")

print(f"Saldo final: {saldoInicial}")