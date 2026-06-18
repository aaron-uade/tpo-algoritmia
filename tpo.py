# Sistema de Gestión de ventas

from validaciones.validadores import (
    es_numero, validar_entrada_numerica_en_lista, validar_edad, validar_tipo,
    validar_precio, validar_codigo_existente, validar_entero_positivo, validar_opcion_entre
)
from utils.utilidades import (
    login, mostrar_menu_principal, mostrar_submenu, preguntar_orden,
    obtener_indice_por_codigo, ver_clientes, ver_productos, ver_ventas,
    ordenar_burbuja, ordenar_seleccion, ordenar_insercion, 
    busqueda_secuencial, busqueda_binaria
)

from constantes.constantes import (
    nombres_clientes, edades_clientes, tipos_clientes, codigos_clientes,
    nombres_productos, precios_productos, codigos_productos, 
    codigos_ventas, ventas_clientes, ventas_productos, ventas_clientes, ventas_cantidades,
    medios_pago, edad_maxima, usuarios, claves
)

def modificar_campos_cliente(indice):
    entrada = input("Modificar: 1. Nombre 2. Edad 3. Tipo: ")
    while not es_numero(entrada, "int") or int(entrada) < 1 or int(entrada) > 3:
        print("Opción inválida.")
        entrada = input("Modificar: 1. Nombre 2. Edad 3. Tipo: ")
    mod = int(entrada)

    if mod == 1:
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nombre_viejo = nombres_clientes[indice]
        nombres_clientes[indice] = nuevo_nombre
        print(f"Se cambió {nombre_viejo} a {nuevo_nombre}.")

    elif mod == 2:
        entrada = input("Ingrese la nueva edad: ")
        while not es_numero(entrada, "int"):
            print("Ingrese un número válido.")
            entrada = input("Ingrese la nueva edad: ")
        nueva_edad = int(entrada)
        edad_vieja = edades_clientes[indice]
        edades_clientes[indice] = nueva_edad
        print(f"Se cambió la edad de {nombres_clientes[indice]} de {edad_vieja} a {nueva_edad} años.")

    else:
        tipo_viejo = tipos_clientes[indice]
        tipos_clientes[indice] = 2 if tipo_viejo == 1 else 1
        tipo_nuevo = "Frecuente" if tipos_clientes[indice] == 2 else "Regular"
        print(f"Se cambió el tipo de {nombres_clientes[indice]} a {tipo_nuevo}.")


def modificar_cliente():
    ver_clientes(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes)
    entrada = input("Código de cliente: ")
    while not es_numero(entrada, "int"):
        print("Ingrese un número válido.")
        entrada = input("Código de cliente: ")
    cod_cliente = int(entrada)
    indice_cliente = obtener_indice_por_codigo(codigos_clientes, cod_cliente)
    if indice_cliente == -1:
        print("Código inválido")
        return
    modificar_campos_cliente(indice_cliente)


def modificar_campos_producto(indice):
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


def modificar_producto():
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

    modificar_campos_producto(indice)


def modificar_venta():
    ver_ventas(codigos_ventas, ventas_clientes, codigos_clientes, nombres_clientes,
               ventas_productos, codigos_productos, nombres_productos,
               ventas_cantidades, precios_productos)
    entrada = input("Código de venta: ")
    while not es_numero(entrada, "int"):
        print("Ingrese un número válido.")
        entrada = input("Código de venta: ")
    cod_venta = int(entrada)

    indice_venta = -1
    i = 0
    while i < len(codigos_ventas):
        if codigos_ventas[i] == cod_venta:
            indice_venta = i
        i += 1

    if indice_venta == -1:
        print("Código de venta inválido")
        return

    entrada = input("Modificar: 1. Cliente 2. Producto 3. Cantidad 4. Medio de pago: ")
    while not es_numero(entrada, "int") or int(entrada) < 1 or int(entrada) > 4:
        print("Opción inválida.")
        entrada = input("Modificar: 1. Cliente 2. Producto 3. Cantidad 4. Medio de pago: ")
    mod = int(entrada)

    if mod == 1:
        indice_cliente = obtener_indice_por_codigo(codigos_clientes, ventas_clientes[indice_venta])
        if indice_cliente == -1:
            print("Cliente de la venta no existe en el registro.")
            return
        modificar_campos_cliente(indice_cliente)

    elif mod == 2:
        indice_producto = obtener_indice_por_codigo(codigos_productos, ventas_productos[indice_venta])
        if indice_producto == -1:
            print("Producto de la venta no existe en el catálogo.")
            return
        modificar_campos_producto(indice_producto)

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


def modificar():
    print("\n--- MODIFICAR ---")
    entrada = input("1. Cliente 2. Producto 3. Venta: ")
    while not es_numero(entrada, "int") or int(entrada) < 1 or int(entrada) > 3:
        print("Opción inválida.")
        entrada = input("1. Cliente 2. Producto 3. Venta: ")
    conjunto = int(entrada)

    if conjunto == 1:
        modificar_cliente()
    elif conjunto == 2:
        modificar_producto()
    else:
        modificar_venta()


def nuevo_cliente():
    print("\n--- NUEVO CLIENTE---")
    ver_clientes(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes)
    entrada_cliente = input("Codigo de cliente: ")

    cod_cliente = validar_entrada_numerica_en_lista(entrada_cliente, codigos_clientes)

    nombre_cliente = input("Nombre de cliente: ")

    entrada_edad = input("Edad de cliente: ")

    edad_cliente = validar_edad(entrada_edad)
    
    entrada_tipo_cliente = input("Tipo de cliente: 1. Regular 2. Frecuente ")

    tipo_cliente = validar_tipo(entrada_tipo_cliente)
    
    codigos_clientes.append(cod_cliente)
    nombres_clientes.append(nombre_cliente)
    edades_clientes.append(edad_cliente)
    tipos_clientes.append(tipo_cliente)


def nuevo_producto():
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

def nueva_venta():
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

    codigos_ventas.append(max(codigos_ventas) + 1)
    ventas_clientes.append(cod_cliente)
    ventas_productos.append(cod_producto)
    ventas_cantidades.append(cantidad)
    medios_pago.append(medio)
    print("Venta registrada")


def dar_de_alta():
    print("\n---DAR DE ALTA---")
    print("1-Cliente")
    print("2-Producto")
    print("3-Venta")
    alta = input("¿Qué desea dar de alta? ")

    if alta == "1":
        nuevo_cliente()
    elif alta == "2":
        nuevo_producto()
    elif alta == "3":
        nueva_venta()
    else:
        print("\n No ingresó una de las opciones disponibles")


def listar_clientes():
    entrada = preguntar_orden()
    while not es_numero(entrada, "int") or int(entrada) < 1 or int(entrada) > 3:
        print("Opción inválida.")
        entrada = preguntar_orden()
    orden = int(entrada)

    if orden == 1:
        ver_clientes(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes)
        return

    es_descendente = orden == 3

    print("Ordenar por: 1. Código 2. Edad")
    entrada = input("Seleccione una opción: ")
    while not es_numero(entrada, "int") or int(entrada) < 1 or int(entrada) > 2:
        print("Opción inválida.")
        entrada = input("Seleccione una opción: ")
    campo = int(entrada)

    indice_clave = 0 if campo == 1 else 2

    listas = [codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes]
    listas_ordenadas = ordenar_burbuja(listas, indice_clave, es_descendente)
    ver_clientes(listas_ordenadas[0], listas_ordenadas[1], listas_ordenadas[2], listas_ordenadas[3])


def listar_productos():
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


def listar_ventas():
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
    
def buscar(clase):
    entrada = input("Ingrese el código que desea buscar: ")
    while not es_numero(entrada, "int"):
        entrada = input("Ingrese un código numérico: ")

    match clase:
        case "cliente":
            indice = busqueda_secuencial(codigos_clientes, int(entrada))
            mostrar("cliente", indice)
        case "venta":
            indice = busqueda_secuencial(codigos_ventas, int(entrada))
            mostrar("venta", indice)
        case "producto":
            indice = busqueda_binaria(codigos_productos, int(entrada))
            mostrar("producto", indice)

def mostrar(clase, indice):
    if indice == -1:
        print(f"No se encontró el valor en la lista.")
        return
    
    match clase:
        case "cliente":
            tipo = "Regular" if tipos_clientes[indice] == 1 else "Frecuente"
            print(f"Cod: {codigos_clientes[indice]} | {nombres_clientes[indice]} | Edad: {edades_clientes[indice]} | {tipo}")
        case "venta":
            print(f"Cod: {codigos_ventas[indice]} | Cod Cliente: {ventas_clientes[indice]} | Cantidades: {ventas_cantidades[indice]} | Producto: {ventas_productos[indice]}")
        case "producto":
            print(f"Cod: {codigos_productos[indice]} | {nombres_productos[indice]} | Precio: ${precios_productos[indice]}")


def menu_clientes():
    volver = False
    while volver == False:
        entrada = mostrar_submenu("Clientes")

        while not es_numero(entrada, "int"):
            entrada = input("Ingrese una opción válida: ")

        opcion = int(entrada)

        if opcion == 1:
            listar_clientes()
        elif opcion == 2:
            nuevo_cliente()
        elif opcion == 3:
            modificar_cliente()
        elif opcion == 4:
            buscar("cliente")
        elif opcion == 5:
            volver = True
        else:
            print("Opción inválida")


def menu_productos():
    volver = False
    while volver == False:
        entrada = mostrar_submenu("Productos")

        while not es_numero(entrada, "int"):
            entrada = input("Ingrese una opción válida: ")

        opcion = int(entrada)

        if opcion == 1:
            listar_productos()
        elif opcion == 2:
            nuevo_producto()
        elif opcion == 3:
            modificar_producto()
        elif opcion == 4:
            buscar("producto")
        elif opcion == 5:
            volver = True
        else:
            print("Opción inválida")


def menu_ventas():
    volver = False
    while volver == False:
        entrada = mostrar_submenu("Ventas")

        while not es_numero(entrada, "int"):
            entrada = input("Ingrese una opción válida: ")
        
        opcion = int(entrada)

        if opcion == 1:
            listar_ventas()
        elif opcion == 2:
            nueva_venta()
        elif opcion == 3:
            modificar_venta()
        elif opcion == 4:
            buscar("venta")
        elif opcion == 5:
            volver = True
        else:
            print("Opción inválida.")

# Programa principal
login_usuario = login(usuarios, claves)

if login_usuario:
    print("Usuario correcto\n")

    salir = False
    while salir == False:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_productos()
        elif opcion == "3":
            menu_ventas()
        elif opcion == "4":
            buscar("producto")
        elif opcion == "5":
            print("Hasta luego")
            salir = True
        else:
            print("Opción inválida")
else:
    print("Usuario incorrecto")
