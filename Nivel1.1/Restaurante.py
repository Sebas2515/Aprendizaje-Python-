# todo Calcular el porcentaje de propina en un restaurante 
"""
Descripcion
Dado un total de cuenta y un porcentaje de propina, calcular cuanto se debe 
dar de propina y el total a pagar, autocompletar
"""

def calcular_propina(total_cuenta, porcentaje_propina):
    """
    Calcula la propina y el total a pagar.

    Args:
        total_cuenta (float): El total de la cuenta.
        porcentaje_propina (float): El porcentaje de propina a aplicar.

    Returns:
        tuple: Una tupla que contiene la cantidad de propina y el total a pagar.
    """
    propina = total_cuenta * (porcentaje_propina / 100)
    total_a_pagar = total_cuenta + propina
    return propina, total_a_pagar

# Ejemplo de uso
if __name__ == "__main__":
    total_cuenta = float(input("Ingrese el total de la cuenta: "))
    porcentaje_propina = float(input("Ingrese el porcentaje de propina: "))

    propina, total_a_pagar = calcular_propina(total_cuenta, porcentaje_propina)

    print("Propina: ", propina)
    print("Total a pagar: ", total_a_pagar)
