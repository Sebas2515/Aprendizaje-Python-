"""
Ejemplos Varios de Declaracion de Variables 
"""

#Asignacion simple 

nom_per= "Armando"
ape_per='Ruiz'
edad_per=49
sue_per=49
act_per=True

#Asignaciones multiples 

cant_prod,msj_bien, estado = 5,"Hola",True
#print(msj_bien)

#Asignar el mismo valor a varias variables 

nom_per = 200

x = y = z = 10 
#print(x)
#print(y)
#print(z)

#Tipos de datos especiales (Estructura de datos)
"""
LIST
DICCIONARIOS 
TUPLAS 
CONJUNTOS 
"""

cursos =["PYTHON","DJANGO","FLASK",20,130.70,True,["FASTAPI","PANDAS"]] #list 
#cursos.append()

empleados = {
    "CODIGO":"200","NOMBRE":"ARMANDO","APELLIDO":"RUIZ"
}#dict
#print(empleados["NOMBRE"])

valores = (100,200,300) #tuple

datos = {12,45,67,89,45} #set
print(datos)

#print(empleados["NOMBRE"])

import keyword
#print(keyword.kwlist)

empleado_nom= "Armando"
print(keyword.iskeyword(empleado_nom))

#Constante se recomiendan en MAYUSCULAS
cant = 0 
PI= 3.14

