# Ejercicio 6

palabra = input("Ingrese una palabra: ")
vocales = 0

for i in palabra:
    #la variable "i" representa una letra en cada iteración del ciclo.
    if i in "aeiouAEIOU":
        vocales += 1

print(f"La palabra contiene {vocales} vocales.")