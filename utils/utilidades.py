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

def obtener_indice_por_codigo(codigos, codigo):
    i = 0
    while i < len(codigos):
        if codigos[i] == codigo:
            return i
        i += 1
    return -1


def mostrar_menu_principal():
    print("\n--- MENU PRINCIPAL ---")
    print("1. Clientes")
    print("2. Productos")
    print("3. Ventas")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion


def mostrar_submenu(nombre):
    print(f"\n--- {nombre.upper()} ---")
    print("1. Listar")
    print("2. Nuevo")
    print("3. Modificar")
    print("4. Buscar")
    print("5. Volver al menú principal")
    opcion = input("Selecciona una opción: ")
    return opcion


def preguntar_orden():
    print("\n¿Cómo desea ver el listado?")
    print("1. Orden de carga (sin ordenar)")
    print("2. Ascendente")
    print("3. Descendente")
    opcion = input("Selecciona una opción: ")
    return opcion


def ordenar_burbuja(listas, indice_clave, es_descendente):
    copias = []
    i = 0
    while i < len(listas):
        copias.append(listas[i][:])
        i += 1

    n = len(copias[indice_clave])
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if es_descendente:
                cambiar = copias[indice_clave][j] < copias[indice_clave][j + 1]
            else:
                cambiar = copias[indice_clave][j] > copias[indice_clave][j + 1]

            if cambiar:
                k = 0
                while k < len(copias):
                    copias[k][j], copias[k][j + 1] = copias[k][j + 1], copias[k][j]
                    k += 1
            j += 1
        i += 1

    return copias


def ordenar_seleccion(listas, indice_clave, es_descendente):
    copias = []
    i = 0
    while i < len(listas):
        copias.append(listas[i][:])
        i += 1

    n = len(copias[indice_clave])
    i = 0
    while i < n - 1:
        indice_elegido = i
        j = i + 1
        while j < n:
            if es_descendente:
                mejor = copias[indice_clave][j] > copias[indice_clave][indice_elegido]
            else:
                mejor = copias[indice_clave][j] < copias[indice_clave][indice_elegido]

            if mejor:
                indice_elegido = j
            j += 1

        if indice_elegido != i:
            k = 0
            while k < len(copias):
                copias[k][i], copias[k][indice_elegido] = copias[k][indice_elegido], copias[k][i]
                k += 1
        i += 1

    return copias


def ordenar_insercion(listas, indice_clave, es_descendente):
    copias = []
    i = 0
    while i < len(listas):
        copias.append(listas[i][:])
        i += 1

    n = len(copias[indice_clave])
    i = 1
    while i < n:
        j = i
        while j > 0:
            if es_descendente:
                mover = copias[indice_clave][j - 1] < copias[indice_clave][j]
            else:
                mover = copias[indice_clave][j - 1] > copias[indice_clave][j]

            if not mover:
                break

            k = 0
            while k < len(copias):
                copias[k][j - 1], copias[k][j] = copias[k][j], copias[k][j - 1]
                k += 1
            j -= 1
        i += 1

    return copias

def busqueda_secuencial(lista, valor):
    k = 0
    for k in range(len(lista) - 1):
        if lista[k] == valor:
            return k
        k += 1
    return -1

def busqueda_binaria(lista, valor):
    izq = 0
    der = len(lista) - 1

    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            izq = medio + 1
        elif lista[medio] > valor:
            der = medio - 1
    return -1