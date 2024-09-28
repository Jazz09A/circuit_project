from carrera import *
from pilotos import *
from circuito import *
from constructor import *
class Temporada:
    def __init__(self, nombre, circuitos, pilotos, equipos):
        self.nombre = nombre
        self.circuitos = circuitos
        self.pilotos = pilotos
        self.equipos = equipos
        self.carreras = []
    
    def agregar_carrera(self, fecha, circuito, participantes):
        carrera = Carrera(fecha, circuito, participantes)
        self.carreras.append(carrera)
    
    def calcular_puntos_constructores(self):
        # Creamos un diccionario para almacenar los puntajes de cada equipo
        puntajes_equipos = {equipo: 0 for equipo in self.equipos}
    
    # Sumamos los puntajes
        for carrera in self.carreras:
            for equipo, piloto in carrera.podio.items():
                # Si el piloto está en el podio, le asignamos el puntaje correspondiente
                if piloto is not None:
                    puntaje = 0
                    if piloto == carrera.primero:
                        puntaje = 25
                    elif piloto == carrera.segundo:
                        puntaje = 18
                    elif piloto == carrera.tercero:
                        puntaje = 15
                    puntajes_equipos[equipo] += puntaje
        
        return puntajes_equipos