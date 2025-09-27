"""
FUNCION PRINT
"""
nombre_curso = "Python"
precio_curso= 200.20
horas_curso= 56
estado_curso= True
#print("Hola mundo desde Python")
#print('Mi Nombre es Armando Ruiz')

#f-string sirve para incluir expresiones, dentro de una cadena de texto de forma directa y legible.
cadena= f"El Curso es {nombre_curso} el precio es {precio_curso} y las horas es {horas_curso}"

#print(cadena)
#print (f"EL Nombre del producto ingresado es {nombre_producto}")
#print(f"El tipo de datos es {type(nombre_producto)}")

"""
FUNCION INPUT
""" 
# nombre_producto = input("Ingrese el nombre del producto:")
# precio_producto = float(input("Ingrese el precio del producto:"))
# cant_prod= int(input("Ingrese la cantidad del producto:"))
# total=precio_producto*cant_prod
#print(f"El Total a pagar es {total}")

"""
FUNCION FORMAT
SINTAXI:
"cadena de texto {}".format(valor)
"""

nombre_usuario = "Armando"
saludo= "Hola, {}".format(nombre_usuario)
print(saludo)

pi=3.14159
formated_pi = "El valor de pi es {:.2f}".format(pi)
print(formated_pi)

nombre_persona="Alice"
saludo= f"Hola, {nombre_persona}"
print(saludo)


