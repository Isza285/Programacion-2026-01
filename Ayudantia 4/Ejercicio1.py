#Ejercicio 1

horas = int(input("Ingrese horas estacionado: "))
monto = 0

if horas >= 1:

  monto+=500

if horas > 1:

  monto+= (horas - 1) * 750

print(f"Horas estacionado: {horas}")
print(f"Total a pagar: {monto}")