#caracteristica importante de una lista son mutables
#
valores = []
valores = list()

valores = [1200,1900,1700,"Juan", True, [1200,90]]

print(valores[0]) #El valor extrae los valores de izquierda a derecha 
print(valores[-1]) #Los valores negativos extrae los valores de derecha a izquierda

valores.append("Armando") #agrega 
valores.insert(2,"Maria") #agrega en una posicion especifica 
valores.pop(2) 
valores.remove("Armando")
valores [2]=2900

cant_ele=len(valores)
cant_1900= valores.count(1900)
print(f"La cantidad de elementos de la lista es {cant_ele}")
print(f"El valor de 1900 se repite {cant_1900} veces")

frutas = ["manzana","banana","cereza"]

frutas.sort() #te permite ordenar en orden alfabetico a-z
frutas.reverse() # ""      ""    "" z-a

print(frutas)
for fruta in frutas:
    print(fruta)


alumnos = ["Juan", "Maria", "Pedro"]
"""
for alumno in alumnos:
    print(alumno)
"""
alumnos.append("Ana")
alumnos.insert(2,"Miguel")
alumnos.pop(3)
print(alumnos)
