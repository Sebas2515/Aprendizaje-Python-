import random

#lower() en Python es un método de las cadenas (strings) que convierte todo el texto a minúsculas.
#Un método es una función que pertenece a un objeto.
# En Python, cuando algo tiene . (punto) y luego un nombre, es un método del objeto. 
# x in y = x dentro de y  

#Todo funcion para jugar una sola ronda 
def jugar(victorias_jugador, victorias_computadora):
    #Todas opciones disponibles 
    opciones = ["piedra", "papel", "tijera"]

    #Todo el jugador eloga una opcion 
    jugador = input("Elige piedra, papel o tijera: ").lower()

    #Todo asegurarse de que el jugador elija una opcion valida 
    if jugador not in opciones:
        print("Opcion no valida, elija piedra, papel o tijera")
        return victorias_jugador, victorias_computadora

    #la computadora elige aleatoriamente una opcion
    computadora = random.choice(opciones)

    #Mostrar las elecciones 
    print(f"El jugador eligio: {jugador}")
    print(f"La computadora eligio: {computadora}")

    #determinar el resultado del juego
    if jugador == computadora:
        print("Empate")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("Ganaste!")
        victorias_jugador += 1 #incrementar el conteo de victorias del jugador 
    else:
        print("Perdiste")
        victorias_computadora += 1 #incrementar el conteo de victorias de la computadora 
    
    return victorias_jugador, victorias_computadora


#todo bucle principal del juego para seguir jugando

def juego_piedra_papel_tijera():
    print("Bienvenido al juego de Piedra, Papel o Tijera")
    victorias_jugador = 0
    victorias_computadora = 0

    #crear variables para almacenar las victorias 
    while True:
        victorias_jugador, victorias_computadora = jugar(victorias_jugador, victorias_computadora)
        # todo preguntar si el jugador quiere jugar de nuevo
        jugas_otra_vez = input("¿Quieres jugar de nuevo? (si/no): ").lower()
        if jugas_otra_vez != "si":
            #todo mostrar las estadisticas 
            print("\n--Estadisticas finales--")
            print(f"Victorias del jugador: {victorias_jugador}")
            print(f"Victorias de la computadora: {victorias_computadora}")

            #todo compara quien gano mas veces 
            if victorias_jugador > victorias_computadora:
                print("¡Felicidades, ganaste el juego!")
                
            elif victorias_jugador < victorias_computadora:
                print("La computadora gano mas veces. No te rindas es solo un robot :(")
            else:
                print("El juego termino en empate.")
            
            print("Gracias por jugar. ¡Hasta luego!")
            break

# ejecutar el juego 
juego_piedra_papel_tijera()




