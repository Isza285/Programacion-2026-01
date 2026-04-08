#Problema 2 con for
maxPalabra = ""
maxLetras = 0
for i in range(10):
  palabra = input(f"Ingrese palabra {i+1}: ")

  if len(palabra) > maxLetras:
    maxLetras = len(palabra)
    maxPalabra = palabra

print(f"Palabra mas larga: {maxPalabra}")
print(f"Letras de la palabra: {maxLetras}")