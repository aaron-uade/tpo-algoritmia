import tkinter as tk
from constantes.constantes import (
    usuarios, claves, codigos_clientes, nombres_clientes, edades_clientes,
    tipos_clientes, codigos_productos, nombres_productos, precios_productos,
    codigos_ventas, ventas_clientes, ventas_productos, ventas_cantidades, medios_pago
)
from utils.utilidades import obtener_indice_por_codigo

root = tk.Tk()
root.title("Sistema de Gestión")
root.geometry("700x500")

# Diccionario para traducir medios de pago
medios_pago_nombres = {
    1: "Efectivo",
    2: "Tarjeta",
    3: "Transferencia"
}

# Variables globales
logueado = False
seccion_actual = None
accion_actual = None
paso_actual = 0
datos_ingresados = {}

# Configuración de campos por sección y acción
campos = {
    "clientes_agregar": ["Código", "Nombre", "Edad", "Tipo (1=Regular, 2=Frecuente)"],
    "clientes_modificar": ["Código", "Nombre", "Edad", "Tipo (1=Regular, 2=Frecuente)"],
    "clientes_buscar": ["Código"],
    "productos_agregar": ["Código", "Nombre", "Precio"],
    "productos_modificar": ["Código", "Nombre", "Precio"],
    "productos_buscar": ["Código"],
    "ventas_agregar": ["Código", "Cliente", "Producto", "Cantidad", "Pago (1=Efectivo, 2=Tarjeta, 3=Transferencia)"],
    "ventas_modificar": ["Código", "Cliente", "Producto", "Cantidad", "Pago (1=Efectivo, 2=Tarjeta, 3=Transferencia)"],
    "ventas_buscar": ["Código"],
}

# LOGIN
login_window = tk.Frame(root)
login_window.pack()

tk.Label(login_window, text="INICIAR SESION", font=("Arial", 14)).pack(pady=10)

tk.Label(login_window, text="Usuario").pack()
user_entry = tk.Entry(login_window)
user_entry.pack()

tk.Label(login_window, text="Contraseña").pack()
pass_entry = tk.Entry(login_window, show="*")
pass_entry.pack()

error_msg = tk.Label(login_window, text="", fg="red")
error_msg.pack()

def hacer_login():
    global logueado
    user = user_entry.get()
    pas = pass_entry.get()
    
    if user == usuarios[0] and pas == claves[0]:
        logueado = True
        login_window.pack_forget()
        main_window.pack()
        error_msg.config(text="")
    else:
        error_msg.config(text="Usuario o contraseña incorrectos")

tk.Button(login_window, text="Entrar", command=hacer_login).pack(pady=10)

# MENU PRINCIPAL
main_window = tk.Frame(root)

tk.Label(main_window, text="MENU PRINCIPAL", font=("Arial", 12)).pack(pady=5)

menu_buttons = tk.Frame(main_window)
menu_buttons.pack()

def ir_clientes():
    global seccion_actual, accion_actual, paso_actual, datos_ingresados
    seccion_actual = "clientes"
    accion_actual = None
    paso_actual = 0
    datos_ingresados = {}
    limpiar_submenu()
    llenar_submenu()
    mostrar("Selecciona qué deseas hacer con Clientes\n")

def ir_productos():
    global seccion_actual, accion_actual, paso_actual, datos_ingresados
    seccion_actual = "productos"
    accion_actual = None
    paso_actual = 0
    datos_ingresados = {}
    limpiar_submenu()
    llenar_submenu()
    mostrar("Selecciona qué deseas hacer con Productos\n")

def ir_ventas():
    global seccion_actual, accion_actual, paso_actual, datos_ingresados
    seccion_actual = "ventas"
    accion_actual = None
    paso_actual = 0
    datos_ingresados = {}
    limpiar_submenu()
    llenar_submenu()
    mostrar("Selecciona qué deseas hacer con Ventas\n")

def salir():
    root.destroy()

tk.Button(menu_buttons, text="Clientes", command=ir_clientes, width=12).pack(side="left", padx=5)
tk.Button(menu_buttons, text="Productos", command=ir_productos, width=12).pack(side="left", padx=5)
tk.Button(menu_buttons, text="Ventas", command=ir_ventas, width=12).pack(side="left", padx=5)
tk.Button(menu_buttons, text="Salir", command=salir, width=12).pack(side="left", padx=5)

submenu_frame = tk.Frame(main_window)
submenu_frame.pack(pady=5)

resultado_text = tk.Text(main_window, height=15, width=90)
resultado_text.pack(padx=5, pady=5)
resultado_text.config(state="disabled")

prompt_label = tk.Label(main_window, text="", font=("Arial", 10))
prompt_label.pack()

entrada_datos = tk.Entry(main_window, width=60)
entrada_datos.pack(pady=5)

def limpiar_submenu():
    for widget in submenu_frame.winfo_children():
        widget.destroy()

def llenar_submenu():
    tk.Button(submenu_frame, text="Listar", command=listar, width=12).pack(side="left", padx=3)
    tk.Button(submenu_frame, text="Agregar", command=iniciar_agregar, width=12).pack(side="left", padx=3)
    tk.Button(submenu_frame, text="Modificar", command=iniciar_modificar, width=12).pack(side="left", padx=3)
    tk.Button(submenu_frame, text="Buscar", command=iniciar_buscar, width=12).pack(side="left", padx=3)
    tk.Button(submenu_frame, text="Volver", command=volver, width=12).pack(side="left", padx=3)

def mostrar(texto):
    resultado_text.config(state="normal")
    resultado_text.delete(1.0, tk.END)
    resultado_text.insert(tk.END, texto)
    resultado_text.config(state="disabled")

def actualizar_prompt():
    global accion_actual, paso_actual, seccion_actual
    
    if accion_actual is None:
        return
    
    clave = f"{seccion_actual}_{accion_actual.lower()}"
    lista_campos = campos.get(clave, [])
    
    if paso_actual < len(lista_campos):
        prompt_label.config(text=f"Ingresa {lista_campos[paso_actual]}:")
    
    entrada_datos.delete(0, tk.END)
    entrada_datos.focus()

def procesar_input():
    global accion_actual, paso_actual, seccion_actual, datos_ingresados
    
    if accion_actual is None:
        return
    
    valor = entrada_datos.get().strip()
    
    if not valor:
        mostrar("Por favor ingresa un valor\n")
        return
    
    clave = f"{seccion_actual}_{accion_actual.lower()}"
    lista_campos = campos.get(clave, [])
    
    if paso_actual < len(lista_campos):
        nombre_campo = lista_campos[paso_actual]
        datos_ingresados[nombre_campo] = valor
        
        # VALIDAR CÓDIGO DUPLICADO APENAS SE INGRESA EL CÓDIGO
        if paso_actual == 0 and nombre_campo == "Código" and accion_actual.lower() == "agregar":
            try:
                codigo = int(valor)
                if seccion_actual == "clientes":
                    if obtener_indice_por_codigo(codigos_clientes, codigo) != -1:
                        mostrar(f"Error: Ya existe un cliente con código {codigo}\n")
                        entrada_datos.delete(0, tk.END)
                        entrada_datos.focus()
                        return
                elif seccion_actual == "productos":
                    if obtener_indice_por_codigo(codigos_productos, codigo) != -1:
                        mostrar(f"Error: Ya existe un producto con código {codigo}\n")
                        entrada_datos.delete(0, tk.END)
                        entrada_datos.focus()
                        return
                elif seccion_actual == "ventas":
                    if obtener_indice_por_codigo(codigos_ventas, codigo) != -1:
                        mostrar(f"Error: Ya existe una venta con código {codigo}\n")
                        entrada_datos.delete(0, tk.END)
                        entrada_datos.focus()
                        return
            except ValueError:
                mostrar("El código debe ser un número\n")
                entrada_datos.delete(0, tk.END)
                entrada_datos.focus()
                return
        
        # VALIDAR QUE EL CÓDIGO EXISTA PARA MODIFICAR
        if paso_actual == 0 and nombre_campo == "Código" and accion_actual.lower() == "modificar":
            try:
                codigo = int(valor)
                if seccion_actual == "clientes":
                    if obtener_indice_por_codigo(codigos_clientes, codigo) == -1:
                        mostrar(f"Error: No existe cliente con código {codigo}\n")
                        entrada_datos.delete(0, tk.END)
                        entrada_datos.focus()
                        return
                elif seccion_actual == "productos":
                    if obtener_indice_por_codigo(codigos_productos, codigo) == -1:
                        mostrar(f"Error: No existe producto con código {codigo}\n")
                        entrada_datos.delete(0, tk.END)
                        entrada_datos.focus()
                        return
                elif seccion_actual == "ventas":
                    if obtener_indice_por_codigo(codigos_ventas, codigo) == -1:
                        mostrar(f"Error: No existe venta con código {codigo}\n")
                        entrada_datos.delete(0, tk.END)
                        entrada_datos.focus()
                        return
            except ValueError:
                mostrar("El código debe ser un número\n")
                entrada_datos.delete(0, tk.END)
                entrada_datos.focus()
                return
        
        # VALIDAR QUE EL CÓDIGO EXISTA PARA BUSCAR
        if paso_actual == 0 and nombre_campo == "Código" and accion_actual.lower() == "buscar":
            try:
                codigo = int(valor)
                if seccion_actual == "clientes":
                    if obtener_indice_por_codigo(codigos_clientes, codigo) == -1:
                        mostrar(f"No se encontró cliente con código {codigo}\n")
                        entrada_datos.delete(0, tk.END)
                        entrada_datos.focus()
                        return
                elif seccion_actual == "productos":
                    if obtener_indice_por_codigo(codigos_productos, codigo) == -1:
                        mostrar(f"No se encontró producto con código {codigo}\n")
                        entrada_datos.delete(0, tk.END)
                        entrada_datos.focus()
                        return
                elif seccion_actual == "ventas":
                    if obtener_indice_por_codigo(codigos_ventas, codigo) == -1:
                        mostrar(f"No se encontró venta con código {codigo}\n")
                        entrada_datos.delete(0, tk.END)
                        entrada_datos.focus()
                        return
            except ValueError:
                mostrar("El código debe ser un número\n")
                entrada_datos.delete(0, tk.END)
                entrada_datos.focus()
                return
        
        # VALIDAR QUE EL CLIENTE EXISTA EN VENTAS
        if seccion_actual == "ventas" and nombre_campo == "Cliente" and accion_actual.lower() in ["agregar", "modificar"]:
            try:
                cliente_id = int(valor)
                if obtener_indice_por_codigo(codigos_clientes, cliente_id) == -1:
                    mostrar(f"Error: No existe cliente con código {cliente_id}\n")
                    entrada_datos.delete(0, tk.END)
                    entrada_datos.focus()
                    return
            except ValueError:
                mostrar("El cliente debe ser un número\n")
                entrada_datos.delete(0, tk.END)
                entrada_datos.focus()
                return
        
        # VALIDAR QUE EL PRODUCTO EXISTA EN VENTAS
        if seccion_actual == "ventas" and nombre_campo == "Producto" and accion_actual.lower() in ["agregar", "modificar"]:
            try:
                producto_id = int(valor)
                if obtener_indice_por_codigo(codigos_productos, producto_id) == -1:
                    mostrar(f"Error: No existe producto con código {producto_id}\n")
                    entrada_datos.delete(0, tk.END)
                    entrada_datos.focus()
                    return
            except ValueError:
                mostrar("El producto debe ser un número\n")
                entrada_datos.delete(0, tk.END)
                entrada_datos.focus()
                return
        
        # VALIDAR QUE LA CANTIDAD SEA POSITIVA EN VENTAS
        if seccion_actual == "ventas" and nombre_campo == "Cantidad" and accion_actual.lower() in ["agregar", "modificar"]:
            try:
                cantidad = int(valor)
                if cantidad <= 0:
                    mostrar("Error: La cantidad debe ser un número positivo\n")
                    entrada_datos.delete(0, tk.END)
                    entrada_datos.focus()
                    return
            except ValueError:
                mostrar("La cantidad debe ser un número\n")
                entrada_datos.delete(0, tk.END)
                entrada_datos.focus()
                return
        
        paso_actual += 1
        
        if paso_actual >= len(lista_campos):
            # Todos los datos ingresados
            if accion_actual == "Agregar":
                ejecutar_agregar()
            elif accion_actual == "Modificar":
                ejecutar_modificar()
            elif accion_actual == "Buscar":
                ejecutar_buscar()
        else:
            # Pedir siguiente dato
            actualizar_prompt()

def listar():
    if seccion_actual == "clientes":
        texto = "CLIENTES\n"
        for i in range(len(codigos_clientes)):
            tipo = "Regular" if tipos_clientes[i] == 1 else "Frecuente"
            texto += f"Cod: {codigos_clientes[i]} | {nombres_clientes[i]} | Edad: {edades_clientes[i]} | {tipo}\n"
        mostrar(texto)
    elif seccion_actual == "productos":
        texto = "PRODUCTOS\n"
        for i in range(len(codigos_productos)):
            texto += f"Cod: {codigos_productos[i]} | {nombres_productos[i]} | Precio: {precios_productos[i]}\n"
        mostrar(texto)
    else:
        texto = "VENTAS\n"
        for i in range(len(codigos_ventas)):
            pago_nombre = medios_pago_nombres.get(medios_pago[i], str(medios_pago[i]))
            texto += f"Venta {codigos_ventas[i]} | Cliente: {ventas_clientes[i]} | Producto: {ventas_productos[i]} | Cantidad: {ventas_cantidades[i]} | Pago: {pago_nombre}\n"
        mostrar(texto)

def iniciar_agregar():
    global accion_actual, paso_actual, datos_ingresados
    accion_actual = "Agregar"
    paso_actual = 0
    datos_ingresados = {}
    actualizar_prompt()

def ejecutar_agregar():
    global datos_ingresados, accion_actual, paso_actual
    
    try:
        if seccion_actual == "clientes":
            codigo = int(datos_ingresados.get("Código", ""))
            nombre = datos_ingresados.get("Nombre", "")
            edad = int(datos_ingresados.get("Edad", ""))
            tipo = int(datos_ingresados.get("Tipo (1=Regular, 2=Frecuente)", ""))
            
            codigos_clientes.append(codigo)
            nombres_clientes.append(nombre)
            edades_clientes.append(edad)
            tipos_clientes.append(tipo)
            mostrar(f"Cliente agregado: {codigo} | {nombre} | {edad} | {tipo}\n")
        
        elif seccion_actual == "productos":
            codigo = int(datos_ingresados.get("Código", ""))
            nombre = datos_ingresados.get("Nombre", "")
            precio = float(datos_ingresados.get("Precio", ""))
            
            codigos_productos.append(codigo)
            nombres_productos.append(nombre)
            precios_productos.append(precio)
            mostrar(f"Producto agregado: {codigo} | {nombre} | {precio}\n")
        
        else:
            codigo = int(datos_ingresados.get("Código", ""))
            cliente = int(datos_ingresados.get("Cliente", ""))
            producto = int(datos_ingresados.get("Producto", ""))
            cantidad = int(datos_ingresados.get("Cantidad", ""))
            pago = int(datos_ingresados.get("Pago (1=Efectivo, 2=Tarjeta, 3=Transferencia)", ""))
            
            codigos_ventas.append(codigo)
            ventas_clientes.append(cliente)
            ventas_productos.append(producto)
            ventas_cantidades.append(cantidad)
            medios_pago.append(pago)
            mostrar(f"Venta agregada: {codigo} | {cliente} | {producto} | {cantidad} | {pago}\n")
        
        accion_actual = None
        paso_actual = 0
        prompt_label.config(text="")
    except:
        mostrar("Error en los datos ingresados\n")

def iniciar_modificar():
    global accion_actual, paso_actual, datos_ingresados
    accion_actual = "Modificar"
    paso_actual = 0
    datos_ingresados = {}
    actualizar_prompt()

def ejecutar_modificar():
    global datos_ingresados, accion_actual, paso_actual
    
    try:
        if seccion_actual == "clientes":
            codigo = int(datos_ingresados.get("Código", ""))
            nombre = datos_ingresados.get("Nombre", "")
            edad = int(datos_ingresados.get("Edad", ""))
            tipo = int(datos_ingresados.get("Tipo (1=Regular, 2=Frecuente)", ""))
            
            idx = obtener_indice_por_codigo(codigos_clientes, codigo)
            if idx == -1:
                mostrar(f"No existe cliente con codigo {codigo}\n")
                return
            
            nombres_clientes[idx] = nombre
            edades_clientes[idx] = edad
            tipos_clientes[idx] = tipo
            mostrar(f"Cliente modificado: {codigo} | {nombre} | {edad} | {tipo}\n")
        
        elif seccion_actual == "productos":
            codigo = int(datos_ingresados.get("Código", ""))
            nombre = datos_ingresados.get("Nombre", "")
            precio = float(datos_ingresados.get("Precio", ""))
            
            idx = obtener_indice_por_codigo(codigos_productos, codigo)
            if idx == -1:
                mostrar(f"No existe producto con codigo {codigo}\n")
                return
            
            nombres_productos[idx] = nombre
            precios_productos[idx] = precio
            mostrar(f"Producto modificado: {codigo} | {nombre} | {precio}\n")
        
        else:
            codigo = int(datos_ingresados.get("Código", ""))
            cliente = int(datos_ingresados.get("Cliente", ""))
            producto = int(datos_ingresados.get("Producto", ""))
            cantidad = int(datos_ingresados.get("Cantidad", ""))
            pago = int(datos_ingresados.get("Pago (1=Efectivo, 2=Tarjeta, 3=Transferencia)", ""))
            
            idx = obtener_indice_por_codigo(codigos_ventas, codigo)
            if idx == -1:
                mostrar(f"No existe venta con codigo {codigo}\n")
                return
            
            ventas_clientes[idx] = cliente
            ventas_productos[idx] = producto
            ventas_cantidades[idx] = cantidad
            medios_pago[idx] = pago
            mostrar(f"Venta modificada: {codigo} | {cliente} | {producto} | {cantidad} | {pago}\n")
        
        accion_actual = None
        paso_actual = 0
        prompt_label.config(text="")
    except:
        mostrar("Error en los datos ingresados\n")

def iniciar_buscar():
    global accion_actual, paso_actual, datos_ingresados
    accion_actual = "Buscar"
    paso_actual = 0
    datos_ingresados = {}
    actualizar_prompt()

def ejecutar_buscar():
    global datos_ingresados, accion_actual, paso_actual
    
    try:
        codigo = int(datos_ingresados.get("Código", ""))
        
        if seccion_actual == "clientes":
            idx = obtener_indice_por_codigo(codigos_clientes, codigo)
            if idx == -1:
                mostrar(f"No encontrado cliente {codigo}\n")
            else:
                mostrar(f"Cliente: {codigos_clientes[idx]} | {nombres_clientes[idx]} | {edades_clientes[idx]} | {tipos_clientes[idx]}\n")
        
        elif seccion_actual == "productos":
            idx = obtener_indice_por_codigo(codigos_productos, codigo)
            if idx == -1:
                mostrar(f"No encontrado producto {codigo}\n")
            else:
                mostrar(f"Producto: {codigos_productos[idx]} | {nombres_productos[idx]} | {precios_productos[idx]}\n")
        
        else:
            idx = obtener_indice_por_codigo(codigos_ventas, codigo)
            if idx == -1:
                mostrar(f"No encontrada venta {codigo}\n")
            else:
                pago_nombre = medios_pago_nombres.get(medios_pago[idx], str(medios_pago[idx]))
                mostrar(f"Venta: {codigos_ventas[idx]} | {ventas_clientes[idx]} | {ventas_productos[idx]} | {ventas_cantidades[idx]} | {pago_nombre}\n")
        
        accion_actual = None
        paso_actual = 0
        prompt_label.config(text="")
    except:
        mostrar("Debe ingresar un numero\n")

def volver():
    global seccion_actual, accion_actual, paso_actual
    seccion_actual = None
    accion_actual = None
    paso_actual = 0
    limpiar_submenu()
    prompt_label.config(text="")
    mostrar("Volvio al menu principal\n")

# Vincular Enter a procesar_input
entrada_datos.bind("<Return>", lambda e: procesar_input())

if __name__ == "__main__":
    root.mainloop()