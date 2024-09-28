from constructor import *
from pilotos import *
from circuito import *
from carrera import *
from restaurante import *
import matplotlib.pyplot as plt
import random



###Funciones para gestion de carreras###

###Funcion para busqueda utilizando busqueda binaria para agilizar la busqueda###
def buscar_constructores_por_pais(constructores, pais):
    # asegurarse de que la lista de constructores esté ordenada por país
    constructores_ordenados = sorted(constructores, key=lambda x: x.nacionalidad)

    # definir los límites del rango de búsqueda
    izquierda = 0
    derecha = len(constructores_ordenados) - 1

    # mientras el rango de búsqueda no se haya reducido a un solo elemento
    while izquierda <= derecha:
        # definir el índice central del rango de búsqueda
        medio = (izquierda + derecha) // 2

        # si se encontró el país buscado, construir la cadena con la información de los constructores que coinciden
        if constructores_ordenados[medio].nacionalidad == pais:
            resultado = ""
            # agregar la información de los constructores en el rango izquierdo que coinciden
            i = medio
            while i >= 0 and constructores_ordenados[i].nacionalidad == pais:
                resultado += str(constructores_ordenados[i]) + "\n"
                i -= 1
            # agregar la información de los constructores en el rango derecho que coinciden
            i = medio + 1
            while i < len(constructores_ordenados) and constructores_ordenados[i].nacionalidad == pais:
                resultado += str(constructores_ordenados[i]) + "\n"
                i += 1
            return resultado.strip()

        # si el país buscado está a la izquierda del índice central, reducir el rango de búsqueda a la izquierda
        elif constructores_ordenados[medio].nacionalidad > pais:
            derecha = medio - 1

        # si el país buscado está a la derecha del índice central, reducir el rango de búsqueda a la derecha
        else:
            izquierda = medio + 1

    # si no se encontraron constructores que coincidan, devolver un mensaje de error como string
    return "Constructor no encontrado, intentelo de nuevo"

def buscar_pilotos_por_constructor(listapilotos, constructor_id):
    pilotos_encontrados = []
    for piloto in listapilotos:
        if piloto.equipo == constructor_id:
            pilotos_encontrados.append(piloto)
    return pilotos_encontrados

def buscar_carreras_por_pais_circuito(races, circuito):
    # Se ordena la lista de carreras según el país del circuito en el que se realizó.
    races_sorted = sorted(races, key=lambda x: x.pais)
    # Se inicializan las variables left y right para utilizar el algoritmo de búsqueda binaria.
    left = 0
    right = len(races_sorted) - 1
    while left <= right:
        mid = (left + right) // 2
        if races_sorted[mid].pais == circuito.pais:
            return [races_sorted[mid]]
        elif races_sorted[mid].pais < circuito.pais:
            left = mid + 1
        else:
            right = mid - 1
    # Si no se encontró ninguna carrera en el país especificado, se devuelve una lista vacía.
    return []


def busqueda_por_mes(listacarreras, mes):
    # Diccionario que relaciona los nombres de los meses con sus números correspondientes
    meses = {
        "enero": "01",
        "febrero": "02",
        "marzo": "03",
        "abril": "04",
        "mayo": "05",
        "junio": "06",
        "julio": "07",
        "agosto": "08",
        "septiembre": "09",
        "octubre": "10",
        "noviembre": "11",
        "diciembre": "12",
        "01": "01",
        "02": "02",
        "03": "03",
        "04": "04",
        "05": "05",
        "06": "06",
        "07": "07",
        "08": "08",
        "09": "09",
        "10": "10",
        "11": "11",
        "12": "12"
    }
    
    # Comprobamos si el mes ingresado por el usuario es un nombre de mes válido
    if mes.lower() in meses:
        # Si es un nombre de mes válido, obtenemos su número correspondiente del diccionario `meses`
        mes_num = meses[mes.lower()]
    # Si el mes ingresado por el usuario no es un nombre de mes válido, comprobamos si es un número de mes válido
    elif mes.isdigit() and 1 <= int(mes) <= 12:
        # Si es un número de mes válido, obtenemos su número correspondiente del diccionario `meses`
        mes_num = meses[mes]
    # Si el mes ingresado por el usuario no es ni un nombre de mes válido ni un número de mes válido, imprimimos un mensaje de error y devolvemos una lista vacía.
    else:
        print("Mes no válido. Por favor ingrese un número del 1 al 12 o el nombre de un mes válido en minúsculas.")
        return []
    
    # Creamos una lista vacía para almacenar las carreras encontradas
    carreras_encontradas = []
    # Iteramos sobre cada carrera en la lista de carreras
    for carrera in listacarreras:
        # Si el mes de la carrera coincide con el número de mes buscado, agregamos la carrera a la lista de carreras encontradas
        if mes_num == carrera.fecha.split("-")[1]:
            carreras_encontradas.append(carrera)
    
    # Imprimimos cada carrera encontrada
    for carrera in carreras_encontradas:
        print(carrera)
    
    # Devolvemos la lista de carreras encontradas
    return carreras_encontradas
# Funcion para calcular puntajes de los constructores
def calcular_puntajes_constructores(carreras, equipos):
    # Se crea un diccionario para guardar los puntos de cada equipo
    puntajes = {}
    for equipo in equipos:
        puntajes[equipo.nombre] = 0
    
    # Se recorren todas las carreras y se suman los puntos de cada equipo en cada carrera
    for carrera in carreras:
        for piloto in carrera.resultado:
            equipo_piloto = piloto.equipo
            puntajes[equipo_piloto] += piloto.puntaje
    
    # Se ordenan los puntajes de los equipos de mayor a menor
    puntajes_ordenados = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
    
    # Se muestra el puntaje de cada equipo y se devuelve el diccionario de puntajes
    print("Puntajes de los constructores:")
    for nombre_equipo, puntaje_equipo in puntajes_ordenados:
        print(f"{nombre_equipo}: {puntaje_equipo} puntos")
    return puntajes

#Funcion para finalizar carrera
def finalizar_carrera(carrera, pilotos):
    # Se pide al usuario que ingrese los números de los pilotos en orden de llegada
    print(f"Finalizando carrera: {carrera.nombre} ({carrera.fecha})")
    print("Seleccione el número de los pilotos en el orden de llegada (separados por comas):")
    for i, piloto in enumerate(pilotos):
        print(f"{i+1}. {piloto.nombre}")
    numeros_pilotos = input().split(",")
    
    # Se crea una lista vacía para guardar los pilotos que llegaron
    pilotos_llegada = []
    
    # Se busca cada piloto en la lista de pilotos y se agrega a la lista de llegada
    for numero in numeros_pilotos:
        try:
            index_piloto = int(numero) - 1
            piloto = pilotos[index_piloto]
            pilotos_llegada.append(piloto)
        except ValueError:
            print(f"El valor '{numero}' no es un número válido.")
        except IndexError:
            print(f"No existe un piloto con número '{numero}'")
    
    # Se asigna el puntaje correspondiente a cada piloto en base al orden de llegada
    puntajes = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
    for i, piloto in enumerate(pilotos_llegada):
        try:
            puntaje = puntajes[i]
            piloto.puntaje += puntaje
        except IndexError:
            print(f"El piloto {piloto.nombre} no recibió puntaje.")
    
    # Se muestra el orden de llegada y los puntajes asignados
    print("Orden de llegada y puntajes:")
    for i, piloto in enumerate(pilotos_llegada):
        print(f"{i+1}. {piloto.nombre}: {puntajes[i]} puntos")
    
    return pilotos_llegada

### FUNCIONES PARA LA GESTION DE VENTAS ###
def calcular_total(tickets):
            total = 0
            for ticket in tickets:
                total += ticket.obtener_precio_entrada()
            return total

def es_numero_ondulado(cedula):
    cedula_str = str(cedula)
    if len(cedula_str) < 3:
        return False
    for i in range(1, len(cedula_str)-1):
        if not (int(cedula_str[i-1]) < int(cedula_str[i]) > int(cedula_str[i+1]) or int(cedula_str[i-1]) > int(cedula_str[i]) < int(cedula_str[i+1])):
            return False
    return True
def generar_codigo_boleto(codigos_boletos_existentes):
    while True:
        # Generar un número aleatorio de 5 dígitos
        codigo = str(random.randint(10000, 99999))
        # Verificar si el código ya está en uso
        if codigo not in codigos_boletos_existentes:
            return codigo

def validate(codigo, valid_codes):
    if codigo in valid_codes:
        return True
    else:
        return False
        

def check_ticket(ticket, valid_codes):
    if validate(ticket,valid_codes):
        print("Ticket valido\n\n")
    else:
        print("Ticket invalido\n\n")

def busqueda_por_nombre(data, name):
    resultado = []
    for carrera in data:
        restaurantes = carrera.get('restaurants', [])
        for restaurante in restaurantes:
            items = restaurante.get('items', [])
            for item in items:
                item_name = item.get('name')
                if item_name == name:
                    resultado.append(item)
    return resultado


def busqueda_por_rango(data, min_price, max_price):
    resultados = []
    for carrera in data:
        restaurantes = carrera.get('restaurants', [])
        for restaurante in restaurantes:
            items = restaurante.get('items', [])
            for item in items:
                item_price = float(item.get('price', 0)) * 1.16 # adding 16% IVA
                if min_price <= item_price <= max_price:
                    resultados.append(item)
                    resultado_str = 'Resultados:\n'
    for resultado in resultados:
        resultado_str += f'Name: {resultado["name"]}\nPrice: {resultado["price"]}\n\n'
    return resultado_str


def buscar_por_tipos(data, tipo):
    resultados = []
    for carrera in data:
        restaurantes = carrera.get('restaurants', [])
        for restaurante in restaurantes:
            items = restaurante.get('items', [])
            for item in items:
                item_type = item.get('type')
                if item_type == tipo:
                    resultados.append(item)
    resultado_str = 'Resultados:\n'
    for resultado in resultados:
        resultado_str += f'Name: {resultado["name"]}\nPrice: {resultado["price"]}\n\n'
    return resultado_str


def venta_producto(lista_clientes, cedula, edad, producto_a_comprar):
    # Check if customer has a VIP ticket
    vip_customers = lista_clientes.get('vip', [])
    if cedula not in vip_customers:
        return 'Customer does not have a VIP ticket'
    
    # Check if all items are available for purchase
    inventory = lista_clientes.get('inventory', {})
    for item in producto_a_comprar:
        if item not in inventory:
            return f'Item {item} is not available for purchase'
        if inventory[item] == 0:
            return f'Item {item} is out of stock'
        if edad < 18 and item == 'drink:alcoholic':
            return 'Customer is not allowed to purchase alcoholic beverages'
    
    # Calculate total cost
    total_cost = 0
    for item in producto_a_comprar:
        total_cost += inventory[item]['price']
    
    # Apply discount if applicable
    if is_perfect_number(cedula):
        total_cost *= 0.85
    
    # Update inventory
    for item in producto_a_comprar:
        inventory[item] -= 1
    
    # Return success message with cost breakdown
    subtotal = total_cost / 1.16
    tax = total_cost - subtotal
    discount = subtotal * 0.15 if is_perfect_number(cedula) else 0
    result_str = f'Successful purchase!\nSubtotal: ${subtotal:.2f}\nDiscount: ${discount:.2f}\nTax: ${tax:.2f}\nTotal: ${total_cost:.2f}'
    return result_str
    
def is_perfect_number(n):
   sum_of_divisors = sum([i for i in range(1,n) if n%i==0])
   return sum_of_divisors == n

def validar_cedula(cedula):
    """
    Valida si la cédula tiene un formato válido.
    """
    if len(cedula) != 11 or not cedula.isdigit():
        return False
    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    suma = sum([int(digito)*coeficientes[i] for i, digito in enumerate(cedula)])
    if suma % 10 == 0:
        return True
    else:
        return False

def calcular_descuento(cedula):
    """
    Si la cédula es un número perfecto, se aplica un descuento del 15%.
    """
    if int(cedula) in [6, 28, 496, 8128, 33550336]:
        return 0.15
    else:
        return 0

def restar_inventario(productos, cantidades, seleccionados):
    """
    Resta las cantidades de los productos seleccionados del inventario.
    """
    for producto, cantidad in zip(seleccionados, cantidades):
        productos[producto] -= cantidad

def mostrar_menu(restaurante):
    """
    Muestra el menú del restaurante.
    """
    print(f"Menú del restaurante {restaurante['name']}:")
    for i, item in enumerate(restaurante["items"]):
        print(f"{i+1}. {item['name']} (${item['price']})")

def realizar_compra(restaurante, seleccionados, cedula):
    """
    Realiza la compra y muestra el resumen de la misma.
    """
    productos = {item["name"]: float(item["price"]) for item in restaurante["items"]}
    cantidades = seleccionados.values()
    subtotal = sum([productos[item]*cantidad for item, cantidad in seleccionados.items()])
    descuento = calcular_descuento(cedula)
    total_descuento = subtotal * descuento
    total = subtotal - total_descuento
    print(f"\nResumen de la compra:\nSubtotal: ${subtotal}\nDescuento: ${total_descuento}\nTotal: ${total}")
    restar_inventario(productos, cantidades, seleccionados.keys())

def buscar_restaurante_por_nombre(lista_restaurantes, nombre):
    """
    Busca un restaurante por su nombre en la lista de restaurantes.
    """
    for restaurante in lista_restaurantes:
        if restaurante["name"] == nombre:
            return restaurante
    print(f"No se encontró ningún restaurante con el nombre '{nombre}'")
    return None

def buscar_productos_por_tipo(restaurante, tipo):
    """
    Busca los productos de un tipo específico en el menú del restaurante.
    """
    seleccionados = []
    for item in restaurante["items"]:
        if item["type"].startswith(tipo):
            seleccionados.append(item["name"])
    if len(seleccionados) == 0:
        print(f"No se encontraron productos de tipo '{tipo}' en el restaurante '{restaurante['name']}'")
    else:
        print(f"Productos de tipo '{tipo}' en el restaurante '{restaurante['name']}':")
        print(", ".join(seleccionados))

def buscar_productos_por_rango(restaurante, rango):
    productos_en_rango = []
    # Recorremos la lista de productos del restaurante
    for producto in restaurante["menu"]:
    # Verificamos si el precio del producto está dentro del rango especificado
        if producto["precio"] >= rango[0] and producto["precio"] <= rango[1]:
        # Si el producto cumple con el rango de precios, lo agregamos a la lista de productos_en_rango
            productos_en_rango.append(producto)

# Retornamos la lista de productos que están dentro del rango de precios
            return productos_en_rango
        
def es_numero_perfecto(num):
    """
    Determina si un número es perfecto o no.
    Un número perfecto es aquel que es igual a la suma de sus divisores propios (excluyendo al propio número).
    """
    # Inicializamos la suma de los divisores propios a cero
    suma_divisores = 0
    
    # Iteramos sobre todos los posibles divisores propios del número
    for divisor in range(1, num):
        if num % divisor == 0:
            suma_divisores += divisor
    
    # Si la suma de los divisores propios es igual al número, entonces es perfecto
    return suma_divisores == num

def restar_en_inventario(producto, cantidad, inventario):
    if producto in inventario and inventario[producto] >= cantidad:
        inventario[producto] -= cantidad
        return True
    else:
        return False
    
def es_menor_edad(edad):
    if edad <= 18:
        return "El cliente es menor de edad"
    else:
        return
def guardar_tickets(tickets, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for ticket in tickets:
            archivo.write(f"{ticket.nombre},{ticket.cedula},{ticket.edad},{ticket.carrera_seleccionada},{ticket.tipo_entrada},{ticket.codigo}\n")
def guardar_ventas_entradas(ventas, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for venta in ventas:
            archivo.write(f"{venta['nombre_carrera']},{venta['tipo_entrada']},{venta['cantidad']},{venta['subtotal']},{venta['descuento']},{venta['iva']},{venta['total']}\n")
"""
def leer_tickets(nombre_archivo):
    tickets = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo.readlines():
            nombre, cedula, edad, carrera_seleccionada, tipo_entrada, codigo = linea.strip().split(',')
            ticket = Cliente(nombre, cedula, int(edad), carrera_seleccionada, tipo_entrada, codigo)
            tickets.append(ticket)
    return tickets
"""
def es_cliente_vip(cedula_cliente, tickets):
    for ticket in tickets:
        if ticket.cedula == cedula_cliente and ticket.tipo_entrada.lower() == 'vip':
            return ticket
    return None


def calcular_descuento(cedula, subtotal):
    # Obtén los últimos dos dígitos de la cédula
    ultimos_digitos = int(cedula[-2:])

    # Aplica descuentos según los últimos dos dígitos
    if 1 <= ultimos_digitos <= 30:
        descuento = subtotal * 0.15
    elif 31 <= ultimos_digitos <= 65:
        descuento = subtotal * 0.20
    else:
        descuento = subtotal * 0.25

    return descuento

def es_numero_ondulado(cedula):
    numeros = [int(digito) for digito in str(cedula)]
    suma_pares = sum(numeros[::2])
    suma_impares = sum(numeros[1::2])
    return abs(suma_pares - suma_impares) % 10 == 0

def promedio_gasto_cliente_vip(tickets):
    gastos = [t.obtener_precio_entrada() for t in tickets if t.tipo_entrada == 'Vip']
    return sum(gastos) / len(gastos) if gastos else 0

def promedio_gasto_vip(clientes_vip, tickets, compras_restaurante):
    gasto_total = 0
    num_clientes = len(clientes_vip)

    for cliente in clientes_vip:
        gasto_total += tickets[cliente] + compras_restaurante[cliente]

    promedio = gasto_total / num_clientes
    return promedio

def mostrar_tabla_asistencia(carreras):
    print("Carrera\tEstadio\tBoletos vendidos\tAsistentes\tRelación Asistencia/Venta")
    for carrera in carreras:
        print("{}\t{}\t{}\t{}\t{:.2f}".format(carrera["nombre"], carrera["estadio"], carrera["boletos_vendidos"], carrera["asistentes"], carrera["asistentes"]/carrera["boletos_vendidos"]))

def carrera_mayor_asistencia(carreras):
    max_asistentes = 0
    carrera_nombre = ""

    for carrera in carreras:
        if carrera["asistentes"] > max_asistentes:
            max_asistentes = carrera["asistentes"]
            carrera_nombre = carrera["nombre"]

    return carrera_nombre

def carrera_mayor_boletos_vendidos(carreras):
    max_boletos = 0
    carrera_nombre = ""

    for carrera in carreras:
        if carrera["boletos_vendidos"] > max_boletos:
            max_boletos = carrera["boletos_vendidos"]
            carrera_nombre = carrera["nombre"]

    return carrera_nombre

def top_3_productos_mas_vendidos(ventas_producto):
    top_productos = sorted(ventas_producto.items(), key=lambda x: x[1], reverse=True)[:3]
    return top_productos

def top_3_clientes_boletos(compras_boletos):
    top_clientes = sorted(compras_boletos.items(), key=lambda x: x[1], reverse=True)[:3]
    return top_clientes

def grafico_top_productos(ventas_producto):
    productos, ventas = zip(*ventas_producto)
    plt.bar(productos, ventas)
    plt.xlabel("Productos")
    plt.ylabel("Ventas")
    plt.title("Top 3 productos más vendidos")
    plt.show()

def grafico_top_clientes(compras_boletos):
    clientes, boletos = zip(*compras_boletos)
    plt.bar(clientes, boletos)
    plt.xlabel("Clientes")
    plt.ylabel("Boletos Comprados")
    plt.title("Top 3 clientes que más compraron boletos")
    plt.show()