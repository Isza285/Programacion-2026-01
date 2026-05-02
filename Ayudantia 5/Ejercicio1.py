#Ejercicio 1: Factura de productos

totalAcumulado = 0

while True:

  valorProducto = int(input("Ingrese valor neto del producto(Sin IVA): "))

  if valorProducto == 0:
    break
  elif valorProducto < 0:
    print("Valor invalido")
    continue


  totalAcumulado += valorProducto


totalIva = totalAcumulado*0.19

print(f"Subtotal: {totalAcumulado}")
print(f"IVA: {totalIva}")
print(f"Total: {totalAcumulado+totalIva}")