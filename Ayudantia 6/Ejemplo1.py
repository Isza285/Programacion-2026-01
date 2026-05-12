#Ejemplo 1
lista = []

for i in range(5):

    num = int(input())
    lista.append(num)

suma = 0

for elemento in lista:
    suma += elemento

print(suma / len(lista))