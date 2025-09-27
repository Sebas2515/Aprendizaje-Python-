"""
Sintaxis:
if condition:
  pass
else:
  pass
  
if condition:
  pass
elif condition:
  pass

"""  

""""
x=int(input("Ingrese el valor de x:"))
if x>0:
    print("X es Positivo") #True
elif x==0:
    print("X es Cero")    
else:
    print("X es Negativo")    

"""
"""
x=15
y=-10
if x>0:
    if y>0:
        print("Ambos x e y son positivos")
    else:
        print("x es positivo , pero y no es positivo")  
else:
    print("x no es positivo")        
""" 
"""
x=20
y=30
if x > 10 and y <40:
    print("x es mayor que 10 y es menor que 40")   
"""

"""
x=5
y=15

if x <10 or y>10:
    print("Al Menos una de las condiciones es verdadera")
if not(x>10):
    print("x no es mayor que 10")    
"""

"""""
try:
    punt_obt=int(input("Ingrese el puntaje obtenido:"))
    if punt_obt >150:
        print("Eres un Master en Python")
    elif 100 < punt_obt <=150:
        print("Tienes un Nivel Señior")    
    elif 70 <punt_obt<=100:
        print("Tienes un Nivel Intermedio")    
    else:
        print("Tienes un Nivel Basico")    
except ValueError:
    print("Debes ingresar un valor numerico")        


"""""
"""
nota_uno=float(input("Ingrese la Nota1:"))    
nota_dos=float(input("Ingrese la Nota2:"))    
nota_tres=float(input("Ingrese la Nota3:"))    
prom_notas=(nota_uno+nota_dos+nota_tres)/3
if prom_notas>=10.5:
    print("Felicitaciones APROBO EL CURSO!!!!")
else:
    nota_sus=float(input("Ingrese la Nota Sustitutoria:"))    
    nue_prom=(nota_sus+prom_notas)/2
    if nue_prom>=10.5:
        print(f"El Alumno aprobo el curso usando el sustitutorio {round(nue_prom,2)}")
    else:
        print(f"El Alumno debera lleevar nuevamente el curso {round(nue_prom,2)}")    
"""

#Ejercicios 26/09/25

x=10
if x>10:
    print("x es positivo")
elif x==0
    print ("x es cero")
    