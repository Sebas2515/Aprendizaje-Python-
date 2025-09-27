"""
AMBITO LOCAL; Las variables declaradas dentro de una funcion o bloque tienen un alcance local, es decir 
solo estan disponibles dentro de esa funcion o bloque.

"""
global_var=20 #variable global

def my_funcion():
    local_var=10 #varible local
    print(local_var)

def my_funcion_dos():
    print(global_var)

#my_funcion_dos()

"""
AMBITO GLOBAL; Las variables declaradas fuera de cualquier función o bloque tienen un alcance global y 
estan disponibles en todo el módulo. 
"""

COUNT= 0 

def incremento_valor():
    global COUNT
    COUNT +=1

incremento_valor()
print(COUNT)
