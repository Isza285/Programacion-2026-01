contraseña = input("Ingrese contraseña: ")

intentos = 1

while True:

      adivinar = input("Ingrese contraseña a adivinar: ")
      if adivinar == contraseña:
          print("Acceso concedido")
          break

      intentos+=1

print(f"Numero de intentos: {intentos}")

