# Sistema de Gestión de ventas.

usuarios = ["admin", "aa"]
claves = ["1234", "22"]

productos = []
precios = []
stock = []

ventas_productos = []
ventas_cantidades = []
ventas_totales = []

'''Retorna True o False según el acceso del usuario'''
def login():
    acceso = False
    i = 0

    while acceso == False and i < len(usuarios):
        usuario_actual = input("Usuario: ")
        clave_actual = input("Clave: ")

        if usuario_actual == usuarios[i] and clave_actual == claves[i]:
            return True
        i += 1

    return False

login_usuario = login()

if login_usuario:
    print("Usuario correcto")
else:
    print("Usuario incorrecto")