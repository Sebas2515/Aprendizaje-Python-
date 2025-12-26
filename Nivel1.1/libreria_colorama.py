"""
Colorama  es una libreria escrita en python que me permite cambiar los colores 
y el formato de fuente en mi programas de consola 
"""
from colorama import init, Fore, Back, Style, init
#todo inicializar colorama para que funcione correctamente en todas las palabras 
init(autoreset=True)
def ejemplo_uso_colorama():
    #todo cambiar el color del texto 
    print(Fore.RED + "Esto es un texto en rojo")
    #todo cambiar el color de fondo 
    print(Back.GREEN + "Esto es un texto en verde")
    #todo cambiar texto y el fondo
    print(Fore.YELLOW + Back.BLUE+ "Texto en amarillo con fondo azul")
    #todo aplicar estilo de negrita (resaltado)
    print(Style.BRIGHT + "Texto en negrita")

    #todo resetear estilos despues de una cadena 
    print(Fore.WHITE + Back.BLACK + 'Texto en blanco en fondo negro'+ Style.RESET_ALL)

def menu_opciones():
    borde_superior = f"{Fore.YELLOW}{Back.BLUE}+" + "-" * 30 + "+"

    opciones = [
        f"{Fore.CYAN}{Back.BLACK}/ 1. Opcion 1                 ",
        f"{Fore.CYAN}{Back.BLACK}/ 2. Opcion 2                 ",
        f"{Fore.CYAN}{Back.BLACK}/ 3. Opcion 3                 "
    ]
    borde_inferior = f"{Fore.YELLOW}{Back.BLUE}+" + "-" * 30 + "+"
    print(borde_superior)
    for opcion in opciones:
        print(opcion)
    print(borde_superior)

menu_opciones()
seleccion = int(input(f'{Fore.GREEN} Seleccione una opcion:'))
if seleccion == 1:
    print("Has seleccionado la opcion 1")
elif seleccion == 2:
    print("Has seleccionado la opcion 2")
elif seleccion == 3:
    print("Has seleccionado la opcion 3")
else:
    print("Opcion no valida")


