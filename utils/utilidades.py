def login(usuarios, claves):
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
    print("4. Dar de Alta")
    print("5. Modificar")
    print("6. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion


def obtener_indice_por_codigo(codigos, codigo):
    i = 0
    while i < len(codigos):
        if codigos[i] == codigo:
            return i
        i += 1
    return -1


def ver_clientes(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes):
    print("\n--- CLIENTES ---")
    i = 0
    while i < len(codigos_clientes):
        tipo = "Regular" if tipos_clientes[i] == 1 else "Frecuente"
        print(f"Cod: {codigos_clientes[i]} | {nombres_clientes[i]} | Edad: {edades_clientes[i]} | {tipo}")
        i += 1


def ver_productos(codigos_productos, nombres_productos, precios_productos):
    print("\n--- PRODUCTOS ---")
    i = 0
    while i < len(codigos_productos):
        print(f"Cod: {codigos_productos[i]} | {nombres_productos[i]} | ${precios_productos[i]:.2f}")
        i += 1


def ver_ventas(codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
               ventas_productos, codigos_productos, nombres_productos,
               ventas_cantidades, precios_productos):
    print("\n--- HISTORIAL DE VENTAS ---")
    i = 0
    while i < len(codigos_ventas):
        indice_cliente = obtener_indice_por_codigo(codigos_clientes, ventas_clientes[i])
        if indice_cliente == -1:
            nombre_cliente = "Cliente desconocido"
        else:
            nombre_cliente = nombres_clientes[indice_cliente]

        indice_producto = obtener_indice_por_codigo(codigos_productos, ventas_productos[i])
        if indice_producto == -1:
            nombre_producto = "Producto desconocido"
            total = 0
        else:
            nombre_producto = nombres_productos[indice_producto]
            total = ventas_cantidades[i] * precios_productos[indice_producto]

        print(f"Venta {codigos_ventas[i]} | {nombre_cliente} | {nombre_producto} x{ventas_cantidades[i]} | ${total:.2f}")
        i += 1
