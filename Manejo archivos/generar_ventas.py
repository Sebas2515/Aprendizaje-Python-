"""
Sistema de Registro de Ventas 
- Guardar cada venta (con detalles del producto, cantidad y precio)
en un archivo de texto 
-Mostrar en un Reporte 
-Cada vez que se realize una venta registrarlo en el archivo 'Ventas1.txt'
"""

def registrar_venta(producto, cantidad, precio):
    with open('ventas2.txt','a') as archivo: #'a' agregar sin borrar lo anterior 
        total = cantidad*precio
        archivo.write(f'producto: {producto}, cantidad: {cantidad}, precio: {precio},Total:{total}\n') #el \n ayuda para que Cada vez que registres una venta, se va a guardar en una línea distinta dentro del archivo.  
    print(f'Venta registrada:{producto},{cantidad} unidades, ${total:.2f} total')


registrar_venta('lapiz',3,0.5)
registrar_venta('cuaderno',2,01.25)
registrar_venta('lapiz',3,0.5)
registrar_venta('cuaderno',2,01.25)
registrar_venta('lapiz',3,0.5)
registrar_venta('cuaderno',2,01.25)












"""

def registrar_venta(producto,cantidad,precio):
    with open ('ventas.txt','a') as archivo: #se guarda en una variable archivo 'a' agregar sin borrar lo anterior
        total = cantidad*precio 
        archivo.write(f"Producto: {producto}, Cantidad:{cantidad}, Precio:{precio}, total:{total}") #aca escribe en el archivo
    print(f"Venta registrada:{producto}, {cantidad} unidades, ${total:.2f}")

registrar_venta("Lapiz",3,0.50)
registrar_venta("Cuaderno",2,1.75)
registrar_venta("Lapiz",3,0.50)
registrar_venta("Cuaderno",2,1.75)   
registrar_venta("Lapiz",3,0.50)
registrar_venta("Cuaderno",2,1.75)

# def mostrar_mensaje(nombre):
#     return f"Bienvenido al curso de Python {nombre}"
# print(mostrar_mensaje("Armando"))
"""
