"""
print("hola mundo desde python")
"""

#Tipo de datos primitivos 
"""""
-- Numericos
    -- int (enteros)
    --float(decimales)
-- Cadenas 
    --str (string)
--Booleanos/Logicos  
    --True/False 
--Estructura de datos (LIST, DICC, TUPLAS, SETS) - Almacena varios valores a la vez 
"""
#Variable: es una porcion de memoria que generalmente almecena un valor a la vez
"""""
curso = 'Python Camara de comercio'
edad_persona = 20 #int
nom_prod="Laptop" #str
fab_prod="Lenovo" #Str
Unidad = 1 
Precio_prod = 1200.90 #float
exis_prod=False #bool 
print(type(curso))
"""
""""
print(type(edad_persona))
print(type(nom_prod))
print(type(fab_prod))
print(type(exis_prod))
"""

"""
indentacion, separa los bloques de codigo, no es necesario cerrar el end
"""
"""""
edad_persona= input("Ingrese su edad )
if edad_persona >=18:
    print("Persona mayor de edad")
else: 
    print("Persona menor de edad")
"""

#Ingreso de datos, todo lo ingresado en input es de type string
"""""
nombre= input("Ingrese el nombre del estudiante:") #castear, tomar una variable con un tipo de dato y cambiarla 
califi1= float(input("Ingrese nota 1:"))
califi2= float(input("Ingrese nota 1:"))
promedio= (califi1 + califi2) / 2 
#print("El promedio del Estudiante:" + str(promedio)) #"+" esta concatenando
# print("El promedio del Estudiante:", promedio)
print(f"El promedio del estudiante {nombre} es {promedio}") # es el mas pythonico posible 
#print(type(nombre))
"""
#SE LLAMAN VARIABLES COMPUESTAS 
#Dentro de ellas hay estructuras de datos

#Las lista son mutables (se pueden editar)
"""""
alumnos= list() #inicializando (constructor)
alumnos = ["Juan", "Pedro", "Sebas",200,True,[1,2,3]] #List, puede almacenar n valores a la vez, se destaca de python que puedes combinar los tipos de datos a diferencia de r
alumnos.append("Carlos") #añadiendo 
alumnos.pop(3) #eliminando 
alumnos[2]="Manuela" #modificando
print(alumnos)
print(alumnos[0]) #si le pones valores negativos de izquierda a derecha, positivos de derecha a izquierda  
print(alumnos[1:]) #De la posición 1 hasta N
print(alumnos[-1])
"""
#La tupla son inmutables 
"""""
valores = tuple() #inicializando la tupla 
valores= (200,700, 800)
nueva_lista=list(valores) #cast tuple list
nueva_lista.append(1200) #insete el valor nuevo
valores=tuple(nueva_lista) #cast list a tuple 
valores. append(20) #no se puede agregar
print(valores)
"""""
#Ejercicios de practica 
familia_mendoza= list()
familia_mendoza=["Pamela", "Sebas", "Salvador", "Mayra"]
familia_mendoza.append("Marina")
familia_mendoza.pop(0)
familia_mendoza[1]="Gordito pop"
print(familia_mendoza)

nombre_apellido= input("Ingresar nombre y apellido:")
edad= int(input("Ingresar edad:"))
peso= float(input("Ingresar peso en kg:"))

if edad >=18:
    print(f"{nombre_apellido} tiene {edad} y es mayor de edad, pesa {round(peso,2)} kg") #Funcion round para elegir cuanto decimales deseas visualizar 
else: 
    print(f"{nombre_apellido} tiene {edad} y es menor de edad, pesa {round(peso,2)} kg")


