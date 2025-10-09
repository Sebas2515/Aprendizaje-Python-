
""" status = input("Ingrese el codigo status:")
if status == "200":
    print("Solicitud exitosa")
elif status == "404":
    print("EL recurso no fue encontrado")
elif status == "500":
    print("Error interno en el servidor")
else: 
    print("El codigo no existe") """


status = int(input("Ingrese el codigo de status: "))
match status: 
    case 200:
        print("Solicitud exitosa")
    case 404 | 403 | 407: 
        print("El Recurso no fue encontrado")
    case 500: 
        print("Error interno en el servidor")
    case _:
        print("Codigo no existe")
