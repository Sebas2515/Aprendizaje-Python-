saldo_cajero = 1000

def consultar_saldo():
    print(f'Tu saldo actual es: {saldo_cajero}')

def retirar_dinero():
    global saldo_cajero
    cantidad = float(input('Ingrese la cantidad a retirar: '))
    if cantidad > saldo_cajero:
        print ('No tienes suficiente saldo para retirar')
    else:
        saldo_cajero -= cantidad
        print(f'Has retirado: {cantidad}\nTu saldo actual es: {saldo_cajero}')

def depositar_dinero():
    global saldo_cajero
    cantidad = float(input('Ingrese la cantidad a depositar: '))
    saldo_cajero += cantidad
    print(f'Has depositado: {cantidad}\nTu saldo actual es: {saldo_cajero}')


def mostrar_menu():
    print("\nMenu de opciones")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

#Con el bucle while, se esta llamando a todas las funciones creadas. Tengas que hacer un programa con varias funciones, hacer un menu y meterlo en un proceso repetitivo y salgas cuando se necesite.

while True : 
    mostrar_menu()
    opcion=int(input("Ingrese una opcion: "))
    if opcion == 1:
        consultar_saldo()
    elif opcion == 2:
        retirar_dinero()
    elif opcion == 3:
        depositar_dinero()
    elif opcion == 4:
        print("Gracias por usar el cajero automatico")
        break
    else: 
        print("Opcion no valida")









