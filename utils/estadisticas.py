from utils.utilidades import obtener_indice_por_codigo

#Calcular el total de la venta.

"Esta funcion recibe el indice de la venta dentro de las listas paralelas, si el producto no existe, devuelve 0."
def calcular_total_venta(indice_venta, ventas_productos, codigos_productos,ventas_cantidades, precios_productos):
    
    indice_producto = obtener_indice_por_codigo(codigos_productos, ventas_productos[indice_venta])
    
    if indice_producto == -1: 
        return 0.0
    return ventas_cantidades[indice_venta] * precios_productos[indice_producto]

#La MATRIZ 

def listas_a_matriz_ventas(codigos_ventas, medios_pago, ventas_productos, codigos_productos, ventas_cantidades, precios_productos):
    matriz = []
    i = 0
    while i < len(codigos_ventas):
        total = calcular_total_venta(i, ventas_productos, codigos_productos, ventas_cantidades, precios_productos)

        fila = [codigos_ventas[i], medios_pago[i], total]
        matriz.append(fila)
        i += 1
    return matriz

# Medios de pago 

def conservar_unicos_medios(matriz):
    unicos = []
    i = 0
    while i < len(matriz):
        medio = matriz[i][1]
        if obtener_indice_por_codigo(unicos, medio) == -1:
            unicos.append(medio)
        i += 1
    return unicos

#Acumular por medio de pago

def obtener_total_medio(matriz, medio):
    suma = 0 
    i = 0 
    while i < len(matriz):
        if matriz[i][1] == medio:
            suma += matriz[i][2]
        i += 1
    return suma

def obtener_cantidad_medio(matriz, medio):
    cantidad = 0 
    i = 0 
    while i < len(matriz):
        if matriz[i][1] == medio:
            cantidad += 1
        i += 1
    return cantidad

#Calcular el total de la vta.
def calcular_total_venta(indice_venta, ventas_productos, codigos_productos, ventas_cantidades, precios_productos):
    indice_producto = obtener_indice_por_codigo(codigos_productos, ventas_productos[indice_venta])

    if indice_producto == -1:
        return 0.0
    return ventas_cantidades[indice_venta] * precios_productos[indice_producto]


#La MATRIZ
def listas_a_matriz_ventas(codigos_ventas, medios_pago, ventas_productos, codigos_productos, ventas_cantidades, precios_productos):
    matriz = []
    i = 0
    while i < len(codigos_ventas):
        total = calcular_total_venta(i, ventas_productos, codigos_productos, ventas_cantidades, precios_productos)
        fila = [codigos_ventas[i], medios_pago[i], total]
        matriz.append(fila)
        i += 1
    return matriz


#Matriz Estadisticas.
def traducir_medio(medio):
    if medio == 1:
        return "Efectivo"
    elif medio == 2:
        return "Tarjeta"
    else:
        return "Transferencia"


def armar_matriz_estadisticas(matriz):
    medios_unicos = conservar_unicos_medios(matriz)
    matriz_estad = []
    i = 0
    while i < len(medios_unicos):
        medio = medios_unicos[i]
        total = obtener_total_medio(matriz, medio)
        cantidad = obtener_cantidad_medio(matriz, medio)
        fila = [traducir_medio(medio), cantidad, total]
        matriz_estad.append(fila)
        i += 1
    return matriz_estad

#Imprimir matriz
"definitivamente es para imprimir la matriz"

def imprimir_matriz_estadisticas(matriz_estado):

    print(f"{'Medio de pago':<16}{'Cantidad':>10}{'Total':>12}")
    i = 0
    while i < len(matriz_estado):
        nombre, cantidad, total = matriz_estado[i]
        print(f"{nombre:<16}{cantidad:>10}{total:>12.2f}")
        i += 1
