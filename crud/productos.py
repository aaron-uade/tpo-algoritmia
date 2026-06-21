from validaciones.validadores import (
    es_numero,
    validar_entrada_numerica_en_lista,
    validar_precio,
    validar_opcion_entre,
)
from utils.utilidades import (
    ordenar_seleccion,
    preguntar_orden,
    pedir_indice_por_codigo,
    existe_en_lista,
    eliminar_en_listas_paralelas,
)


def ver_productos(codigos_productos, nombres_productos, precios_productos):
    print("\n--- PRODUCTOS ---")
    i = 0
    while i < len(codigos_productos):
        print(f"Cod: {codigos_productos[i]} | {nombres_productos[i]} | ${precios_productos[i]:.2f}")
        i += 1


def listar_productos(codigos_productos, nombres_productos, precios_productos):
    entrada = preguntar_orden()
    orden = validar_opcion_entre(entrada, 1, 3)

    if orden == 1:
        ver_productos(codigos_productos, nombres_productos, precios_productos)
        return

    es_descendente = orden == 3
    print("Ordenar por: 1. Codigo 2. Precio")
    entrada = input("Seleccione una opcion: ")
    campo = validar_opcion_entre(entrada, 1, 2)

    indice_clave = 0 if campo == 1 else 2
    listas = [codigos_productos, nombres_productos, precios_productos]
    listas_ordenadas = ordenar_seleccion(listas, indice_clave, es_descendente)
    ver_productos(listas_ordenadas[0], listas_ordenadas[1], listas_ordenadas[2])


def crear_producto(codigos_productos, nombres_productos, precios_productos):
    print("\n--- NUEVO PRODUCTO---")
    ver_productos(codigos_productos, nombres_productos, precios_productos)

    entrada_producto = input("Codigo de producto: ")
    cod_producto = validar_entrada_numerica_en_lista(entrada_producto, codigos_productos)

    nombre_producto = input("Nombre del producto ")

    entrada_precio = input("Precio del producto ")
    precio_producto = validar_precio(entrada_precio)

    codigos_productos.append(cod_producto)
    nombres_productos.append(nombre_producto)
    precios_productos.append(precio_producto)


def modificar_producto(codigos_productos, nombres_productos, precios_productos):
    ver_productos(codigos_productos, nombres_productos, precios_productos)
    _, indice = pedir_indice_por_codigo("Codigo de producto: ", codigos_productos)
    if indice == -1:
        print("Ingrese un codigo valido: ")
        return

    _modificar_campos_producto(indice, nombres_productos, precios_productos)


def buscar_producto(codigos_productos, nombres_productos, precios_productos):
    _, indice = pedir_indice_por_codigo("Ingrese el codigo que desea buscar: ", codigos_productos)
    mostrar_producto(indice, codigos_productos, nombres_productos, precios_productos)


def mostrar_producto(indice, codigos_productos, nombres_productos, precios_productos):
    if indice == -1:
        print("No se encontro el valor en la lista.")
        return
    print(f"Cod: {codigos_productos[indice]} | {nombres_productos[indice]} | Precio: ${precios_productos[indice]:.2f}")

def _modificar_campos_producto(indice, nombres_productos, precios_productos):
    entrada = input("Modificar: 1. Nombre 2. Precio: ")
    mod = validar_opcion_entre(entrada, 1, 2)

    if mod == 1:
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nombre_viejo = nombres_productos[indice]
        nombres_productos[indice] = nuevo_nombre
        print(f"Se cambio {nombre_viejo} a {nuevo_nombre}.")
    else:
        entrada = input("Ingrese el nuevo precio: ")
        while not es_numero(entrada, "float"):
            print("Ingrese un numero valido.")
            entrada = input("Ingrese el nuevo precio: ")
        nuevo_precio = float(entrada)
        precio_viejo = precios_productos[indice]
        precios_productos[indice] = nuevo_precio
        print(f"Se cambio el precio de {nombres_productos[indice]} de ${precio_viejo} a ${nuevo_precio}.")


def eliminar_producto(codigos_productos, nombres_productos, precios_productos, ventas_productos):
    print("\n--- ELIMINAR PRODUCTO ---")
    ver_productos(codigos_productos, nombres_productos, precios_productos)

    cod_producto, indice = pedir_indice_por_codigo("Codigo de producto a eliminar: ", codigos_productos)
    if indice == -1:
        print("Codigo no encontrado.")
        return

    if existe_en_lista(ventas_productos, cod_producto):
        print(f"No se puede eliminar: {nombres_productos[indice]} tiene ventas registradas.")
        return

    nombre = nombres_productos[indice]
    eliminar_en_listas_paralelas(
        [codigos_productos, nombres_productos, precios_productos],
        indice,
    )
    print(f"Producto {nombre} eliminado correctamente.")
