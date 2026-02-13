"""
Argumentos posicionales: 
se aquellos que se pasan a una funcion con el orden con los que se definen 
deben coincidir con el numero de parametros definidos en una función
"""
#se pasan en la funcion en el orden en que se definen 
def suma_valores(a,b):
    return a+b

resultado = suma_valores(2,3)
#print(f'El resultado de la funcion es {resultado}')

"""
ARGUMENTOS NOMBRADOS (O ARGUMENTOS CON NOMBRE):
"""

def describir_persona (nombre,edad):
    return f'{nombre} tiene {edad} años'

resultado= describir_persona(nombre='Juan',edad=30)
#print(resultado)

"""
Argumento por defecto 
"""
def mensaje_bienvenidda (nombre, saludo='Hola'):
    return f'{saludo} {nombre}'

resultado1= mensaje_bienvenidda('Juan')
resultado2= mensaje_bienvenidda('Juan','Bienvenido')
#print(resultado1)
#print(resultado2)

"""
ARGUMENTOS VARIABLES 
*args = Captura multiples argumentos posicionales en una tupla 
**kwargs = Captura multiples argumentos nombrados en un diccionario 

"""
def sumar_valores_dos(*args):
    return sum(*args)

resultado= sumar_valores_dos([1,2,3,5,6,7])
print(f'el valor es {resultado}')

def mostras_info(**kwargs):
    for clave,valor in kwargs.items():
        print(f'{clave}: {valor}')
    
mostras_info(nombre='Juan',edad=30,ciudad='Lima')

"""
Combinar Argumentos 
1- Argumentos Posicionales
2- Argumentos Por Defecto
3- *args
4- **kwargs
"""
def ejemplo_combinacion(a,b=5, *args, **kwargs):
    print(f'a: {a}, b: {b}')
    print(args)
    print(kwargs)

ejemplo_combinacion (1,2,3,4,x=10, y=10)
