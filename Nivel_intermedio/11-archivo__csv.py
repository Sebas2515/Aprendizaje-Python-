"""
Leer archivo 
"""
import csv 

def extraer_csv():
    con = 0
    with open("Nivel_intermedio/productos.csv") as asrchivo_csv:
        lector_csv = csv.reader(asrchivo_csv)
        #iterar sobre las filas del archivo
        for fila in lector_csv:
            if con>0:
                print(fila)
            con+=1
        print (con)

def extraer_txt():
    with open("Nivel_intermedio/productos.txt") as file:
        contenido = file.read()
        print(contenido)

def generar_archivo():
    #si hubiera un error que me capture el tema de la seccion
    try:
        data_to_write= [['CODIGO','PRODUCTO','STOCK'],
                        ['A100','XYZ',200],
                        ['A200','MNO',100],
                        ['A300','POR',170]
        ]
        with open ("Nivel_intermedio/NuevosDatos.csv","w",newline='') as file: 
            writer = csv.writer(file)
            writer.writerows(data_to_write)

    
    except Exception as err:
        print(f'El archivo no se genero {err}')
    else: 
        print("Se genero el archivo")
    finally:
        file.close


generar_archivo()


 
 


      