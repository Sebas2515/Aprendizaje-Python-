
"""
d= {'a':'1','b':'2','c':'3'}
item= d.popitem() #te elimina el ultimo valor insertado
print(item)
print(d)
"""

mi_diccionario= {}
mi_diccionario= dict()

mi_diccionario = {
    "Nombre": "Juan",
    "Apellido": "Perez",
    "Edad": 35,
    "Ciudad": "New York"
}

print(mi_diccionario.get("Nombre")) #entre parantesis se pone la clave y te duelve el valor
print(mi_diccionario.keys()) #te devuelve las clavesdel diccionario 
print(mi_diccionario.values()) #te devuelve los valores del diccionario 
print(mi_diccionario.items()) 

"""
mi_diccionario["Profesion"] = "Develeoper Python Pro"
mi_diccionario["Nombre"] = "Jose Luis"

del mi_diccionario["Profesion"]  #del sirve para eliminar una clave en el diccionario 
print(mi_diccionario)

for k,v in mi_diccionario.items():  #items sirve para gestionarar los valores del diccionario 
    print(f"La clave es {k} y el valor es {v}")
"""