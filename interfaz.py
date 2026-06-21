import tkinter as tk

from constantes.constantes import (
    usuario, clave,
    codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes,
    codigos_productos, nombres_productos, precios_productos,
    codigos_ventas, ventas_clientes, ventas_productos, ventas_cantidades, medios_pago,
)
from utils.estadisticas import (
    traducir_medio, armar_matriz_estadisticas, listas_a_matriz_ventas
)
from utils.utilidades import (
    obtener_indice_por_codigo,
    existe_en_lista,
    eliminar_en_listas_paralelas,
)


root = tk.Tk()
root.title("Sistema de Gestion")
root.geometry("760x520")

logueado = False
seccion_actual = None
accion_actual = None
paso_actual = 0
datos_ingresados = {}

campos = {
    "clientes_agregar": ["Codigo", "Nombre", "Edad", "Tipo (1=Regular, 2=Frecuente)"],
    "clientes_modificar": ["Codigo", "Nombre", "Edad", "Tipo (1=Regular, 2=Frecuente)"],
    "clientes_buscar": ["Codigo"],
    "clientes_eliminar": ["Codigo"],
    "productos_agregar": ["Codigo", "Nombre", "Precio"],
    "productos_modificar": ["Codigo", "Nombre", "Precio"],
    "productos_buscar": ["Codigo"],
    "productos_eliminar": ["Codigo"],
    "ventas_agregar": ["Codigo", "Cliente", "Producto", "Cantidad", "Pago (1=Efectivo, 2=Tarjeta, 3=Transferencia)"],
    "ventas_modificar": ["Codigo", "Cliente", "Producto", "Cantidad", "Pago (1=Efectivo, 2=Tarjeta, 3=Transferencia)"],
    "ventas_buscar": ["Codigo"],
    "ventas_eliminar": ["Codigo"],
}


login_window = tk.Frame(root)
login_window.pack()

tk.Label(login_window, text="INICIAR SESION", font=("Arial", 14)).pack(pady=10)

tk.Label(login_window, text="Usuario").pack()
user_entry = tk.Entry(login_window)
user_entry.pack()

tk.Label(login_window, text="Contrasenia").pack()
pass_entry = tk.Entry(login_window, show="*")
pass_entry.pack()

error_msg = tk.Label(login_window, text="", fg="red")
error_msg.pack()


def hacer_login():
    global logueado

    user = user_entry.get()
    password = pass_entry.get()

    if user == usuario and password == clave:
        logueado = True
        login_window.pack_forget()
        main_window.pack()
        error_msg.config(text="")
    else:
        error_msg.config(text="Usuario o contrasenia incorrectos")


tk.Button(login_window, text="Entrar", command=hacer_login).pack(pady=10)

main_window = tk.Frame(root)

tk.Label(main_window, text="MENU PRINCIPAL", font=("Arial", 12)).pack(pady=5)

menu_buttons = tk.Frame(main_window)
menu_buttons.pack()


def seleccionar_seccion(seccion):
    global seccion_actual, accion_actual, paso_actual, datos_ingresados

    seccion_actual = seccion
    accion_actual = None
    paso_actual = 0
    datos_ingresados = {}
    limpiar_submenu()
    llenar_submenu()
    prompt_label.config(text="")
    entrada_datos.delete(0, tk.END)
    mostrar(f"Selecciona que deseas hacer con {seccion.capitalize()}\n")


def mostrar_estadisticas():
    matriz_ventas = listas_a_matriz_ventas(
        codigos_ventas, medios_pago, ventas_productos,
        codigos_productos, ventas_cantidades, precios_productos
    )
    matriz_estadisticas = armar_matriz_estadisticas(matriz_ventas)

    texto = "ESTADISTICAS POR MEDIO DE PAGO\n"
    texto += f"{'Medio':<16}{'Cantidad':>10}{'Total':>12}\n"
    for nombre, cantidad, total in matriz_estadisticas:
        texto += f"{nombre:<16}{cantidad:>10}{total:>12.2f}\n"

    mostrar(texto)


def salir():
    root.destroy()


tk.Button(menu_buttons, text="Clientes", command=lambda: seleccionar_seccion("clientes"), width=12).pack(side="left", padx=5)
tk.Button(menu_buttons, text="Productos", command=lambda: seleccionar_seccion("productos"), width=12).pack(side="left", padx=5)
tk.Button(menu_buttons, text="Ventas", command=lambda: seleccionar_seccion("ventas"), width=12).pack(side="left", padx=5)
tk.Button(menu_buttons, text="Estadisticas", command=mostrar_estadisticas, width=12).pack(side="left", padx=5)
tk.Button(menu_buttons, text="Salir", command=salir, width=12).pack(side="left", padx=5)

submenu_frame = tk.Frame(main_window)
submenu_frame.pack(pady=5)

resultado_text = tk.Text(main_window, height=16, width=100)
resultado_text.pack(padx=5, pady=5)
resultado_text.config(state="disabled")

prompt_label = tk.Label(main_window, text="", font=("Arial", 10))
prompt_label.pack()

entrada_datos = tk.Entry(main_window, width=70)
entrada_datos.pack(pady=5)


def limpiar_submenu():
    for widget in submenu_frame.winfo_children():
        widget.destroy()


def llenar_submenu():
    tk.Button(submenu_frame, text="Listar", command=listar, width=12).pack(side="left", padx=3)
    tk.Button(submenu_frame, text="Agregar", command=iniciar_agregar, width=12).pack(side="left", padx=3)
    tk.Button(submenu_frame, text="Modificar", command=iniciar_modificar, width=12).pack(side="left", padx=3)
    tk.Button(submenu_frame, text="Buscar", command=iniciar_buscar, width=12).pack(side="left", padx=3)
    tk.Button(submenu_frame, text="Eliminar", command=iniciar_eliminar, width=12).pack(side="left", padx=3)
    tk.Button(submenu_frame, text="Volver", command=volver, width=12).pack(side="left", padx=3)


def mostrar(texto):
    resultado_text.config(state="normal")
    resultado_text.delete(1.0, tk.END)
    resultado_text.insert(tk.END, texto)
    resultado_text.config(state="disabled")


def limpiar_entrada():
    entrada_datos.delete(0, tk.END)
    entrada_datos.focus()


def finalizar_accion():
    global accion_actual, paso_actual, datos_ingresados

    accion_actual = None
    paso_actual = 0
    datos_ingresados = {}
    prompt_label.config(text="")
    entrada_datos.delete(0, tk.END)


def obtener_codigos_seccion(seccion):
    if seccion == "clientes":
        return codigos_clientes
    if seccion == "productos":
        return codigos_productos
    return codigos_ventas


def obtener_indice_seccion(seccion, codigo):
    return obtener_indice_por_codigo(obtener_codigos_seccion(seccion), codigo)


def tipo_cliente_texto(tipo):
    return "Regular" if tipo == 1 else "Frecuente"


def obtener_nombre_cliente(codigo_cliente):
    indice = obtener_indice_por_codigo(codigos_clientes, codigo_cliente)
    if indice == -1:
        return "Cliente desconocido"
    return nombres_clientes[indice]


def obtener_nombre_producto(codigo_producto):
    indice = obtener_indice_por_codigo(codigos_productos, codigo_producto)
    if indice == -1:
        return "Producto desconocido"
    return nombres_productos[indice]


def calcular_total_venta(indice_venta):
    indice_producto = obtener_indice_por_codigo(codigos_productos, ventas_productos[indice_venta])
    if indice_producto == -1:
        return 0
    return ventas_cantidades[indice_venta] * precios_productos[indice_producto]


def formatear_cliente(indice):
    return (
        f"Cod: {codigos_clientes[indice]} | {nombres_clientes[indice]} | "
        f"Edad: {edades_clientes[indice]} | {tipo_cliente_texto(tipos_clientes[indice])}"
    )


def formatear_producto(indice):
    return f"Cod: {codigos_productos[indice]} | {nombres_productos[indice]} | Precio: ${precios_productos[indice]:.2f}"


def formatear_venta(indice):
    cliente = obtener_nombre_cliente(ventas_clientes[indice])
    producto = obtener_nombre_producto(ventas_productos[indice])
    pago = traducir_medio(medios_pago[indice])
    total = calcular_total_venta(indice)
    return (
        f"Venta {codigos_ventas[indice]} | {cliente} | {producto} x{ventas_cantidades[indice]} | "
        f"{pago} | ${total:.2f}"
    )


def actualizar_prompt():
    if accion_actual is None:
        return

    clave = f"{seccion_actual}_{accion_actual.lower()}"
    lista_campos = campos.get(clave, [])

    if paso_actual < len(lista_campos):
        prompt_label.config(text=f"Ingresa {lista_campos[paso_actual]}:")

    limpiar_entrada()


def validar_codigo(valor, accion):
    try:
        codigo = int(valor)
    except ValueError:
        mostrar("El codigo debe ser un numero\n")
        return None

    indice = obtener_indice_seccion(seccion_actual, codigo)

    if accion == "agregar" and indice != -1:
        mostrar(f"Error: ya existe un registro con codigo {codigo}\n")
        return None

    if accion in ["modificar", "buscar", "eliminar"] and indice == -1:
        mostrar(f"Error: no existe un registro con codigo {codigo}\n")
        return None

    if accion == "eliminar":
        if seccion_actual == "clientes" and existe_en_lista(ventas_clientes, codigo):
            mostrar("No se puede eliminar el cliente porque tiene ventas asociadas.\n")
            return None

        if seccion_actual == "productos" and existe_en_lista(ventas_productos, codigo):
            mostrar("No se puede eliminar el producto porque tiene ventas asociadas.\n")
            return None

    return codigo


def validar_campo(nombre_campo, valor):
    accion = accion_actual.lower()

    if nombre_campo == "Codigo":
        return validar_codigo(valor, accion) is not None

    if seccion_actual == "clientes":
        if nombre_campo == "Edad":
            return validar_entero_positivo(valor, "La edad debe ser un numero entero positivo")
        if nombre_campo.startswith("Tipo"):
            return validar_rango_entero(valor, 1, 2, "El tipo debe ser 1 o 2")

    if seccion_actual == "productos" and nombre_campo == "Precio":
        return validar_float_positivo(valor, "El precio debe ser un numero positivo")

    if seccion_actual == "ventas":
        if nombre_campo == "Cliente":
            return validar_codigo_relacionado(valor, codigos_clientes, "cliente")
        if nombre_campo == "Producto":
            return validar_codigo_relacionado(valor, codigos_productos, "producto")
        if nombre_campo == "Cantidad":
            return validar_entero_positivo(valor, "La cantidad debe ser un numero entero positivo")
        if nombre_campo.startswith("Pago"):
            return validar_rango_entero(valor, 1, 3, "El pago debe ser 1, 2 o 3")

    return True


def validar_entero_positivo(valor, mensaje):
    try:
        numero = int(valor)
    except ValueError:
        mostrar(f"{mensaje}\n")
        return False

    if numero <= 0:
        mostrar(f"{mensaje}\n")
        return False

    return True


def validar_float_positivo(valor, mensaje):
    try:
        numero = float(valor)
    except ValueError:
        mostrar(f"{mensaje}\n")
        return False

    if numero <= 0:
        mostrar(f"{mensaje}\n")
        return False

    return True


def validar_rango_entero(valor, minimo, maximo, mensaje):
    try:
        numero = int(valor)
    except ValueError:
        mostrar(f"{mensaje}\n")
        return False

    if numero < minimo or numero > maximo:
        mostrar(f"{mensaje}\n")
        return False

    return True


def validar_codigo_relacionado(valor, codigos, nombre):
    try:
        codigo = int(valor)
    except ValueError:
        mostrar(f"El {nombre} debe ser un numero\n")
        return False

    if obtener_indice_por_codigo(codigos, codigo) == -1:
        mostrar(f"Error: no existe {nombre} con codigo {codigo}\n")
        return False

    return True


def procesar_input():
    global paso_actual

    if accion_actual is None:
        return

    valor = entrada_datos.get().strip()

    if not valor:
        mostrar("Por favor ingresa un valor\n")
        return

    clave = f"{seccion_actual}_{accion_actual.lower()}"
    lista_campos = campos.get(clave, [])

    if paso_actual >= len(lista_campos):
        return

    nombre_campo = lista_campos[paso_actual]

    if not validar_campo(nombre_campo, valor):
        limpiar_entrada()
        return

    datos_ingresados[nombre_campo] = valor
    paso_actual += 1

    if paso_actual >= len(lista_campos):
        if accion_actual == "Agregar":
            ejecutar_agregar()
        elif accion_actual == "Modificar":
            ejecutar_modificar()
        elif accion_actual == "Buscar":
            ejecutar_buscar()
        elif accion_actual == "Eliminar":
            ejecutar_eliminar()
    else:
        actualizar_prompt()


def listar():
    if seccion_actual == "clientes":
        texto = "CLIENTES\n"
        for i in range(len(codigos_clientes)):
            texto += f"{formatear_cliente(i)}\n"
        mostrar(texto)
    elif seccion_actual == "productos":
        texto = "PRODUCTOS\n"
        for i in range(len(codigos_productos)):
            texto += f"{formatear_producto(i)}\n"
        mostrar(texto)
    elif seccion_actual == "ventas":
        texto = "VENTAS\n"
        for i in range(len(codigos_ventas)):
            texto += f"{formatear_venta(i)}\n"
        mostrar(texto)
    else:
        mostrar("Selecciona una seccion\n")


def iniciar_accion(nombre):
    global accion_actual, paso_actual, datos_ingresados

    if seccion_actual is None:
        mostrar("Selecciona una seccion\n")
        return

    accion_actual = nombre
    paso_actual = 0
    datos_ingresados = {}
    actualizar_prompt()


def iniciar_agregar():
    iniciar_accion("Agregar")


def iniciar_modificar():
    iniciar_accion("Modificar")


def iniciar_buscar():
    iniciar_accion("Buscar")


def iniciar_eliminar():
    iniciar_accion("Eliminar")


def ejecutar_agregar():
    try:
        if seccion_actual == "clientes":
            codigo = int(datos_ingresados["Codigo"])
            nombre = datos_ingresados["Nombre"]
            edad = int(datos_ingresados["Edad"])
            tipo = int(datos_ingresados["Tipo (1=Regular, 2=Frecuente)"])

            codigos_clientes.append(codigo)
            nombres_clientes.append(nombre)
            edades_clientes.append(edad)
            tipos_clientes.append(tipo)
            mostrar(f"Cliente agregado: {formatear_cliente(len(codigos_clientes) - 1)}\n")

        elif seccion_actual == "productos":
            codigo = int(datos_ingresados["Codigo"])
            nombre = datos_ingresados["Nombre"]
            precio = float(datos_ingresados["Precio"])

            codigos_productos.append(codigo)
            nombres_productos.append(nombre)
            precios_productos.append(precio)
            mostrar(f"Producto agregado: {formatear_producto(len(codigos_productos) - 1)}\n")

        else:
            codigo = int(datos_ingresados["Codigo"])
            cliente = int(datos_ingresados["Cliente"])
            producto = int(datos_ingresados["Producto"])
            cantidad = int(datos_ingresados["Cantidad"])
            pago = int(datos_ingresados["Pago (1=Efectivo, 2=Tarjeta, 3=Transferencia)"])

            codigos_ventas.append(codigo)
            ventas_clientes.append(cliente)
            ventas_productos.append(producto)
            ventas_cantidades.append(cantidad)
            medios_pago.append(pago)
            mostrar(f"Venta agregada: {formatear_venta(len(codigos_ventas) - 1)}\n")

        finalizar_accion()
    except (KeyError, ValueError):
        mostrar("Error en los datos ingresados\n")


def ejecutar_modificar():
    try:
        codigo = int(datos_ingresados["Codigo"])

        if seccion_actual == "clientes":
            indice = obtener_indice_por_codigo(codigos_clientes, codigo)
            nombres_clientes[indice] = datos_ingresados["Nombre"]
            edades_clientes[indice] = int(datos_ingresados["Edad"])
            tipos_clientes[indice] = int(datos_ingresados["Tipo (1=Regular, 2=Frecuente)"])
            mostrar(f"Cliente modificado: {formatear_cliente(indice)}\n")

        elif seccion_actual == "productos":
            indice = obtener_indice_por_codigo(codigos_productos, codigo)
            nombres_productos[indice] = datos_ingresados["Nombre"]
            precios_productos[indice] = float(datos_ingresados["Precio"])
            mostrar(f"Producto modificado: {formatear_producto(indice)}\n")

        else:
            indice = obtener_indice_por_codigo(codigos_ventas, codigo)
            ventas_clientes[indice] = int(datos_ingresados["Cliente"])
            ventas_productos[indice] = int(datos_ingresados["Producto"])
            ventas_cantidades[indice] = int(datos_ingresados["Cantidad"])
            medios_pago[indice] = int(datos_ingresados["Pago (1=Efectivo, 2=Tarjeta, 3=Transferencia)"])
            mostrar(f"Venta modificada: {formatear_venta(indice)}\n")

        finalizar_accion()
    except (KeyError, ValueError):
        mostrar("Error en los datos ingresados\n")


def ejecutar_buscar():
    try:
        codigo = int(datos_ingresados["Codigo"])

        if seccion_actual == "clientes":
            indice = obtener_indice_por_codigo(codigos_clientes, codigo)
            mostrar(f"Cliente: {formatear_cliente(indice)}\n")
        elif seccion_actual == "productos":
            indice = obtener_indice_por_codigo(codigos_productos, codigo)
            mostrar(f"Producto: {formatear_producto(indice)}\n")
        else:
            indice = obtener_indice_por_codigo(codigos_ventas, codigo)
            mostrar(f"Venta: {formatear_venta(indice)}\n")

        finalizar_accion()
    except (KeyError, ValueError):
        mostrar("Debe ingresar un numero\n")


def ejecutar_eliminar():
    try:
        codigo = int(datos_ingresados["Codigo"])

        if seccion_actual == "clientes":
            indice = obtener_indice_por_codigo(codigos_clientes, codigo)
            nombre = nombres_clientes[indice]
            eliminar_en_listas_paralelas(
                [codigos_clientes, nombres_clientes, edades_clientes, tipos_clientes],
                indice,
            )
            mostrar(f"Cliente eliminado: {codigo} | {nombre}\n")

        elif seccion_actual == "productos":
            indice = obtener_indice_por_codigo(codigos_productos, codigo)
            nombre = nombres_productos[indice]
            eliminar_en_listas_paralelas(
                [codigos_productos, nombres_productos, precios_productos],
                indice,
            )
            mostrar(f"Producto eliminado: {codigo} | {nombre}\n")

        else:
            indice = obtener_indice_por_codigo(codigos_ventas, codigo)
            eliminar_en_listas_paralelas(
                [codigos_ventas, ventas_clientes, ventas_productos, ventas_cantidades, medios_pago],
                indice,
            )
            mostrar(f"Venta eliminada: {codigo}\n")

        finalizar_accion()
    except (KeyError, ValueError):
        mostrar("Debe ingresar un numero\n")


def volver():
    global seccion_actual, accion_actual, paso_actual, datos_ingresados

    seccion_actual = None
    accion_actual = None
    paso_actual = 0
    datos_ingresados = {}
    limpiar_submenu()
    prompt_label.config(text="")
    entrada_datos.delete(0, tk.END)
    mostrar("Volvio al menu principal\n")


entrada_datos.bind("<Return>", lambda e: procesar_input())

if __name__ == "__main__":
    root.mainloop()
