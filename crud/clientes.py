from validaciones.validadores import (
    es_numero,
    validar_entrada_numerica_en_lista,
    validar_edad,
    validar_tipo,
    validar_opcion_entre,
)
from utils.utilidades import (
    ordenar_burbuja,
    preguntar_orden,
    pedir_indice_por_codigo,
    existe_en_lista,
    eliminar_en_listas_paralelas,
    busqueda_binaria,
)


def ver_clientes(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes):
    print("\n--- CLIENTES ---")
    i = 0
    while i < len(codigos_clientes):
        tipo = "Regular" if tipos_clientes[i] == 1 else "Frecuente"
        print(f"Cod: {codigos_clientes[i]} | {nombres_clientes[i]} | Edad: {edades_clientes[i]} | {tipo}")
        i += 1


def listar_clientes(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes):
    entrada = preguntar_orden()
    orden = validar_opcion_entre(entrada, 1, 3)

    if orden == 1:
        ver_clientes(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes)
        return

    es_descendente = orden == 3
    print("Ordenar por: 1. Codigo 2. Edad")
    entrada = input("Seleccione una opcion: ")
    campo = validar_opcion_entre(entrada, 1, 2)

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
    _, indice_cliente = pedir_indice_por_codigo("Codigo de cliente: ", codigos_clientes)
    if indice_cliente == -1:
        print("Codigo invalido")
        return

    _modificar_campos_cliente(indice_cliente, nombres_clientes, edades_clientes, tipos_clientes)


def buscar_cliente(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes):
    entrada = input("Ingrese el codigo que desea buscar: ")
    while not es_numero(entrada, "int"):
        print("Ingrese un numero valido.")
        entrada = input("Ingrese el codigo que desea buscar: ")

    codigo = int(entrada)

    listas = [codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes]
    listas_ordenadas = ordenar_burbuja(listas, 0, False)
    indice = busqueda_binaria(listas_ordenadas[0], codigo)

    if indice == -1:
        print("No se encontro el valor en la lista.")
        return

    mostrar_cliente(indice, listas_ordenadas[0], listas_ordenadas[1], listas_ordenadas[2], listas_ordenadas[3])


def mostrar_cliente(indice, codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes):
    if indice == -1:
        print("No se encontro el valor en la lista.")
        return

    tipo = "Regular" if tipos_clientes[indice] == 1 else "Frecuente"
    print(f"Cod: {codigos_clientes[indice]} | {nombres_clientes[indice]} | Edad: {edades_clientes[indice]} | {tipo}")

def _modificar_campos_cliente(indice, nombres_clientes, edades_clientes, tipos_clientes):
    entrada = input("Modificar: 1. Nombre 2. Edad 3. Tipo: ")
    mod = validar_opcion_entre(entrada, 1, 3)

    if mod == 1:
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nombre_viejo = nombres_clientes[indice]
        nombres_clientes[indice] = nuevo_nombre
        print(f"Se cambio {nombre_viejo} a {nuevo_nombre}.")
    elif mod == 2:
        entrada = input("Ingrese la nueva edad: ")
        while not es_numero(entrada, "int"):
            print("Ingrese un numero valido.")
            entrada = input("Ingrese la nueva edad: ")
        nueva_edad = int(entrada)
        edad_vieja = edades_clientes[indice]
        edades_clientes[indice] = nueva_edad
        print(f"Se cambio la edad de {nombres_clientes[indice]} de {edad_vieja} a {nueva_edad} anios.")
    else:
        tipo_viejo = tipos_clientes[indice]
        tipos_clientes[indice] = 2 if tipo_viejo == 1 else 1
        tipo_nuevo = "Frecuente" if tipos_clientes[indice] == 2 else "Regular"
        print(f"Se cambio el tipo de {nombres_clientes[indice]} a {tipo_nuevo}.")


def eliminar_cliente(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes, ventas_clientes):
    ver_clientes(codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes)
    cod_cliente, indice_cliente = pedir_indice_por_codigo("Codigo de cliente a eliminar: ", codigos_clientes)
    if indice_cliente == -1:
        print("Codigo invalido")
        return

    if existe_en_lista(ventas_clientes, cod_cliente):
        print("No se puede eliminar el cliente porque tiene ventas asociadas.")
        return

    eliminar_en_listas_paralelas(
        [codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes],
        indice_cliente,
    )
    print("Cliente eliminado exitosamente.")
