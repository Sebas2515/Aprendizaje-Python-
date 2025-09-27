"""
Descripcion: 
Realziar un analisis de ventas que contiene un registro de ventas, con columnos como fecha 
productos, cantidad, precio. El objetivo es generar un resumen de total de ventas por producto
y el ingreso total por día.
"""
import csv 
from collections import defaultdict

def analizar_ventas(archivo_csv):
    ventas_por_producto= defaultdict(float)
    ingresos_por_dia = defaultdict(float)

    with open(archivo_csv, mode='r') as file:
        lector_csv=csv.DictReader(file)   #dictreader te permite usar cada fila como un diccionario 
        for fila in lector_csv:
            producto = fila['Producto']
            fecha = fila['Fecha']
            cantidad = int(fila ['Cantidad'])
            precio = fila ['Precio']

            total_venta = cantidad * precio 
            ventas_por_producto[producto] += total_venta
            ingresos_por_dia[fecha] += total_venta
    print("Total de ventas por producto")
    for producto, total in ventas_por_producto.items():
        print(f"{producto}: ${total:.2f}")

    print("\nIngresos totales por dia")
    for fecha, total in ingresos_por_dia.items():
        print(f"{fecha}:${total:.2f}")


archivo_csv = 'ventas.csv'
