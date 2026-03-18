#Termómetro simple

temperatura = int(input("Ingrese temperatura: "))

if temperatura < 10:
    print("Temperatura fría")
elif temperatura <= 25: #No es necesario utilizar un 'and', ya que la condición primero verifica si la temperatura < 10
    print("Temperatura templada")
else:
    print("Temperatura calurosa")