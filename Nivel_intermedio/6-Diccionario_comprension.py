"""
sintaxis basica:
{Clave_expr: valor_expr for item in iterable if condicion}
Antes del for va la expresión resultado

"""

cuadrados = {x:x**2 for x in range(10)}
#print(cuadrados)

cuadrados_pares = {x:x**2 for x in range (10) if x % 2 == 0}
#print(cuadrados_pares)

diccionario = {"a":1, "b":2, "c":3}
dicc_invertido = {v:k for k,v in diccionario.items()}
#print(dicc_invertido)

tuplas = [("a", 1), ("b", 2), ("c", 3)]
diccionario = {k:v for k,v in tuplas}
#print(type(diccionario))

claves = ["a", "b", "c"]
diccionario = {clave:0 for clave in claves} #clave:valor 

print(diccionario)
