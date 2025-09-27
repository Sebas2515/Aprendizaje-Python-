"""
Hasta que ingrese el numero "0" salir del programa 
"""
"""
while True:
    numero = int(input("Introduce un numero (0 para salir):"))
    if numero ==0:
        print("Saliendo del bucle...")
        break #Falso
    print(f"Ingresaste {numero}")
"""

"""
Solicitar numeros al usuario pero si el numero es negativo lo 
voy a ignorar. Solo imprimir los numeros positivos 
"""

while True:
    numero = int(input("Introduce un número positivo (0 para Salir): "))
    if numero <0:
        print ("Numero Negativo IGNORADO")
        continue #si el numero es menor a 0 generalmente lo ignora 
    if numero ==0:
        print ("Saliendo del bucle...")
        break #termina la interaccion 
