# Sistema de Gestión de ventas

usuarios = ["admin"]
claves = ["1234"]

# Clientes
codigos_clientes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nombres_clientes = ["Juan", "María", "Carlos", "Ana", "Luis", "Pedro", "Sofia", "Marco", "Laura", "Diego"]
edades_clientes = [25, 32, 45, 28, 35, 50, 29, 38, 41, 26]
tipos_clientes = [1, 2, 1, 2, 1, 2, 1, 1, 2, 1]

# Productos
codigos_productos = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
nombres_productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Cable USB", "Auriculares", "Webcam", "Hub USB",
                     "Mousepad", "Adaptador HDMI"]
precios_productos = [500, 25, 80, 200, 10, 60, 75, 35, 15, 20]

# Ventas
codigos_ventas = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
ventas_clientes = [1, 3, 2, 5, 4, 1, 6, 2, 7, 3]
ventas_productos = [101, 103, 102, 104, 105, 106, 107, 108, 109, 110]
ventas_cantidades = [1, 2, 3, 1, 5, 2, 1, 4, 2, 1]
medios_pago = [1, 2, 1, 3, 2, 1, 2, 3, 1, 2]


def login():
    acceso = False
    i = 0

    while acceso == False and i < len(usuarios):
        usuario_actual = input("Usuario: ")
        clave_actual = input("Clave: ")

        if usuario_actual == usuarios[i] and clave_actual == claves[i]:
            return True
        i += 1

    return False


def mostrar_menu():
    print("\n--- MENU ---")
    print("1. Ver clientes")
    print("2. Ver productos")
    print("3. Ver ventas")
    print("4. Nueva venta")
    print("5. Modificar")
    print("6. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion


def ver_clientes():
    print("\n--- CLIENTES ---")
    i = 0
    while i < len(codigos_clientes):
        tipo = "Regular" if tipos_clientes[i] == 1 else "Frecuente"
        print(f"Cod: {codigos_clientes[i]} | {nombres_clientes[i]} | Edad: {edades_clientes[i]} | {tipo}")
        i += 1


def ver_productos():
    print("\n--- PRODUCTOS ---")
    i = 0
    while i < len(codigos_productos):
        print(f"Cod: {codigos_productos[i]} | {nombres_productos[i]} | ${precios_productos[i]}")
        i += 1


def ver_ventas():
    print("\n--- HISTORIAL DE VENTAS ---")
    i = 0
    while i < len(codigos_ventas):
        nombre_cliente = nombres_clientes[ventas_clientes[i] - 1]
        nombre_producto = nombres_productos[ventas_productos[i] - 101]
        total = ventas_cantidades[i] * precios_productos[ventas_productos[i] - 101]
        print(f"Venta {codigos_ventas[i]} | {nombre_cliente} | {nombre_producto} x{ventas_cantidades[i]} | ${total}")
        i += 1


def modificar():
    print("\n--- MODIFICAR ---")
    conjunto = int(input("1. Cliente 2. Producto 3. Venta: "))

    while conjunto < 1 or conjunto > 3:
        conjunto = int(input("1. Cliente 2. Producto 3. Venta: "))

    if conjunto == 1:
        ver_clientes()
        cod_cliente = int(input("Código de cliente: "))

        if cod_cliente < 1 or cod_cliente > len(codigos_clientes):
            print("Código inválido")
            return

        indice = cod_cliente - 1
        mod = int(input("Modificar: 1. Nombre 2. Edad 3. Tipo: "))

        while mod < 1 or mod > 3:
            mod = int(input("Modificar: 1. Nombre 2. Edad 3. Tipo: "))

        if mod == 1:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nombre_viejo = nombres_clientes[indice]
            nombres_clientes[indice] = nuevo_nombre
            print(f"Se cambió {nombre_viejo} a {nuevo_nombre}.")

        elif mod == 2:
            nueva_edad = int(input("Ingrese la nueva edad: "))
            edad_vieja = edades_clientes[indice]
            edades_clientes[indice] = nueva_edad
            print(f"Se cambió la edad de {nombres_clientes[indice]} de {edad_vieja} a {nueva_edad} años.")

        else:
            tipo_viejo = tipos_clientes[indice]
            tipos_clientes[indice] = 2 if tipo_viejo == 1 else 1
            tipo_nuevo = "Frecuente" if tipos_clientes[indice] == 2 else "Regular"
            print(f"Se cambió el tipo de {nombres_clientes[indice]} a {tipo_nuevo}.")

    elif conjunto == 2:
        ver_productos()
        cod_producto = int(input("Código de producto: "))

        if cod_producto < 101 or cod_producto > 110:
            print("Código inválido")
            return

        indice = cod_producto - 101
        mod = int(input("Modificar: 1. Nombre 2. Precio: "))

        while mod < 1 or mod > 2:
            mod = int(input("Modificar: 1. Nombre 2. Precio: "))

        if mod == 1:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nombre_viejo = nombres_productos[indice]
            nombres_productos[indice] = nuevo_nombre
            print(f"Se cambió {nombre_viejo} a {nuevo_nombre}.")

        else:
            nuevo_precio = int(input("Ingrese el nuevo precio: "))
            precio_viejo = precios_productos[indice]
            precios_productos[indice] = nuevo_precio
            print(f"Se cambió el precio de {nombres_productos[indice]} de ${precio_viejo} a ${nuevo_precio}.")

    else:
        ver_ventas()
        cod_venta = int(input("Código de venta: "))

        indice_venta = -1
        i = 0
        while i < len(codigos_ventas):
            if codigos_ventas[i] == cod_venta:
                indice_venta = i
            i += 1

        if indice_venta == -1:
            print("Código de venta inválido")
            return

        mod = int(input("Modificar: 1. Cliente 2. Producto 3. Cantidad 4. Medio de pago: "))

        while mod < 1 or mod > 4:
            mod = int(input("Modificar: 1. Cliente 2. Producto 3. Cantidad 4. Medio de pago: "))

        if mod == 1:
            ver_clientes()
            nuevo_cliente = int(input("Nuevo código de cliente: "))
            cliente_viejo = ventas_clientes[indice_venta]
            ventas_clientes[indice_venta] = nuevo_cliente
            print(f"Se cambió el cliente de {cliente_viejo} a {nuevo_cliente}.")

        elif mod == 2:
            ver_productos()
            nuevo_producto = int(input("Nuevo código de producto: "))
            producto_viejo = ventas_productos[indice_venta]
            ventas_productos[indice_venta] = nuevo_producto
            print(f"Se cambió el producto de {producto_viejo} a {nuevo_producto}.")

        elif mod == 3:
            nueva_cantidad = int(input("Nueva cantidad: "))
            cantidad_vieja = ventas_cantidades[indice_venta]
            ventas_cantidades[indice_venta] = nueva_cantidad
            print(f"Se cambió la cantidad de {cantidad_vieja} a {nueva_cantidad}.")

        else:
            print("1. Efectivo  2. Tarjeta  3. Transferencia")
            nuevo_medio = int(input("Nuevo medio de pago: "))
            medio_viejo = medios_pago[indice_venta]
            medios_pago[indice_venta] = nuevo_medio
            print(f"Se cambió el medio de pago de {medio_viejo} a {nuevo_medio}.")

def nueva_venta():
    print("\n--- NUEVA VENTA ---")
    ver_clientes()
    cod_cliente = int(input("Código de cliente: "))
    ver_productos()
    cod_producto = int(input("Código de producto: "))
    cantidad = int(input("Cantidad: "))
    print("1. Efectivo  2. Tarjeta  3. Transferencia")
    medio = int(input("Medio de pago: "))

    codigos_ventas.append(max(codigos_ventas) + 1)
    ventas_clientes.append(cod_cliente)
    ventas_productos.append(cod_producto)
    ventas_cantidades.append(cantidad)
    medios_pago.append(medio)
    print("Venta registrada")


# Programa principal
login_usuario = login()

if login_usuario:
    print("Usuario correcto\n")

    salir = False
    while salir == False:
        opcion = mostrar_menu()

        if opcion == "1":
            ver_clientes()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            ver_ventas()
        elif opcion == "4":
            nueva_venta()
        elif opcion == "5":
            modificar()
        elif opcion == "6":
            print("Hasta luego")
            salir = True
        else:
            print("Opción inválida")
else:
    print("Usuario incorrecto")