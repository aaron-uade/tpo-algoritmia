from validaciones.validadores import es_numero, validar_entrada_numerica_en_lista, validar_edad, validar_tipo
from utils.utilidades import ordenar_burbuja, preguntar_orden, obtener_indice_por_codigo


def ver_clientes(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes):
    print("\n--- CLIENTES ---")
    i = 0
    while i < len(codigos_clientes):
        tipo = "Regular" if tipos_clientes[i] == 1 else "Frecuente"
        print(f"Cod: {codigos_clientes[i]} | {nombres_clientes[i]} | Edad: {edades_clientes[i]} | {tipo}")
        i += 1


def listar_clientes(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes):
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


def crear_cliente(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes):
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


def modificar_cliente(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes):
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

    _modificar_campos_cliente(indice_cliente, nombres_clientes, edades_clientes, tipos_clientes)


def buscar_cliente(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes):
    entrada = input("Ingrese el código que desea buscar: ")
    while not es_numero(entrada, "int"):
        entrada = input("Ingrese un código numérico: ")
    codigo = int(entrada)
    indice = _buscar_indice_cliente(codigo, codigos_clientes)
    mostrar_cliente(indice, codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes)


def mostrar_cliente(indice, codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes):
    if indice == -1:
        print("No se encontró el valor en la lista.")
        return

    tipo = "Regular" if tipos_clientes[indice] == 1 else "Frecuente"
    print(f"Cod: {codigos_clientes[indice]} | {nombres_clientes[indice]} | Edad: {edades_clientes[indice]} | {tipo}")


def _buscar_indice_cliente(codigo, codigos_clientes):
    return obtener_indice_por_codigo(codigos_clientes, codigo)


def _modificar_campos_cliente(indice, nombres_clientes, edades_clientes, tipos_clientes):
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
