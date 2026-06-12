def es_numero(entrada, tipo):
    match tipo:
        case "int":
            try:
                int(entrada)
                return True
            except:
                return False
        case "float":
            try:
                float(entrada)
                return True
            except:
                return False
        case _:
            return False


def validar_entrada_numerica_en_lista(entrada, lista):
    while (not es_numero(entrada, "int") or int(entrada) in lista or int(entrada) <= 0):
        print("La entrada ingresada es inválida. Debe ser un NÚMERO positivo y no debe existir en la lista.")
        entrada = input("Ingrese nuevamente la entrada: ")
    return int(entrada)


def validar_edad(entrada):
    while (not es_numero(entrada, "int") or int(entrada) <= 0 or int(entrada) >= 99):
        print("La entrada ingresada es inválida. Debe ser un NÚMERO positivo.")
        entrada = input("Ingrese nuevamente la entrada: ")
    return int(entrada)


def validar_tipo(entrada):
    while (not es_numero(entrada, "int") or int(entrada) < 1 or int(entrada) > 2):
        print("La entrada ingresada es inválida. Debe ser un NÚMERO entre 1 y 2.")
        entrada = input("Ingrese nuevamente la entrada: ")
    return int(entrada)


def validar_precio(entrada):
    while (not es_numero(entrada, "float") or float(entrada) < 1):
        print("El valor ingresado es inválido.")
        entrada = input("Ingrese un precio válido: ")
    return float(entrada)


def validar_codigo_existente(entrada, codigos):
    while not es_numero(entrada, "int") or int(entrada) not in codigos:
        print("Ingrese un código existente y válido.")
        entrada = input("Ingrese nuevamente: ")
    return int(entrada)


def validar_entero_positivo(entrada):
    while not es_numero(entrada, "int") or int(entrada) <= 0:
        print("Ingrese un número entero positivo.")
        entrada = input("Ingrese nuevamente: ")
    return int(entrada)


def validar_opcion_entre(entrada, minimo, maximo):
    while not es_numero(entrada, "int") or int(entrada) < minimo or int(entrada) > maximo:
        print(f"Ingrese un número entre {minimo} y {maximo}.")
        entrada = input("Ingrese nuevamente: ")
    return int(entrada)
