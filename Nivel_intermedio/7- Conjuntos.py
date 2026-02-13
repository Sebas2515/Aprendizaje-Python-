# Objetivo, En esta entrega aprenderemos a utilizar conjuntos en Python para organizar y 
# manipular datos de elementos únicos  también utilizar operaciones matemáticas  como unión e 
# intersección etc
# set son conjuntos
# no son ordenados, son elementos unicos, son mutables

# Operaciones con conjuntos sirven para la estructura de datos.
conjunto = {1,2,3}
conjunto_dos = set([1,2,3])

conjunto.add(4)
#conjunto.remove(2)
#conjunto.discard(1)

elemento = conjunto.pop()

print(elemento)
print(conjunto)

frutas = {'manzana','banana','naranja'}
citrus = {'naranja','limón','pomelo'}

print(frutas.union(citrus))
print(frutas.intersection(citrus))
print(frutas.difference(citrus))
print(frutas.symmetric_difference(citrus))

conjunto1 = {1,2,3,4}
conjunto2 = {3,4,5,6}

diferencia = conjunto1 - conjunto2
print(diferencia)

diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print(diferencia_simetrica)
