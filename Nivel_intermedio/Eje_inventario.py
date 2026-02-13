#Iniializar el inventario 
"""
inventario = {
    'Manzana':{'Cantidad':100 , 'precio':0.50},
    'Platanos':{'Cantidad':150 , 'precio':0.30},
    'Naranjas':{'Cantidad':80 , 'precio':0.40},
}

def listar_inventario(inventario):
    for nombre,detalles in inventario.items():
        print(f'Producto: {nombre}, Cantidad: {detalles["Cantidad"]}, Precio: {detalles["precio"]}')

def agregar_producto(inventario, nombre, cantidad, precio):
    if nombre in inventario:
        inventario[nombre]['Cantidad'] += cantidad
    else: 
        inventario[nombre] = {'Cantidad': cantidad, 'precio': precio}

def eliminar_producto(inventario, nombre):
    if nombre in inventario:
        del inventario[nombre]
    else: 
        print('El producto no existe en el inventario')


def actualizar_cantidades (inventario, nombre, cantidad):
    if nombre in inventario:
        inventario[nombre]['Cantidad'] += cantidad
    else:
        print("El producto no existe en el inventario")


def consultar_producto (inventario, nombre):
    if nombre in inventario:
        producto = inventario[nombre]
        return producto['Cantidad'], producto['precio']
    else:
        return "El producto no existe en el inventario"
    


agregar_producto(inventario, 'peras', 90, 0.25)
eliminar_producto(inventario, 'Manzana')
actualizar_cantidades(inventario, 'Platanos', 50)


producto = input('Ingrese el nombre del producto: ')
cantidad, precio = consultar_producto(inventario, producto)
print(f'Cantidad: {cantidad}, Precio: {precio}')

"""
#listar_inventario(inventario)

################################################################################################
"""
# 1. Acumulación por clave 

ventas = [
    ('cobre', 5000),
    ('oro', 3000),
    ('cobre', 4500),
    ('pota', 1200),
    ('oro', 2700),
    ('cobre', 2300)    
]

#-- Sol
totales = {}
for producto, valor in ventas:
     if producto in totales: 
          totales[producto] += valor #si la clave ya existe sumale el valor nuevo, “En el diccionario totales, usa producto como clave y guarda valor” 
     else:
          totales[producto] = valor

print(totales)
print(type(totales))

#El for es como una mano que toma un elemento, lo pone en una variable y ejecuta el mismo código una y otra vez.


# 2. Diccionario de ranking /
# sorted(objeto, key=..., reverse=...)
ranking = sorted(totales.items(),key= lambda x: x[1], reverse=True)

for puesto, (producto, valor) in enumerate(ranking, start=1):
     print(puesto, producto, valor)


# 3. Filtrado por condición 
exportaciones = {
    "cobre": 18000,
    "oro": 15700,
    "pota": 1220,
    "hierro": 2800,
    "zinc": 4300
}

# sol 

nuevo_expo = {}
for producto, valor in exportaciones.items():
     if valor > 4000:
          nuevo_expo[producto] = valor
          
print(nuevo_expo)

# 4. Diccionario con datos compuestos 

productos = {
    "cobre": {"volumen": 2500, "valor": 18000},
    "oro": {"volumen": 120, "valor": 15700},
    "pota": {"volumen": 900, "valor": 1220},
    "hierro": {"volumen": 3200, "valor": 2800}
}

# sol 


precios = {}

for prod, datos in productos.items():
     precio = datos["valor"] / datos["volumen"]
     precios[prod] = round(precio, 2)

mayor = max(precios, key=precios.get)


print(precios)
print('Mayor precio:', mayor)
"""
# 5.  Agrupacion avanzada 

registros = [
    ("cobre", "Arequipa", 5000),
    ("oro", "Cajamarca", 3000),
    ("cobre", "Moquegua", 4500),
    ("oro", "Cajamarca", 2700),
    ("pota", "Piura", 1200),
    ("cobre", "Arequipa", 2300)
]

nuevo_dic = {}

for producto, provincia, valor in registros: #Python toma una tupla por vez y la separa en 3 variables.
     if producto in nuevo_dic: #¿Existe "producto" en nuevo_dic?
          if provincia in nuevo_dic[producto]: #¿Existe "la provincia" en nuevo_dic?
               nuevo_dic[producto][provincia] += valor
          else:
               nuevo_dic[producto][provincia] = valor
     else:
          nuevo_dic[producto] = {provincia: valor}


print(nuevo_dic)

# 6. 
# - Un diccionario donde cada producto tenga una lista de sus valores
# - Luego calcula el promedio de exportación por producto

product_valor = {}

for producto, provincia, valores in registros:
     if producto in product_valor:
          product_valor[producto].append(valores)
     else:
          product_valor[producto] =[valor]

print(product_valor)    


promedios = {}
for producto, valores in product_valor.items():
     promedio = sum(valores) / len(valores)
     promedios[producto] = round(promedio,2)

print(promedios)

# 7. Detección de líderes  

# -- Calcula el total por producto
exportaciones = {
    "cobre": [5000, 4500, 2300],
    "oro": [3000, 2700],
    "pota": [1200]
}

total_product = {}

for productos, valores in exportaciones.items():
     total_product[productos] = sum(valores)
     
print(total_product)


# -- Identifica el líder en exportaciones

mayor = max(total_product, key=total_product.get) #“Dame la clave del diccionario cuyo valor es el más grande”
print(mayor, total_product[mayor])
