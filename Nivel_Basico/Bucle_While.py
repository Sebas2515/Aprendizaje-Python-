"""
Se debe utilizar este bucle si se cumple una condicion logica 
while condicion: 
#Bloque de codigo
"""

""""
contador = 0 
while contador <5:
    print(contador)
    contador +=1
"""

"""
suma = 0 
n=1 

while suma <20:
    suma +=n
    n +=1
print (f"La suma es {suma}")
"""

usuario_valido= "Arruiz"
contrase_valida="123"
intentos=3
persona= "Armando Ruiz"
while intentos >0:
    usuario= input("Ingrese el usuario: ")
    contraseña= input("Ingrese la contraseña: ")
    if usuario==usuario_valido and contraseña==contrase_valida:
        print(f"Inicio de sesion exitoso, bienvenido al sistema {persona} un gusto tenerlo por aca")
        break
    else:
        intentos -=1
        print(f"Usuario o contraseña incorrecta, intentos restantes {intentos}")
if intentos ==0:
    print ("Tu cuenta se bloqueara por 24 horas!!")