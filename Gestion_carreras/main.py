import requests
from constructor import *
from circuito import *
from pilotos import *
from restaurante import *
from carrera import *
from funciones import *
from tickets import *
from producto import Producto
from restaurante import *



url_pilotos = "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json"
url_constructores = "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/constructors.json"
url_carreras = "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json"

url1 = requests.get(url_pilotos)
url2 = requests.get(url_constructores)
url3 = requests.get(url_carreras)

pilotos = url1.json()
constructores = url2.json()
carreras = url3.json()

#listas con objetos
lista_pilotos= []
lista_constructores= []
lista_carreras = []
lista_circuitos = []


#bucle iternado por cada uno de los pilotos para tener la informacion requerida
for piloto in pilotos:
    nombre = piloto["firstName"]
    apellido = piloto["lastName"]
    fecha_nacimiento = piloto["dateOfBirth"]
    lugar_nacimiento = piloto["nationality"]
    numero = piloto["permanentNumber"]
    equipo = piloto["team"]
    nuevo_piloto = Piloto(nombre,apellido,fecha_nacimiento,lugar_nacimiento,numero,equipo)
    lista_pilotos.append(nuevo_piloto)
#bucle iternado por cada uno de los constructores para tener la informacion requerida
for constructor in constructores:
    id = constructor["id"]
    nombre = constructor["name"]
    nacionalidad = constructor["nationality"]
    nuevo_constructor = Constructor(id, nombre, nacionalidad)
    lista_constructores.append(nuevo_constructor)

#bucle iternado por cada uno de las carreras para tener la informacion requerida
for carrera in carreras:
    nombre = carrera["name"]
    numero_carrera = carrera['round']
    fecha_carrera = carrera['date']
    circuito = carrera['circuit']['circuitId']
    pais = carrera['circuit']["location"]["country"]
    podium = []

    lista_restaurantes = []
    for restaurante_data in carrera["restaurants"]:
        nombre_restaurante = restaurante_data["name"]
        lista_productos = [Producto(producto["name"], producto["type"], producto["price"]) for producto in restaurante_data["items"]]
        nuevo_restaurante = Restaurante(nombre_restaurante, lista_productos)
        lista_restaurantes.append(nuevo_restaurante)

    nueva_carrera = Carrera(nombre, numero_carrera, fecha_carrera, circuito, podium, pais, lista_restaurantes)
    lista_carreras.append(nueva_carrera)
#bucle iternado por cada uno de los circuitos para tener la informacion requerida
for circuito in carreras:
    nombre = circuito['circuit']['name']
    pais = circuito['circuit']['location']['country']
    localidad = circuito['circuit']['location']['locality']
    latitud = circuito['circuit']['location']['lat']
    longitud = circuito['circuit']['location']['long']
    nuevo_circuito = Circuito(nombre, pais, localidad, latitud, longitud)
    lista_circuitos.append(nuevo_circuito)

tickets = []
codigos_existentes = []

while True:
    opcion = input("===BIENVENIDO AL PROYECTO FORMULA 1===\nQue desea ver?\n1. Gestión de carreras y equipo\n2.Gestión de venta de entradas\n3. Gestión de asistencia a las carreras\n4. Gestión de restaurantes\n5. Gestión de venta de restaurantes\n6. ndicadores de gestión (estadísticas)\n7. Salir del programa\n=> ")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6" and opcion != "7":
        opcion = input("===BIENVENIDO AL PROYECTO FORMULA 1===\n Que desea ver?\n 1. Gestión de carreras y equipo\n2.Gestión de venta de entradas\n3. Gestión de asistencia a las carreras\n4. Gestión de restaurantes\n5. Gestión de venta de restaurantes\n6. ndicadores de gestión (estadísticas)")

    ### GESTION DE CARRERAS Y EQUIPOS ###
    if opcion == "1":
        print("****Gestion de carreras y equipos****")
        opcionA = input("Que desea realizar\n1.Buscar los constructores por país\n2.Buscar los pilotos por constructor\n3.Buscar a las carreras por país del circuito\n4.Buscar todas las carreras que ocurran en un mes.\n5. Finalizar carrera\n=> ")
        while opcionA != "1" and opcionA != "2" and opcionA != "3" and opcionA != "4" and opcionA != "5": #validacion para que escoja la opcion deseada 
            opcionA = input("ERROR. Ingrese una opcion valida\n1.Buscar los constructores por país\n2.Buscar los pilotos por constructor\n3.Buscar a las carreras por país del circuito\n4.Buscar todas las carreras que ocurran en un mes.\n5. Finalizar carrera=> ")
        if opcionA == "1":
            pais_a_buscar = input("===Ingrese el pais a buscar===\n***> ").capitalize()
            busqueda = buscar_constructores_por_pais(lista_constructores,pais_a_buscar)
            print(busqueda)

        elif opcionA == "2":
            for indice, constructor in enumerate(lista_constructores):
                print(f"{indice+1}. {constructor.id}")
            while True:
                piloto_a_buscar = input("===Ingrese el número del constructor al cual desea acceder===\n***> ")
                try:
                    piloto_a_buscar = int(piloto_a_buscar) - 1
                    constructor_id = lista_constructores[piloto_a_buscar].id
                    busqueda = buscar_pilotos_por_constructor(lista_pilotos, constructor_id)
                    for piloto in busqueda:
                        print(piloto)
                    break
                except:
                     print("Error: valor ingresado inválido. Intente nuevamente.")
        elif opcionA == "3":
            for indice, circuito in enumerate(lista_circuitos):
                print(f"{indice+1}. {circuito.nombre}")
                    
            while True:
                circuito_a_buscar = input("===Ingrese el número del circuito para buscar las carreras===\n***> ")
                try:
                    circuito_a_buscar = int(circuito_a_buscar)
                    if 1 <= circuito_a_buscar <= len(lista_circuitos):
                        circuito_seleccionado = lista_circuitos[circuito_a_buscar-1]
                        busqueda = buscar_carreras_por_pais_circuito(lista_carreras, circuito_seleccionado)
                        if len(busqueda) == 0:
                            print("Lo siento, no se encontró ninguna carrera en el país especificado.")
                        else:
                            for carrera in busqueda:
                                print(carrera)
                        break
                    else:
                        print("Error: ingrese un número de circuito válido")
                except ValueError:
                    print("Error: ingrese un número de circuito válido")
        elif opcionA == "4":
            mes = input("===Que mes quiere ver?===\n***>")
            mes_a_buscar = busqueda_por_mes(lista_carreras,mes)
            print(mes_a_buscar)
        elif opcionA == "5":     
            opcionA_1 = input("===Que desea hacer===\n1. Finalizar una carrera\n2. Revisar el final de la temporada")
            if opcionA_1 == "1":
                print("\n### Finalizacion de carrera ###\n")
                for indice,carrera in enumerate(lista_carreras):
                    print(f"{indice+1}. {carrera.nombre}")
                circuito_a_finalizar = input("Ingrese el número del circuito que desea finalizar:\n***>")
                try:
                    circuito_a_finalizar = int(circuito_a_finalizar)
                    if circuito_a_finalizar > 0 and circuito_a_finalizar <= len(lista_carreras):
                        carrera_encontrada = lista_carreras[circuito_a_finalizar - 1]
                        pilotos_llegada = finalizar_carrera(carrera_encontrada, pilotos)
                        print("La carrera ha sido finalizada.")
                        print("Orden de llegada:")
                        for i, piloto in enumerate(pilotos_llegada):
                            print(f"{i+1}. {piloto.nombre}")
                    else:
                        print("Circuito no válido.")
                except ValueError:
                    print("Ingrese un valor numérico para seleccionar el circuito.")

            elif opcionA_1 == "2":
                contructores = calcular_puntajes_constructores(lista_carreras,lista_constructores)
                print(constructores)
    ### 2. GESTION DE VENTA DE ENTRADAS ###
    elif opcion == "2":
        print("### Gestor de ventas de entradas###")
        tickets = []
        codigos_existentes = []
        while True:
            nombre = input('Ingrese su nombre: ')
            cedula = input('Ingrese su cédula: ')
            edad = int(input('Ingrese su edad: '))
            codigo_generado = generar_codigo_boleto(codigos_existentes)
            
            # Muestra las carreras disponibles
            print("Carreras disponibles:")
            for indice, carrera in enumerate(lista_carreras):
                print(f"{indice+1}. {carrera.nombre}")

            indice_carrera = input('Ingrese el índice de la carrera a la que desea comprar un ticket: ')
            while not indice_carrera.isnumeric() or int(indice_carrera) < 1 or int(indice_carrera) > len(lista_circuitos):
                indice_carrera = input("Ingrese un índice válido: ")

            nombre_carrera = lista_carreras[int(indice_carrera) - 1].nombre
            tipo_entrada = input('Ingrese el tipo de entrada que desea comprar (General o Vip): ')

            cliente = Cliente(nombre, cedula, edad, tipo_entrada,codigo_generado,nombre_carrera)
            tickets.append(cliente)
            codigos_existentes.append(codigo_generado)

            nueva_entrada = input('Desea adquirir una nueva entrada? (s/n): ')
            if nueva_entrada.lower() != 's':
                break

        total_sin_descuento_sin_impuesto = sum([150 if ticket.tipo_entrada == 'General' else 340 for ticket in tickets])
        total_con_descuento_sin_impuesto = sum([ticket.obtener_precio_entrada() / 1.16 for ticket in tickets])
        total_con_descuento_con_impuesto = sum([ticket.obtener_precio_entrada() for ticket in tickets])
        
        print(f"Carrera seleccionada: {nombre_carrera}")
        print(f"Codigo : {codigo_generado}")    
        print(f'Subtotal: {total_sin_descuento_sin_impuesto}')
        print(f'Descuento: {total_sin_descuento_sin_impuesto - total_con_descuento_sin_impuesto}')
        print(f'IVA: {total_con_descuento_con_impuesto - total_con_descuento_sin_impuesto}')
        print(f'Total: {total_con_descuento_con_impuesto}\n\n')

        
    ### 3. GESTION DE ASISTENCIAS A LAS CARRERAS ###
    elif opcion == "3":
        print("### Gestion de asistencias ###")
        codigo_a_chequear = input("\n===Ingrese el codigo===\n==> ")
        check_ticket(codigo_a_chequear,codigos_existentes)
    
    ### 4.  GESTION DE RESTAURANTES ###
    elif opcion == "4":
            print("===GESTION DE RESTAURANTES===\n Que desea hacer?\n1. Buscar por nombre el producto\n2. Buscar productos por tipos\n3. Buscar productos por rango\n---> ")
            opcionA_2 = input()
            if opcionA_2 == "1":
                nombre = input("Ingresa el nombre del producto\n***> ")
                busqueda = busqueda_por_nombre(carreras,nombre)
                print(busqueda)
            elif opcionA_2 == "2":
                tipo = input("Que tipo desea buscar\n")
                busqueda_tipo = buscar_por_tipos(carreras,tipo)
                print(busqueda_tipo)
            elif opcionA_2 == "3":
                precio_minimo = input("ingrese el precio minimo")
                precio_maximo = input("Ingrese el precio maximo")
                precio_maximo = float(precio_maximo)
                precio_minimo = float(precio_minimo)
                busqueda = busqueda_por_rango(carreras,precio_minimo,precio_maximo)
                print(busqueda)
    ### GESTION DE VENTA DE RESTAURANTE ###
    elif opcion == "5":
        print("===GESTION DE VENTA DE RESTAURANTES===\n")
        # Validar si el cliente es VIP
        cedula_cliente = input("Ingrese su cédula: ")
        cliente_vip = es_cliente_vip(cedula_cliente, tickets)
        if cliente_vip:
            print(f"Cliente VIP encontrado: {cliente_vip.nombre}")
            # Encontrar la carrera seleccionada por el cliente VIP
            nombre_carrera_cliente_vip = cliente_vip.carrera_seleccionada
            print(f"Carrera seleccionada por el cliente VIP: {nombre_carrera_cliente_vip}")
            carrera_seleccionada = None
            for carrera in lista_carreras:
                print(f"Revisando carrera: {carrera.nombre}")
                if carrera.nombre == nombre_carrera_cliente_vip:
                    carrera_seleccionada = carrera
                    break

            if not carrera_seleccionada:
                print("Lo siento, no se encontró la carrera seleccionada.")
                break
            else:
                # Mostrar restaurantes disponibles
                print(f"Restaurantes disponibles para la carrera {carrera_seleccionada.nombre}:")
                for i, restaurante in enumerate(carrera_seleccionada.obtener_restaurantes()):
                    print(f"{i + 1}. {restaurante.nombre}")
            # Seleccionar restaurante
            opcion_restaurante = input("Ingrese el número del restaurante que desea visitar: ")
            while not opcion_restaurante.isnumeric() or int(opcion_restaurante) < 1 or int(opcion_restaurante) > sum(len(carrera.obtener_restaurantes()) for carrera in lista_carreras):
                opcion_restaurante = input("Ingrese un número válido: ")

            # Obtener el restaurante seleccionado
            total_restaurantes = 0
            for i, carrera in enumerate(lista_carreras):
                for j, restaurante in enumerate(carrera.obtener_restaurantes()):
                    total_restaurantes += 1
                    if total_restaurantes == int(opcion_restaurante):
                        restaurante_seleccionado = restaurante
                        break

            # Mostrar menú del restaurante seleccionado
            print("Menú:")
            for i, item in enumerate(restaurante_seleccionado.productos):
                print(f"{i + 1}. {item.nombre} - {item.precio}")
            # Crear carrito de compras
            carrito = []

            # Agregar productos al carrito
            opcion_producto = input("Ingrese el número del producto que desea comprar o 'q' para terminar: ")
            while opcion_producto != 'q':
                while not opcion_producto.isnumeric() or int(opcion_producto) < 1 or int(opcion_producto) > len(restaurante_seleccionado.productos):
                    opcion_producto = input("Ingrese un número válido: ")
                producto_seleccionado = restaurante_seleccionado.productos[int(opcion_producto) - 1]
                if producto_seleccionado.tipo == "drink:alcoholic" and cliente_vip.edad < 18:
                    print("Lo siento, no puedes comprar bebidas alcohólicas si eres menor de 18 años.")
                else:
                    carrito.append(producto_seleccionado)
                    print(f"{producto_seleccionado.nombre} ha sido añadido al carrito.")

                opcion_producto = input("Ingrese el número del producto que desea comprar o 'q' para terminar: ")

            # Mostrar resumen de la compra
            subtotal = sum(item.precio for item in carrito)
            descuento = calcular_descuento(cedula_cliente, subtotal)
            # Mostrar resumen de la compra
            subtotal = sum(item.precio for item in carrito)
            descuento = calcular_descuento(cedula_cliente, subtotal)
            total = subtotal - descuento

            print("\nResumen de la compra:")
            for item in carrito:
                print(f"{item.nombre} - {item.precio}")
            print(f"Subtotal: {subtotal}")
            print(f"Descuento: {descuento}")
            print(f"Total: {total}")

            # Proceder con la compra
            confirmar_compra = input("\n¿Desea proceder con la compra? (s/n): \n")
            if confirmar_compra.lower() == 's':
                print("Pago exitoso. Gracias por su compra.")
            else:
                print("Compra cancelada.")
        else:
            print("\nLo siento, sólo los clientes VIP pueden comprar en los restaurantes\n.")

    ### INDICADORES DE GESTION (ESTADISTICAS)###
    elif opcion == "6":
        print("===INDICADORES DE GESTIÓN (ESTADÍSTICAS)===")
        opcionA_3 = input("¿Qué desea ver?\n1. Promedio de gasto de un cliente VIP en una carrera (ticket + restaurante)\n2. Mostrar tabla con la asistencia a las carreras de mejor a peor\n3. ¿Cuál fue la carrera con mayor asistencia?\n4. ¿Cuál fue la carrera con mayor boletos vendidos?\n5. Top 3 productos más vendidos en el restaurante.\n6. Top 3 de clientes (clientes que más compraron boletos)\n7. Realizar gráficos con dichas estadísticas con las librerías de mathplotlib o Bokeh (Bono).\n==> ")
        if opcionA_3 == "1":
            print("\n=== Promedio de gastos clientes vip===\n")
            promedio_gastos = promedio_gasto_cliente_vip(tickets)
            print(promedio_gastos)
        elif opcionA_3 == "2":
            print("\n=== Tablas de asistencias===\n")
            pass
        elif opcionA_3 == "3":
            print("\n=== Carrera con mayor asistencia ===\n")
            carrera_mayor_asis = carrera_mayor_asistencia(tickets)
            print(carrera_mayor_asis)
        elif opcionA_3 == "4":
            print("\n=== Carrera con mayor boletos vendidos ===\n")
            print(carrera_mayor_boletos_vendidos(carreras))
        elif opcionA_3 == "5":
            print("\n=== Top 3 productos más vendidos en el restaurante===\n")
            print(top_3_productos_mas_vendidos(carrito))
        elif opcionA_3 == "6":
            print("\n=== Top 3 clientes ===\n")
            print(top_3_clientes_boletos(tickets))
        elif opcionA_3 == "7":
            print("\n=== Graficos ===\n")
            pass
    ### OPCION PARA SALIR DEL PROGRAMA ###
    elif opcion == "7":
        break



    
