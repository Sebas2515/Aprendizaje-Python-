"""
Descripcion 
Dado un registro de ventas diarias en una lista de diccionarios, generar un resumen con el total
de ventas y la cantidad de articulos vendidos 
"""

def resumen_ventas(ventas):
    # Paso 1: Inicializar los contadores
    total_ventas = 0 
    total_articulos = 0 
    # Paso 2: Recorre la lista de ventas 
    for venta in ventas: 
        total_ventas += venta['precio'] * venta['cantidad']
        total_articulos += venta['cantidad']
    # Paso 3: Devolver resultados 
    return total_ventas, total_articulos

ventas = [
    {'precio': 10, 'cantidad': 2},
    {'precio': 5, 'cantidad': 4},
    {'precio': 20, 'cantidad': 1}
]

print(resumen_ventas(ventas))
