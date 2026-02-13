"""
Ambito global 
Ambito local

"""

"""
#variable global 

x=10

def mi_funcion ():
    #Variable local
    y=5
    print(f'Dentro de mi funcion x={x}') #Accede a la variable global 
    print(f'Dentro de mi funcion y={y}') #Accede a la variable local 

mi_funcion()

contador = 0 
def incrementar ():
    global contador #que usaremos la variable global 
    contador +=1
    print(f'Dentro de incrementar, contador = {contador}')

incrementar()
"""

#Variable global para llevar el registro de numeros de usuarios activos 

usuarios_activos = 0

def iniciar_sesion(nombre_usuario):
    global usuarios_activos
    usuarios_activos += 1
    print(f'Usuario {nombre_usuario} ha iniciado sesion')
    print(f'Numero de usuarios activos: {usuarios_activos}')

def cerrar_sesion (nombre_usuario):
    global usuarios_activos
    usuarios_activos -= 1
    print(f'Usuario {nombre_usuario} ha cerrado sesion')
    print(f'Numero de usuarios activos: {usuarios_activos}')

#Simulacion de usuarios iniciando y cerrando la sesion 
iniciar_sesion('Juan')
iniciar_sesion('Maria')
iniciar_sesion('Pedro')
cerrar_sesion('Juan')


