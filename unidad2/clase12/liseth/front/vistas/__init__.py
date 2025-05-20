import tkinter as tk
from controladores.comunicacion import Comunicacion 
from .tabla import Tabla  

class Interfaz():

    def __init__(self):
        self.ventanaPrincipal = tk.Tk()
        self.comunicacion = Comunicacion()
        
        titulos = ['Titulo', 'Artista', 'Duracion', 'Genero']
        columnas = ['titulo', 'artista', 'duracion', 'genero']
        data = []  

        self.tabla = Tabla (self.ventanaPrincipal, titulos, columnas, data)
