import tkinter as tk

class Usuario():
    
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.id = tk.StringVar(ventanaPrincipal)
        self.titulo = tk.StringVar(ventanaPrincipal)
        self.artista = tk.StringVar(ventanaPrincipal)
        self.duracion = tk.StringVar(ventanaPrincipal)
        self.genero = tk.StringVar(ventanaPrincipal)