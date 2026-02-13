"""
Nativo significa que ya viene con el paquete o con el programa. 
"""
#Modulo matematico
import math 

#print(math.pi)
#print(math.sqrt(16))

import statistics

datos = [2,90,10,5,14,7,23,7,10,5]
media_arimetica = statistics.mean(datos)
valor_medio = statistics.median(datos)
moda = statistics.mode(datos)

#print(moda)
#print(valor_medio)
#print(media_arimetica)

import random 
numero_azar=random.randint(1,10)
cursos = ["Python","Django","Flask"]
estudiar_mes=random.choice(cursos)

#print(estudiar_mes)
#print(numero_azar)

from datetime import datetime, timedelta #(sirve para operar con fechas)
#obtener la fecha actual 
fecha_actual= datetime.now()
#print(fecha_actual)
# print("Año",fecha_actual.year)
# print("Mes",fecha_actual.month)
# print("Dia",fecha_actual.day)
# print("Hora",fecha_actual.hour)
# print("Minuto",fecha_actual.minute)


nueva_fecha = fecha_actual + timedelta(days=30)
#print(nueva_fecha)

cadena_fecha = "2023-08-25"
fecha_desde_cadena=datetime.strptime(cadena_fecha, "%Y-%m-%d")
print(fecha_desde_cadena)
print(type(fecha_desde_cadena))

#castear la fecha de str a datatime
fecha1=datetime(2022,5,10)
fecha2=datetime(2022,3,15)

#Calcular la diferencia de fechas
diferencia=fecha1-fecha2
print(f"Diferencia entre dias {diferencia.days}")

