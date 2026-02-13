#desde el paquete calculadora llamame al modulo .... e importame la funcion .... 

from calculadora.suma import sumar
from calculadora.resta import resta
from calculadora.multiplicacion import multiplicar
from calculadora.division import dividir    

def main():
    a=10
    b=5
    print(f"La suma de {a} y {b} es {sumar(a,b)}")
    print(f"La resta de {a} y {b} es {resta(a,b)}")
    print(f"La multiplicacion de {a} * {b} = {multiplicar(a,b)}")
    print(f"La division de {a} y {b} es {dividir(a,b)}")

if __name__=="__main__": #es una convencion 
    main()

#cuando se ejecuta el script directamente 
#main cuando se ejecuta el scripit directamente, si el modulo 
