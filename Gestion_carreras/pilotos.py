class Piloto:
    def __init__(self, nombre, apellido, fecha_nacimiento, lugar_nacimiento, numero, equipo, ):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.lugar_nacimiento = lugar_nacimiento
        self.numero = numero
        self.equipo = equipo
        
        
    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nNúmero: {self.numero}\nLugar de nacimiento: {self.lugar_nacimiento}\nFecha de nacimiento: {self.fecha_nacimiento}\nEquipo: {self.equipo}\n"
    