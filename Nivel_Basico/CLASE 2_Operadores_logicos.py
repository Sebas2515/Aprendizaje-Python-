
#Operadores Relacionales 
"""
Igualda: = 
Desigualdad: != 
Mayor que:>
Menor que:
Mayor o igual que:
Menos o igual que: 
"""
#Operadores Logicos 
"""
and: Devuelve True si ambas expresiones son verdaderas.
or: Devuelve True si al menos una de las expresiones es verdadera. 
not: Niega la expresion booleana: devuelve False si la expresion es verdadera y viceversa. 

"""

nombre_persona= "Juan"
nombre_empleado= "Juan"
esta_logueado= True 

respuesta_2= True != esta_logueado 

respuesta = nombre_persona == nombre_empleado

edad_persona= 16
tiene_licencia= True
puedo_conducir=edad_persona >=18 or tiene_licencia


print(puedo_conducir) #True compara 

a= 10
b= 20
c= 10

""" print(a==b)
print(a !=b)
print(a > b)
print(a < b)
print(a >= c)
print(a <= c) """

if a < b and a==c:
    print("a es menor que b y a es igual a c")
else:
    print("La condicion no se cumple")



