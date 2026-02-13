"""
def funcion_recursiva (parametros):
    #Caso base: condicion de parada
    if condicion_base:
        return resultado_base
    else:
        #Caso recursivo: llamada a la funcion con parametros modificados 
        return funcion_recursiva(parametros_modificados)
"""

#Ejemplos: fibonacci, factorial, etc

#Definicion de recursividad
#Caso Base: El factorial de 0 es 1 
#Caso Recursivos = n!=n*(n-1)!  

def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

resultado = factorial(5)
print(resultado)

