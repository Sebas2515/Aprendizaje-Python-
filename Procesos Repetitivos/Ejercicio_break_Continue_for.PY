"""
Buscamos un numero en una lista al encontrarlo usar break 
para salir de bucle 

numeros = [1,3,5,7,9,11,13,15]
objetivo = int(input("Ingrese el Objetivo: "))

for numero in numeros:
    if numero==objetivo:
        print(f"Numero {objetivo} encontrado")
        break 
else:
    print("Numero no encontrado")
"""
"""
Imprime los numeros de una lista, pero salta los números pares
"""

numeros = [1,2,3,4,5,6,7,8,9]
for numero in numeros:
    if numero % 2== 0:
        continue #Saltar los pares (numeros)
    print(numero)

