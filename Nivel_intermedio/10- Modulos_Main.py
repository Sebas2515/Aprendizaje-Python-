"""
Programacion modular 
"""

from Utilidades import mensaje_bienvenida,calcular_edad,contar_vocales


#print(mensaje_bienvenida("Admin","1234","Armando")) 

#print(calcular_edad(2001))

#print(contar_vocales("Hola Mundo"))

import Utilidades as util

#Acceder a la variable del modulo

print(util.mi_variable)
print(util.mensaje_bienvenida("Admin","123","Armando"))
print(util.MiClase("Armando"))

objeto = util.MiClase("Armando")
print(objeto.saludar())

