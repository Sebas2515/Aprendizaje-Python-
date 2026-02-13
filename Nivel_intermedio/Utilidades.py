def mensaje_bienvenida(user,passw,nom=None):
    if user == "Admin" and passw=="123":
        return f"Bienvenido {nom} que bueno tenerte por aca"
    else: 
        return f"Usuario {nom} invalido"
    

def calcular_edad(nac):
    actual= int(input("Ingrese el año actual: "))
    edad = actual-nac
    return edad

def contar_vocales(frase):
    frase=frase.lower()
    vocales="aeiou"
    contador=0
    for letra in frase:
        if letra in vocales:
            contador+=1
    return contador

#Variable global 
mi_variable = "Hola desde mi_modulo"

#Clase POO / plantilla que contiene metodos
class MiClase:
    def __init__(self,nombre):
        self.nombre=nombre
    def saludar(self):
        return f"Hola mi nombre es {self.nombre}"
    

persona=MiClase(nombre="Armando")
#print(persona.saludar())
