class Circuito:
    def __init__(self, nombre, pais, localidad, latitud, longitud):
        self.nombre = nombre
        self.pais = pais
        self.localidad = localidad
        self.latitud = latitud
        self.longitud = longitud

    def __str__(self):
        return f"Nombre: {self.nombre}\nPais: {self.pais}\nLocalidad: {self.localidad}\nLatitud: {self.latitud}\nLongitud: {self.longitud}\n"
    
