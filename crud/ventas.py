from validaciones.validadores import es_numero, validar_codigo_existente, validar_entero_positivo, validar_opcion_entre
from crud.clientes import modificar_cliente
from crud.productos import modificar_producto
from utils.utilidades import ordenar_insercion, preguntar_orden, obtener_indice_por_codigo
from constantes.constantes import medios_pago


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


def listar_ventas(codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
                  ventas_productos, codigos_productos, nombres_productos, ventas_cantidades, precios_productos):
    entrada = preguntar_orden()
    while not es_numero(entrada, "int") or int(entrada) < 1 or int(entrada) > 3:
        print("Opción inválida.")
        entrada = preguntar_orden()
    orden = int(entrada)

    if orden == 1:
        ver_ventas(codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
                   ventas_productos, codigos_productos, nombres_productos,
                   ventas_cantidades, precios_productos)
        return

    es_descendente = orden == 3
    print("Ordenar por: 1. Código 2. Cantidad 3. Medio de pago")
    entrada = input("Seleccione una opción: ")
    while not es_numero(entrada, "int") or int(entrada) < 1 or int(entrada) > 3:
        print("Opción inválida.")
        entrada = input("Seleccione una opción: ")
    campo = int(entrada)

    if campo == 1:
        indice_clave = 0
    elif campo == 2:
        indice_clave = 3
    else:
        indice_clave = 4

    listas = [codigos_ventas, ventas_clientes, ventas_productos, ventas_cantidades, medios_pago]
    listas_ordenadas = ordenar_insercion(listas, indice_clave, es_descendente)
    ver_ventas(listas_ordenadas[0], listas_ordenadas[1], codigos_clientes, nombres_clientes,
               listas_ordenadas[2], codigos_productos, nombres_productos,
               listas_ordenadas[3], precios_productos)


def crear_venta(codigos_ventas, ventas_clientes, ventas_productos, ventas_cantidades, medios_pago,
                 codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes,
                 codigos_productos, nombres_productos, precios_productos):
    print("\n--- NUEVA VENTA ---")
    ver_clientes(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes)
    entrada = input("Código de cliente: ")
    cod_cliente = validar_codigo_existente(entrada, codigos_clientes)

    ver_productos(codigos_productos, nombres_productos, precios_productos)
    entrada = input("Código de producto: ")
    cod_producto = validar_codigo_existente(entrada, codigos_productos)

    entrada = input("Cantidad: ")
    cantidad = validar_entero_positivo(entrada)

    print("1. Efectivo  2. Tarjeta  3. Transferencia")
    entrada = input("Medio de pago: ")
    medio = validar_opcion_entre(entrada, 1, 3)

    siguiente_codigo = max(codigos_ventas) + 1 if codigos_ventas else 1001
    codigos_ventas.append(siguiente_codigo)
    ventas_clientes.append(cod_cliente)
    ventas_productos.append(cod_producto)
    ventas_cantidades.append(cantidad)
    medios_pago.append(medio)
    print("Venta registrada")


def modificar_venta(codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
                    edades_clientes, tipos_clientes,
                    ventas_productos, codigos_productos, nombres_productos, precios_productos,
                    ventas_cantidades, medios_pago):
    ver_ventas(codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
               ventas_productos, codigos_productos, nombres_productos,
               ventas_cantidades, precios_productos)
    entrada = input("Código de venta: ")
    while not es_numero(entrada, "int"):
        print("Ingrese un número válido.")
        entrada = input("Código de venta: ")
    cod_venta = int(entrada)

    indice_venta = _buscar_indice_venta(codigos_ventas, cod_venta)
    if indice_venta == -1:
        print("Código de venta inválido")
        return

    entrada = input("Modificar: 1. Cliente 2. Producto 3. Cantidad 4. Medio de pago: ")
    while not es_numero(entrada, "int") or int(entrada) < 1 or int(entrada) > 4:
        print("Opción inválida.")
        entrada = input("Modificar: 1. Cliente 2. Producto 3. Cantidad 4. Medio de pago: ")
    mod = int(entrada)

    if mod == 1:
        modificar_cliente(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes)
    elif mod == 2:
        modificar_producto(codigos_productos, nombres_productos, precios_productos)
    elif mod == 3:
        entrada = input("Nueva cantidad: ")
        while not es_numero(entrada, "int"):
            print("Ingrese un número válido.")
            entrada = input("Nueva cantidad: ")
        nueva_cantidad = int(entrada)
        cantidad_vieja = ventas_cantidades[indice_venta]
        ventas_cantidades[indice_venta] = nueva_cantidad
        print(f"Se cambió la cantidad de {cantidad_vieja} a {nueva_cantidad}.")
    else:
        print("1. Efectivo  2. Tarjeta  3. Transferencia")
        entrada = input("Nuevo medio de pago: ")
        while not es_numero(entrada, "int"):
            print("Ingrese un número válido.")
            entrada = input("Nuevo medio de pago: ")
        nuevo_medio = int(entrada)
        medio_viejo = medios_pago[indice_venta]
        medios_pago[indice_venta] = nuevo_medio
        print(f"Se cambió el medio de pago de {medio_viejo} a {nuevo_medio}.")


def buscar_venta(codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
                 ventas_productos, codigos_productos, nombres_productos, ventas_cantidades, precios_productos, medios_pago):
    entrada = input("Ingrese el código que desea buscar: ")
    while not es_numero(entrada, "int"):
        entrada = input("Ingrese un código numérico: ")
    codigo = int(entrada)
    indice = _buscar_indice_venta(codigos_ventas, codigo)
    mostrar_venta(indice, codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
                 ventas_productos, codigos_productos, nombres_productos, ventas_cantidades, precios_productos, medios_pago)


def mostrar_venta(indice, codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
                  ventas_productos, codigos_productos, nombres_productos, ventas_cantidades, precios_productos, medios_pago):
    if indice == -1:
        print("No se encontró el valor en la lista.")
        return

    indice_cliente = obtener_indice_por_codigo(codigos_clientes, ventas_clientes[indice])
    if indice_cliente == -1:
        nombre_cliente = "Cliente desconocido"
    else:
        nombre_cliente = nombres_clientes[indice_cliente]

    indice_producto = obtener_indice_por_codigo(codigos_productos, ventas_productos[indice])
    if indice_producto == -1:
        nombre_producto = "Producto desconocido"
    else:
        nombre_producto = nombres_productos[indice_producto]

    print(f"Cod: {codigos_ventas[indice]} | {nombre_cliente} | {nombre_producto} x{ventas_cantidades[indice]} | Medio: {medios_pago[indice]}")


def _buscar_indice_venta(codigos_ventas, codigo):
    i = 0
    while i < len(codigos_ventas):
        if codigos_ventas[i] == codigo:
            return i
        i += 1
    return -1
