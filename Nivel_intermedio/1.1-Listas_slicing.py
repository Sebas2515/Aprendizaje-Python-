"""
SINTAXIS BASICA 
Lista [inicio:fin:paso]

- Inicio : indica donde empieza el sli  (indice)
- Fin-1: indica donde termina no incluido el sli (indice)
- Paso: los saltos dentro de la lista (opcional)

RESUMEN: 
lista[inicio:fin]
lista[inicio:]
lista[:fin]
lista[:-1]
"""

lista=[0,1,2,3,4,5,6]
sublista= lista[2:5]
sublista2= lista[:4]
sublista3= lista[4:]
sublista4= lista[-4:-1]
copia_completa= lista[:]

sublista_paso= lista[::2]
print(sublista_paso)
