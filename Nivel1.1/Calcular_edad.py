"""
Descripcion: 
Dado una fecha de nacimiento, calcular la edad actual 
"""
import datetime

def calcular_edad(fecha_nacimiento):
    """
    Calcula la edad actual a partir de una fecha de nacimiento.

    Args:
        fecha_nacimiento (datetime.date): La fecha de nacimiento.

    Returns:
        int: La edad actual.
    """
    hoy = datetime.date.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

if __name__ == "__main__":
    fecha_nacimiento_str = input("Ingrese su fecha de nacimiento en formato YYYY-MM-DD: ")
    try:
        fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
        edad = calcular_edad(fecha_nacimiento)
        print("Su edad actual es:", edad, "años")
    except ValueError:
        print("Formato de fecha incorrecto. Use YYYY-MM-DD.")
