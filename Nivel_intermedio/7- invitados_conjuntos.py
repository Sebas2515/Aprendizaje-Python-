#Conjunto de todos los invitados 
"""
invitados = {'Ana','Luis','Marta','Pedro','Sofia','Jorge'}

#Conjuntos de invitados que han confirmado su asistencia
confirmaciones = {'Ana','Luis','Pedro'}

#Invitados que han confirmado 
#for invitado in confirmaciones: 
# print(invitado)

#Invitados que no han confirmado 
no_confirmados= invitados - confirmaciones
print('Invitados que no han confirmado su asistencia',no_confirmados)

#Todos los invitados (confirmaciones y no confirmaciones)
todos_invitados= invitados | confirmaciones
print(f'Todos los invitados (confirmaciones y no confirmaciones){todos_invitados}')


#para no manipular el conjunto original se crea una copia
conjunto = {1,2,3}
copia= conjunto.copy()

print(copia)
"""

conjunto1= {1,2}
conjunto2= {1,2,3}
print(conjunto1.issubset(conjunto2)) #si todos los elementos del conjunto estan basado en el conjunto del parametro, entonces asi devuelve true
print(conjunto2.issuperset(conjunto1))


"""
invitado = input('Ingrese el nombre del invitado: ')
if invitado in confirmaciones:
    print(f'{invitado} confirmo su asistencia')
else:
    print(f'{invitado} no confirmo su asistencia')
"""