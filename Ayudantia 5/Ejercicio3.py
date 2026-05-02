#Ejercicio 3: Invertir frase

palabra = input("Ingrese frase: ")

resultado = ""

for i in palabra:

  resultado = i + resultado
  # Aca a cada letra del ciclo se va añadiendo como a una "pila"
  # Por lo que cada letra va quedando hacia el final.

print(f"Frase invertida: {resultado}")