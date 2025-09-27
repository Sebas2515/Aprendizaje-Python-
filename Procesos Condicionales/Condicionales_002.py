"""
Aplicar un descuento a un producto dependiendo de su precio 
- Precio >100 ---> 10%
- Precio <=100 ---> 5%
"""

precio = float(input("Introducir el precio del producto:"))
if precio >100:
    descuento = precio * 0.10
else:
    descuento = precio * 0.05
precio_final = precio - descuento
print(f"El precio final con descuento es $ {precio_final:.2f} ")
