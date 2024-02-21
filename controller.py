from model import Cancion, CancionModel
from view import CancionVista

class CancionControlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
    
    def agregarCancion(self, cancion):
        self.modelo.agregarCancion(cancion)

    def obtenerCanciones(self):
        canciones= self.modelo.obtenerCanciones()
        self.vista.mostrarCanciones(canciones)
    
    def obtenerCancion(self, id):
        cancion: self.modelo.obtenerCancion(id)
        self.vista.mostrarCancion(cancion)
