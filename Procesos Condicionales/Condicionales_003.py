"""
Nota >=90 : A 
80 <=NOTA <90: B 
70 <=NOTA <80: C
60 <=NOTA <70: D
NOTA <60: F 
"""

nota = int(input("Introduce la nota del estudiante:"))
if nota >=90:
    print ("Calificación A")
elif nota >=80:
    print ("Calificación B")
elif nota >=70:
    print ("Calificación C")
elif nota >=60:
    print ("Calificación D")
else:
    print ("Calificación F")