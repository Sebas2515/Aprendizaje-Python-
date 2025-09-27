"""
Utilice el bucle FOR  cuando conozca las veces que se repetira el proceso. 
parametro, la cantidad, y el salto
"""

""" for num in range(1,10,2):
    print(f"{num} - Bienvenido al curso de Python")
print("Fin del bucle")
 """
# frutas = ["manzana","banana","cereza"]
# for fruta in frutas:
#     print(fruta)

# mensaje= "Bienvenido al curso de Python"
# for letra in mensaje:
#     print(letra)

suma_numeros= 0 
cont_num = 0
for x in range(1,7):
    numeros_ing=int(input("Inrgese un numero: "))
    suma_numeros= suma_numeros + numeros_ing
    cont_num = cont_num+1
print(f"La suma total es {suma_numeros} y el numero de vueltas {cont_num}")
