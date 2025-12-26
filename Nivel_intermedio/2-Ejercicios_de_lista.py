"""
frutas= list()

#.index() en Python sirve para encontrar la posición (índice) de un elemento dentro de una lista, cadena (string) o tupla.

while True: 
    nueva_fruta=input("Ingrese la fruta:")
    if nueva_fruta in frutas:
        posicion= frutas.index(nueva_fruta)
        print(f'La fruta ya existe y se encuentra en la posición {posicion}')
        rpta=input("Desea continuar:")
        if rpta=="no":
            print("Gracias por tu participacion")
            break
    else:
        frutas.append(nueva_fruta)
        print(frutas)
"""

"""
frutas = ["manzana", "banana", "cereza", "durazno"]
for index,nombre in enumerate(frutas, start=1):
    print(f"{index}. {nombre}")
"""            
"""
fechas= list()

while True:
    nueva_fecha=input("Ingrese la fecha:")
    if nueva_fecha in fechas:
        posicion = fechas.index(nueva_fecha)
        print(f'La fecha ya existe y se encuentra en la posición {posicion}')
        rpta= input("Deseas continuar:")
        if rpta=="no":
            print("Gracias por tu participacion")
            break
    else:
        fechas.append(nueva_fecha)
        print(fechas)

list_guardada= fechas
for index, fechas in enumerate(list_guardada, start=1):
    print(f"{index}. {fechas}")
"""

####################################################################################################
## EJERCICIOS 
####################################################################################################
import statistics

#1 Crea una lista con los valores de exportaciones mensuales (en millones de USD) de un producto:

"""
expo_naranjas = list()
expo_naranjas = [120,135,110,150,160,145]

total = sum(expo_naranjas)
print(total)
      
promedio = sum(expo_naranjas) / len(expo_naranjas)
print(promedio)
print(statistics.mean(expo_naranjas))

valor_maximo = max(expo_naranjas)
print(valor_maximo)

valor_minimo = min(expo_naranjas)
print(valor_minimo)
"""

#2 Crea una nueva lista solo con los precios mayores a 900, Cuenta cuántos precios cumplen esa condición
"""
precio_prom_tm = [850,920,780,1100,995,870]

def precio_mayor_900(lista):
    lista_nueva = []
    for precio in lista:
        if precio > 900:
            lista_nueva.append(precio)        
    return lista_nueva

lista_nueva = precio_mayor_900(precio_prom_tm)
print(lista_nueva)
print(f'En total son {len(lista_nueva)} los elementos mayor a 900')
"""

##### Nivel avanzado ####
# Analisis temporal 

#Tienes una lista con el valor exportado mensual (en millones USD) de un producto:
"""
Valor_exp_mensual = [120, 135, 110, 150, 160, 145, 155, 170, 165, 180, 175, 190]

def tasa_crec_mensual(lista):
    tasa_crecimiento = []
    for i in range(1, len(lista)):
        tasa = (lista[i] - lista[i-1]) / lista[i-1] * 100
        tasa_crecimiento.append(round(tasa,2))
    return tasa_crecimiento

tasa_crecimiento = tasa_crec_mensual(Valor_exp_mensual)

print("\n---Valor expo mensual ---")
print(Valor_exp_mensual)

print("\n---tasas de crecimiento (var%) ---")
print(tasa_crecimiento)


for index, tasa in enumerate(tasa_crecimiento, start=1):
    if tasa == max(tasa_crecimiento):
        print("\n---mes de tasa de crec max ---")
        print(f"{index}er mes; {max(tasa_crecimiento)}%")
 


for index, tasa in enumerate(tasa_crecimiento, start=1):
    if tasa == min(tasa_crecimiento):
        print("\n---mes de tasa de crec min ---")
        print(f"{index}er mes; {min(tasa_crecimiento)}%")
"""
#Lista de precios promedio por tonelada: 

precios = [820, 850, 870, 860, 2400, 890, 910, 880]

def calc_precio_prom (lista):
    prom = round(sum(lista) / len(lista),2)
    return prom

precio_prom = calc_precio_prom(precios)
print(precio_prom)

def mayo_doblprom (lista): 
    prom2 = []
    for precio in lista:
        if precio > precio_prom * 2:
            prom2.append(precio)
    return prom2

prom2 = mayo_doblprom(precios)
print(prom2)

precios.pop(4)
print(precios)




#Modificación de las listas:
"""
minerales = ['oro','cobre','plata','hierro','zinc']

minerales.append('litio')
minerales.pop(4)
minerales.sort()


print(minerales)
"""



#### NOTAS #####
#Si el resultado es un solo número, probablemente no iteres. 
#Si el resultado es otra lista, sí iteras.