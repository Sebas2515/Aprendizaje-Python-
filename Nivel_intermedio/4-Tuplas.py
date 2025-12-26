"""
mi_tupla=tuple()
mi_tupla=()

mi_tupla = (10,"Hola",3.14, [1,2,3])
print(mi_tupla)
print(type(mi_tupla))
"""

mi_tupla2= (23,15,67,89)

lista_tupla= list(mi_tupla2)
lista_tupla.append(20)
mi_tupla3= tuple(lista_tupla)
print(mi_tupla3)

t=(1,2,3,4,5,)
print(t.count(3))
print(t.index(1))

# tupla[incio:fin:paso]
subtupla= t[1:4]
subtupla1= t[:3]
subtupla2= t[2:]
subtupla3= t[::2]
subtupla4= t[::-1]
print(subtupla4)
