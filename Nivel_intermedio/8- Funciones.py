"""
def nombre_de_la_funcion(parametros):
    #cuerpo de la funcion 
    pass
    
"""

def mi_primer_funcion():
    pass

def sumar(a,b):
    return a+b

print(sumar(12,6))

#Opcion 1 
def msj_bienvenida(nombre):
    print(f'Hola {nombre} que te parece el curso de python')

msj_bienvenida('Armando')

#Opcion 2 / acostumbrase a esta forma 
def msj1_bienvenida(nombre):
    salida = f'Hola {nombre} que te parece el curso de python'
    return salida

print(msj1_bienvenida('Armando'))

def saludar_invitado (nombre = "Invitado"):
    salida = f'Hola {nombre} '
    return salida 

print(saludar_invitado())
print(saludar_invitado('Armando'))

#Funciones anidadas 
def externa ():
    def interna():
        return 'Soy la funcion interna'
    return interna()

print(externa())

#Funciones cortas:
suma = lambda x,y:x+y
print(suma(2,3))

def multiplicar_ahora(x,y): #docstrings
    #Multiplica dos numeros y devuelve el resultado
    return x*y

print(multiplicar_ahora(2,3))

def calculadora_minima(x,y):
    def suma(x,y):
        return x+y
    def resta(x,y):
        return x-y
    return suma(x,y), resta(x,y)

resultado = calculadora_minima(10,5)
print(resultado)
