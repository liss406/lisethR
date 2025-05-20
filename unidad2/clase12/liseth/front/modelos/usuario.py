import tkinter as tk

class Usuario():
    
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.id = tk.StringVar(ventanaPrincipal)
        self.escuderia = tk.StringVar(ventanaPrincipal)
        self.piloto = tk.StringVar(ventanaPrincipal)
        self.rendimiento = tk.StringVar(ventanaPrincipal)
        self.genero = tk.StringVar(ventanaPrincipal)