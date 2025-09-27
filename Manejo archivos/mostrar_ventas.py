def mostrar_reporte_ventas():
    print("Reporte de ventas del dia:")
    try:
        with open('ventas2.txt','r') as archivo:
            contenido = archivo.readlines() #Lee todas las lineas 
            if contenido:
                for linea in contenido:
                    print(linea.strip()) #strip se usa para eliminar los espacio en blanco 
            else:
                print("No se escontro el archivo de ventas")
    except FileNotFoundError:
         print("No se encontro el archivo asegurese de tenerlo como parte del proyecto")

mostrar_reporte_ventas()
