from validaciones.validadores import validar_codigo_existente, validar_entero_positivo, validar_opcion_entre
from crud.clientes import modificar_cliente, ver_clientes
from crud.productos import modificar_producto, ver_productos
from utils.utilidades import (
    ordenar_insercion,
    preguntar_orden,
    obtener_indice_por_codigo,
    pedir_indice_por_codigo,
    eliminar_en_listas_paralelas,
)
from utils.estadisticas import traducir_medio


def ver_ventas(codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
               ventas_productos, codigos_productos, nombres_productos,
               ventas_cantidades, precios_productos, medios_pago):
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

        medio = traducir_medio(medios_pago[i])
        print(f"Venta {codigos_ventas[i]} | {nombre_cliente} | {nombre_producto} x{ventas_cantidades[i]} | {medio} | ${total:.2f}")
        i += 1


def listar_ventas(codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
                  ventas_productos, codigos_productos, nombres_productos,
                  ventas_cantidades, precios_productos, medios_pago):
    entrada = preguntar_orden()
    orden = validar_opcion_entre(entrada, 1, 3)

    if orden == 1:
        ver_ventas(codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
                   ventas_productos, codigos_productos, nombres_productos,
                   ventas_cantidades, precios_productos, medios_pago)
        return

    es_descendente = orden == 3
    print("Ordenar por: 1. Codigo 2. Cantidad 3. Medio de pago")
    entrada = input("Seleccione una opcion: ")
    campo = validar_opcion_entre(entrada, 1, 3)

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
               listas_ordenadas[3], precios_productos, listas_ordenadas[4])


def crear_venta(codigos_ventas, ventas_clientes, ventas_productos, ventas_cantidades, medios_pago,
                codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes,
                codigos_productos, nombres_productos, precios_productos):
    print("\n--- NUEVA VENTA ---")
    ver_clientes(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes)
    entrada = input("Codigo de cliente: ")
    cod_cliente = validar_codigo_existente(entrada, codigos_clientes)

    ver_productos(codigos_productos, nombres_productos, precios_productos)
    entrada = input("Codigo de producto: ")
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
               ventas_cantidades, precios_productos, medios_pago)
    _, indice_venta = pedir_indice_por_codigo("Codigo de venta: ", codigos_ventas)
    if indice_venta == -1:
        print("Codigo de venta invalido")
        return

    entrada = input("Modificar: 1. Cliente 2. Producto 3. Cantidad 4. Medio de pago: ")
    mod = validar_opcion_entre(entrada, 1, 4)

    if mod == 1:
        modificar_cliente(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes)
    elif mod == 2:
        modificar_producto(codigos_productos, nombres_productos, precios_productos)
    elif mod == 3:
        entrada = input("Nueva cantidad: ")
        cantidad = validar_entero_positivo(entrada)
        cantidad_vieja = ventas_cantidades[indice_venta]
        ventas_cantidades[indice_venta] = cantidad
        print(f"Se cambio la cantidad de {cantidad_vieja} a {cantidad}.")
    else:
        print("1. Efectivo  2. Tarjeta  3. Transferencia")
        entrada = input("Nuevo medio de pago: ")
        nuevo_medio = validar_opcion_entre(entrada, 1, 3)
        medio_viejo = medios_pago[indice_venta]
        medios_pago[indice_venta] = nuevo_medio
        print(f"Se cambio el medio de pago de {medio_viejo} a {nuevo_medio}.")


def buscar_venta(codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
                 ventas_productos, codigos_productos, nombres_productos, ventas_cantidades, precios_productos, medios_pago):
    _, indice = pedir_indice_por_codigo("Ingrese el codigo que desea buscar: ", codigos_ventas)
    mostrar_venta(indice, codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
                  ventas_productos, codigos_productos, nombres_productos, ventas_cantidades, precios_productos, medios_pago)


def mostrar_venta(indice, codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
                  ventas_productos, codigos_productos, nombres_productos, ventas_cantidades, precios_productos, medios_pago):
    if indice == -1:
        print("No se encontro el valor en la lista.")
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

    medio = traducir_medio(medios_pago[indice])
    print(f"Cod: {codigos_ventas[indice]} | {nombre_cliente} | {nombre_producto} x{ventas_cantidades[indice]} | Medio: {medio}")


def eliminar_venta(codigos_ventas, ventas_clientes, ventas_productos, ventas_cantidades, medios_pago,
                   codigos_clientes, nombres_clientes, codigos_productos, nombres_productos, precios_productos):
    print("\n--- ELIMINAR VENTA ---")
    ver_ventas(codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
               ventas_productos, codigos_productos, nombres_productos,
               ventas_cantidades, precios_productos, medios_pago)
    cod_venta, indice = pedir_indice_por_codigo("Codigo de venta a eliminar: ", codigos_ventas)
    if indice == -1:
        print("Codigo no encontrado.")
        return

    eliminar_en_listas_paralelas(
        [codigos_ventas, ventas_clientes, ventas_productos, ventas_cantidades, medios_pago],
        indice,
    )
    print(f"Venta {cod_venta} eliminada correctamente.")
