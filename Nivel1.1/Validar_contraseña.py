#Funcion any() en Python es una función integrada (built-in) que sirve para verificar si 
# al menos uno de los elementos de un iterable (como una lista, tupla, conjunto, etc.) es verdadero.
"""
def ejemplo_any_002():
    valores = [2,0,0]
    resultado = any(valores)
    print(resultado)

ejemplo_any_002()
"""
#me imprime true por que hay almenos un true dentro de la lista

"""
def nombre_funcion(parametros):
    # Bloque de código
    # (lo que hará la función)
    return valor
"""

#funcion len, lo que hace es contar los caracteres la cadena que se ingresa como parametro
#Char, simplemente es un nombre de variable que se usa por convención cuando recorres una cadena de texto carácter por carácter.
#funcion isdigit (), es un método de las cadenas de texto en Python. Sirve para verificar si un carácter o cadena está compuesta únicamente por números (0–9).
"""
def verificar_contrasena (contrasena):
    # verificar longitud minima (8 caracteres)
    if len(contrasena) <8: 
        return False
    # verificar si contiene al menos un numero 
    if not any(char.isdigit() for char in contrasena): #“Si no hay ningún número en la contraseña, entonces ejecuta el bloque de abajo”.
        return False
    # si contiene al menos una letra mayuscula
    if not any(char.isdigit() for char in contrasena):
        return False
    # verificar si tiene al menos un caracter especial (@,#,$,etc)
    especiales = "Q#$%$&*-+_"
    if not any(char in especiales for char in contrasena): # sin el not me va retornar falso siempre y cuando encuentre un caracter especial, si no contiene al menos un caracter especial, el resultado es falso.
        return False
    return True

# Todo ejemplo de uso
contrasena = "Segur@123"

print(verificar_contrasena(contrasena))

"""
def verificar_contrasena(contrasena):
    # Verificar longitud mínima (8 caracteres)
    if len(contrasena) < 8:
        return False

    # Verificar si contiene al menos un número
    if not any(char.isdigit() for char in contrasena):
        return False

    # Verificar si contiene al menos una letra mayúscula
    if not any(char.isupper() for char in contrasena):
        return False

    # Verificar si tiene al menos un caracter especial
    especiales = "@#$%&*-+_"
    if not any(char in especiales for char in contrasena):
        return False

    # Si cumple todas las condiciones
    return True


# Ejemplo de uso
clave = 'Segura@123'
print(verificar_contrasena(clave))

    




