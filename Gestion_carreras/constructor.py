class Constructor:
    def __init__(self, id, nombre, nacionalidad):
        self.id = id
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        
    def __str__(self):
        return f"ID: {self.id}\nNombre: {self.nombre}\nNacionalidad: {self.nacionalidad}\n\n"
    
    def obtener_id(self):
        return self.id
    
