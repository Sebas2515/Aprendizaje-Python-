"""
Eliminar los duplicados de una lista de valores 
"""
"""
lista = [1, 2, 2, 3, 4, 4, 5]
conjunto = set(lista) #Castenado la lista en un conjunto 
lista_sin_duplicados = list(conjunto) #lo volvi a convertir en una lista
print(lista_sin_duplicados)
for numero in lista_sin_duplicados:
    print(numero)
"""

"""
Encontrar elementos comunes en dos conjuntos 
"""

"""
def encontrar_elementos_comunes(conjunto1, conjunto2):
    elementos_comunes = conjunto1.intersection(conjunto2)
    return elementos_comunes

#Ejemplo de uso 
conjunto1 = {1,2,3,4,5}
conjunto2 = {4,5,6,7,8}

comunes = encontrar_elementos_comunes(conjunto1, conjunto2)
print(comunes)
"""

###########################################################################################

"""
-Dos almacenes 
-Realizar operaciones en esos almacenes: 
    -Encontrar productos comunes 
    -Encontrar productos exclusivos de cada almacen 
    -Lista completa de todos los productos disponibles en ambos almacenes
"""

almacen_1 = {'laptop','mouse','teclado','monitor','impresora'}
almacen_2 = {'teclado','monitor','tablet','smartphone','impresora'}

#Productos Mas comunes en ambos almacenes 
productos_comunes = almacen_1.intersection(almacen_2)
print(f'Productos comunes en ambos almacenes: {productos_comunes}')

#Productos exclusivos de cada almacen
exclusivos_1 = almacen_1.difference(almacen_2)
exclusivos_2 = almacen_2.difference(almacen_1)
exclusivos = exclusivos_1, exclusivos_2
print(f'Productos exclusivos: {exclusivos}')

#Lista completa de todos los productos
lista_completa = almacen_1.union(almacen_2)
print(f'Lista completa de todos los productos: {lista_completa}')

