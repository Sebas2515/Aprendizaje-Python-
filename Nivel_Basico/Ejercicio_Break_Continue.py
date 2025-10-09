
## FOR ##
"""
Buscamos un numero en una lista al encontrarlo usar break para salir del bucle 
"""
"""
numeros = [1,3,5,7,9,11,13,15]
objetivo = 10

for numero in numeros:
    if numero==objetivo:
        print(f"Numero {objetivo} encontrardo")
        break
else:
    print("Número no encontrado")
"""
"""
Imprime los numeros de una lista, pero salta los numeros pares 
"""
"""
numeros = [1,2,3,4,5,6,7,8]
for numero in numeros: 
    if numero % 2 ==0:
        continue  #Saltar los pares 
    print(numero)
"""

#### WHILE ####
"""
while True:
    numero= int(input("Introduce un numero (0 para salir)"))
    if numero ==0:
        print("Saliendo del bucle...")
        break #False 
    print(f"Ingresaste {numero}")
"""
"""
Solicitar numeros al usuario pero si el numero es negativo lo voy a
ignorar. Solo imprimir los numeros positivos
"""

while True:
    numero = int(input("Introduce un numero positivo (0 para salir):"))
    if numero <0:
        print("Numero negativo IGNORADO")
        continue
    elif numero == 0:
        print("Saliendo del bucle...")
        break

