"""
'r' : Modo de lectura (por defecto). El archivo debe existir.
'w' : Modo de escritura. Crea un archivo nuevo o trunca el archivo existente.
'a' : Modo de anexado. Crea un archivo nuevo o agrega datos al final del archivo existente.
'b' : Modo binario. Se puede combinar con los otros modos (por ejemplo, 'rb' para leer en 
'x' : Modo exclusivo. Crea un nuevo archivo, pero fallará si el archivo ya existe.
"""

#enconding='utf 8', le dice a Python cómo debe interpretar los bytes del archivo como texto.
"""
with open('Nivel_Basico/informacion.txt','r',encoding='utf-8') as file:  
      contenido=file.read()
      print(contenido)
"""

   
with open('Nivel_Basico/informacion.txt','w',encoding='utf-8') as file: #caperta absoluta 
    file.write("Primera Linea de Texto.\n")
    file.write("Segunda Linea de Texto.\n")


