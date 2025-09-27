
#001.- Calcular el precio total de un producto con IGV 

"""
precio_producto= float(input('Introducir precio del producto:'))
cantidad_producto= float(input('Introducir cantidad comprada:'))
IGV= 0.18
precio_con_IGV= precio_producto*(1+IGV)
precio_total = precio_con_IGV * cantidad_producto

print(f'Total a pagar con IGV es de {precio_total:.2f}')
"""


#002.- Calcular el salario semanal de un trabajador 
"""
nombre_trabajdor= input('Ingrese el nombre del trabajador:')
horas_trab=int(input('Ingrese las horas trabajadas:'))
tarifa_hora=float(input('Ingrese la tarifa por hora:'))
salario_diario= horas_trab*tarifa_hora
print(f'El salario del trabajador {nombre_trabajdor} es {salario_diario:.2f}')
"""

#003.- Calcular el promedio de notas de un alumno 
"""
nombre_alumno= input('Ingrese el nombre del alumno:')
nota_1=float(input('Ingrese la nota 1:'))
nota_2=float(input('Ingrese la nota 2:'))
nota_3=float(input('Ingrese la nota 3:'))
promedio_final= (nota_1+nota_2+nota_3)/3
if promedio_final>10:
    print(f'El alumno {nombre_alumno} obtuvo {promedio_final:.2f} por lo tanto aprobó satisfactoriamente')
else:
    print(f'El alumno {nombre_alumno} obtuvo {promedio_final:.2f} por lo tanto no aprobo')

#print(f'El promedio del alumno {nombre_alumno} es {promedio_final:.2f}')
"""

#004.- Convertir de dolares a euros 
"""
cant_dolares= float(input('Ingrese la cantidad de dolares:'))
tipo_de_cambio= float(input('Ingrese la cantidad de dolares:'))
total_soles= cant_dolares*tipo_de_cambio
print(f'El total en soles es {total_soles:.2f}')
"""

#005.- Convertir Segundos a horas, minutos y segundos 
"""
total_segundos= int(input('Ingresar la cantidad de segundos:'))
total_horas= total_segundos //3600 
minutos=(total_segundos%3600)//60
segundos_restantes= total_segundos % 60
print(f'{total_horas} horas, {minutos} minutos, {segundos_restantes} segundos')
"""


