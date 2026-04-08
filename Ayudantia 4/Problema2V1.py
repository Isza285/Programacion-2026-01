#Problema 2 con while
i = 0
maxPalabra = ""
maxLetras = 0
while i < 10:
  palabra = input(f"Ingrese palabra {i+1}: ")

  if len(palabra) > maxLetras:
    maxLetras = len(palabra)
    maxPalabra = palabra

  i+=1

print(f"Palabra mas larga: {maxPalabra}")
print(f"Letras de la palabra: {maxLetras}")