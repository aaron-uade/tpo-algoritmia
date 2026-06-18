from validaciones.validadores import es_numero, validar_entrada_numerica_en_lista, validar_precio
from utils.utilidades import ver_productos, ordenar_seleccion, preguntar_orden, obtener_indice_por_codigo


def listar_productos(codigos_productos, nombres_productos, precios_productos):
    entrada = preguntar_orden()
    while not es_numero(entrada, "int") or int(entrada) < 1 or int(entrada) > 3:
        print("Opción inválida.")
        entrada = preguntar_orden()
    orden = int(entrada)

    if orden == 1:
        ver_productos(codigos_productos, nombres_productos, precios_productos)
        return

    es_descendente = orden == 3
    print("Ordenar por: 1. Código 2. Precio")
    entrada = input("Seleccione una opción: ")
    while not es_numero(entrada, "int") or int(entrada) < 1 or int(entrada) > 2:
        print("Opción inválida.")
        entrada = input("Seleccione una opción: ")
    campo = int(entrada)

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
    entrada = input("Código de producto: ")
    while not es_numero(entrada, "int"):
        print("Ingrese un número válido.")
        entrada = input("Código de producto: ")
    cod_producto = int(entrada)

    indice = obtener_indice_por_codigo(codigos_productos, cod_producto)
    if indice == -1:
        print("Ingrese un código válido: ")
        return

    _modificar_campos_producto(indice, nombres_productos, precios_productos)


def buscar_producto(codigos_productos, nombres_productos, precios_productos):
    entrada = input("Ingrese el código que desea buscar: ")
    while not es_numero(entrada, "int"):
        entrada = input("Ingrese un código numérico: ")
    codigo = int(entrada)
    indice = _buscar_indice_producto(codigo, codigos_productos)
    mostrar_producto(indice, codigos_productos, nombres_productos, precios_productos)


def mostrar_producto(indice, codigos_productos, nombres_productos, precios_productos):
    if indice == -1:
        print("No se encontró el valor en la lista.")
        return
    print(f"Cod: {codigos_productos[indice]} | {nombres_productos[indice]} | Precio: ${precios_productos[indice]:.2f}")


def _buscar_indice_producto(codigo, codigos_productos):
    return obtener_indice_por_codigo(codigos_productos, codigo)


def _modificar_campos_producto(indice, nombres_productos, precios_productos):
    entrada = input("Modificar: 1. Nombre 2. Precio: ")
    while not es_numero(entrada, "int") or int(entrada) < 1 or int(entrada) > 2:
        print("Opción inválida.")
        entrada = input("Modificar: 1. Nombre 2. Precio: ")
    mod = int(entrada)

    if mod == 1:
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nombre_viejo = nombres_productos[indice]
        nombres_productos[indice] = nuevo_nombre
        print(f"Se cambió {nombre_viejo} a {nuevo_nombre}.")
    else:
        entrada = input("Ingrese el nuevo precio: ")
        while not es_numero(entrada, "float"):
            print("Ingrese un número válido.")
            entrada = input("Ingrese el nuevo precio: ")
        nuevo_precio = float(entrada)
        precio_viejo = precios_productos[indice]
        precios_productos[indice] = nuevo_precio
        print(f"Se cambió el precio de {nombres_productos[indice]} de ${precio_viejo} a ${nuevo_precio}.")
