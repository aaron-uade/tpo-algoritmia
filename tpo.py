# Sistema de Gestion de ventas

from crud.clientes import (
    listar_clientes, crear_cliente, modificar_cliente, buscar_cliente, eliminar_cliente
)
from crud.productos import (
    listar_productos, crear_producto, modificar_producto, buscar_producto, eliminar_producto
)
from crud.ventas import (
    listar_ventas, crear_venta, modificar_venta, buscar_venta, eliminar_venta
)
from validaciones.validadores import es_numero
from utils.utilidades import login, mostrar_menu_principal, mostrar_submenu
from constantes.constantes import (
    codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes,
    codigos_productos, nombres_productos, precios_productos,
    codigos_ventas, ventas_clientes, ventas_productos, ventas_cantidades,
    medios_pago, usuario, clave
)


def leer_opcion_valida(entrada):
    while not es_numero(entrada, "int"):
        entrada = input("Ingrese una opcion valida: ")
    return int(entrada)


def menu_clientes():
    while True:
        entrada = mostrar_submenu("Clientes")
        opcion = leer_opcion_valida(entrada)

        if opcion == 1:
            listar_clientes(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes)
        elif opcion == 2:
            crear_cliente(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes)
        elif opcion == 3:
            modificar_cliente(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes)
        elif opcion == 4:
            buscar_cliente(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes)
        elif opcion == 5:
            eliminar_cliente(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes, ventas_clientes)
        elif opcion == 6:
            break
        else:
            print("Opcion invalida")


def menu_productos():
    while True:
        entrada = mostrar_submenu("Productos")
        opcion = leer_opcion_valida(entrada)

        if opcion == 1:
            listar_productos(codigos_productos, nombres_productos, precios_productos)
        elif opcion == 2:
            crear_producto(codigos_productos, nombres_productos, precios_productos)
        elif opcion == 3:
            modificar_producto(codigos_productos, nombres_productos, precios_productos)
        elif opcion == 4:
            buscar_producto(codigos_productos, nombres_productos, precios_productos)
        elif opcion == 5:
            eliminar_producto(codigos_productos, nombres_productos, precios_productos, ventas_productos)
        elif opcion == 6:
            break
        else:
            print("Opcion invalida")


def menu_ventas():
    while True:
        entrada = mostrar_submenu("Ventas")
        opcion = leer_opcion_valida(entrada)

        if opcion == 1:
            listar_ventas(
                codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
                ventas_productos, codigos_productos, nombres_productos,
                ventas_cantidades, precios_productos, medios_pago
            )
        elif opcion == 2:
            crear_venta(
                codigos_ventas, ventas_clientes, ventas_productos, ventas_cantidades, medios_pago,
                codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes,
                codigos_productos, nombres_productos, precios_productos
            )
        elif opcion == 3:
            modificar_venta(
                codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
                edades_clientes, tipos_clientes,
                ventas_productos, codigos_productos, nombres_productos,
                ventas_cantidades, precios_productos, medios_pago
            )
        elif opcion == 4:
            buscar_venta(
                codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
                ventas_productos, codigos_productos, nombres_productos,
                ventas_cantidades, precios_productos, medios_pago
            )
        elif opcion == 5:
            eliminar_venta(
                codigos_ventas, ventas_clientes, ventas_productos, ventas_cantidades, medios_pago,
                codigos_clientes, nombres_clientes, codigos_productos, nombres_productos, precios_productos
            )
        elif opcion == 6:
            break
        else:
            print("Opcion invalida.")


login_usuario = login(usuario, clave)

if login_usuario:
    print("Usuario correcto\n")

    salir = False
    while not salir:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_productos()
        elif opcion == "3":
            menu_ventas()
        elif opcion == "4":
            print("Hasta luego")
            salir = True
        else:
            print("Opcion invalida")
else:
    print("Usuario incorrecto")
