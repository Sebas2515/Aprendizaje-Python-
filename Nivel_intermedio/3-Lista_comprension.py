"""
[expresion for elemento in iterable if condicion]
"""

"""
#comprension de listas
cuadrados = [x**2 for x in range(10)]
print(cuadrados)
print(type(cuadrados))

#Metodo tradicional
cuadrados = []
for x in range(10):
    cuadrados.append(x**2)
print(cuadrados)
"""
"""
#Comprension de listas
numeros = [1,2,3,4,5,6,7,8,9,10]
pares = [x for x in numeros if x % 2 == 0]
print(pares)

#Metodo Tradicional 
pares = []
for x in numeros:
    if x % 2 == 0:
        pares.append(x)
print(pares)
"""
"""
Muchos programadores lo interpretan así:

[x → “una lista que contiene x”

for x in numeros → recorro cada x en la lista numeros

if x % 2 == 0 → me quedo solo con los x pares

x → pongo ese x dentro de la nueva lista

pares = […] → asigno el resultado
"""

#Comprension de listas - sirve mas que todo para operaciones simples 
palabras=["Python", "Django", "Django","Flask"]
longitudes= [len(palabra) for palabra in palabras]
print(longitudes)

#Metodo Tradicional
longitudes = []
for palabra in palabras:
    longitudes.append(len(palabra))
print(longitudes)

#conteo a traves del metodo tradicional
conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1
print(conteo)


