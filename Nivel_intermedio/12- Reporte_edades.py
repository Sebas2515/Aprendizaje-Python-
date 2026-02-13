"""
Crear un archivo en formato csv, con datos provenientes de una lista 
Sumar los datos numericos y colocarlos en la ultima fila del csv
"""

import csv
import gc #recoleccion de basura que tiene python / garbage collection, recoleccion de basura limpiar objetos que no sean utilizados

gc.collect() #que se pueda limpiar las variables que no estoy utilizando

#definir el nombre del archivo 
nombre_archivo = "Nivel_intermedio/datos.csv"

#Crear datos de ejemplo 
datos = [
    ['NOMBRE','EDAD'],
    ['Juan',25],
    ['Maria',19],
    ['Pedro',45],
    ['Armando',43]
]

#Sumar la columna edad 
total_edades = sum(row[1] for row in datos[1:])

#especificar la fila en la que se colocara el total 
fila_total= len(datos) -1

#Calcular el promedio de edades 
promedio_edades = total_edades/fila_total

#añadir el total a la ultima fila de datos 
datos.append(['Total',total_edades])
datos.append(['Promedio',promedio_edades])

#Escribir los datos en el archivo
with open(nombre_archivo,'w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(datos) #Aqui le digo que es lo que voy a escribir, la s final en writerows hacen que sean filas en los datos

#Mostrar los datos escritos en el archivo
with open(nombre_archivo,'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#print(datos)



