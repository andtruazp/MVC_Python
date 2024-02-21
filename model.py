class Cancion:
    def __init__(self, id, titulo, artista, genero):
        self.id =id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero

class CancionModel:
    def __init__(self):
        self.canciones = []

    def agregarCancion(self, cancion):
        self.canciones.append(cancion)
    
    def obtenerCanciones(self):
        return self.canciones

    def obtenerCancion(self, id):
        for cancion in self.canciones:
            if cancion.id == id:
                return cancion
            return None
