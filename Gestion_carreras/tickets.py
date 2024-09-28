from funciones import es_numero_ondulado

class Cliente:
    def __init__(self, nombre, cedula, edad, tipo_entrada,codigo,carrera_seleccionada):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.tipo_entrada = tipo_entrada
        self.codigo = codigo
        self.carrera_seleccionada = carrera_seleccionada

    def obtener_precio_entrada(self):
        precio_base = 150 if self.tipo_entrada == 'General' else 340
        if es_numero_ondulado(self.cedula):
            precio_base *= 0.5
            print('Felicidades! Usted tiene un descuento del 50% en su entrada por tener una cédula ondulada.')
        return precio_base * 1.16

   