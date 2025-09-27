"""
Variables y Funciones 

- Estilo : snake_case 

    mi variable= ""
    calcular_suma()

- Nombres Descriptivos:

    contador_item="
    obtener_dato_usuario=""

Constantes

- Estilo : UPPER_SNAKE_CASE

    VALOR_INICIAL = 0 
    TIMEPO_MAXIMO = 20 

"""

nom_per = "Armando"
aper_per = "Ruiz"
edad_per = 48 
sue_per = 1200.9856666 #float
act_per = True
total_prod = "1900"
cantidad_prod = 8 

def calcular_area(radius):
    return 3.14 *radius **2

#Conversion de datos 
total_pagar = float(total_prod) * cantidad_prod #convertir = CAST
cadena_dos = str(sue_per)
tipo_dato = type(cadena_dos)
#print(total_pagar)


#Concatenacion y formateo de datos 
cadena = nom_per + str(edad_per)
#print(nom_per,",",sue_per)  #masomaso
#print(f"El nombre de la persona es {nom_per} y su sueldo es {round(sue_per,3)}") #manera mas correcta, funcion round para los decimales  

nuevo_sueldo= f"{sue_per: .2f}"
print(nuevo_sueldo)
