from pilotos import *
from constructor import *

class Carrera:
    def __init__(self, nombre, numero_carrera, fecha, circuito, podium, pais, lista_restaurantes):
        self.nombre = nombre
        self.numero_carrera = numero_carrera
        self.fecha = fecha
        self.circuito = circuito
        self.pais = pais
        self.podium = podium
        self.restaurants = lista_restaurantes

    def __str__(self):
        return f"Nombre: {self.nombre}\nNumero de carrera: {self.numero_carrera}\nFecha: {self.fecha}\nCircuito: {self.circuito}\n"
    
    @property
    def restaurants(self):
        return self._restaurants

    @restaurants.setter
    def restaurants(self, lista_restaurantes):
        self._restaurants = lista_restaurantes

    def obtener_restaurantes(self):
        return self.restaurants

   