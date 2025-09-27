"""
str.lower()
# Convierte todos los caracterres en minusculas.
str.upper()
# Convierte todos los caracteres en mayusculas.
str.title()
# Convierte el primer caracteres de cada palabra a mayuscula. 
str.strip()
#Elimina los espacios en blanco al principio y al final de la cadena. 
str.join(iterable)
#Une una lista de cadenas en una sola cadena usando el delimitador. 

"""

nombre_curso="python"


nueva_cadena=nombre_curso.upper() #Convertir a mayusculas
nueva_cadena_min=nueva_cadena.lower() #Convertit a minusculas

print(nueva_cadena)
# print(nueva_cadena_min)

# mensaje=" hola mundo "
# nuevo_cadena_sin=mensaje.strip()
#print(nuevo_cadena_sin)

#mensaje_bien="hola mundo desde Python"
#cadena_buscar=mensaje_bien.find("Python") # -1
# cadena_buscar=mensaje_bien.index("Python") # Valueerror
#print(cadena_buscar)


# mensaje_bien="hola mundo desde Python"
# cadena_reemplazar=mensaje_bien.replace("Python", "Django") #reemplaza cadena a una cadena principal
# print(cadena_reemplazar)

palabras=["manzana","banana","cereza"]

resultado=', '.join(palabras)
print(resultado)

#El manejo de  archivos se realiza principalmente a traves del módulo y la funcionalidad, incorporada en el propia lenguaje