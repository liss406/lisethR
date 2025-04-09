import tkinter as tk
from tkinter import messagebox
import re

class Formula1:
    def __init__(self, escuderia, piloto, rendimiento, genero):
        self.escuderia = escuderia
        self.piloto = piloto
        self.rendimiento = rendimiento
        self.genero = genero

    def validar_letras(self, valor):
        patron = re.compile("^[A-Za-zñÑ]*$")
        resultado = patron.match(valor) is not None
        return resultado

    def evento_presionar_tecla(self, event, campo, labelvalidacion):
        texto = campo.get()
        if self.validar_letras(texto):
            labelvalidacion.config(text="", fg="black")
        else:
            labelvalidacion.config(text="Solo se permiten letras", fg="purple")

    def mostrar_info(self):
        return f"Escudería: {self.escuderia}\nPiloto: {self.piloto}\nRendimiento: {self.rendimiento} min\nGénero: {self.genero}"

def mostrar_informacion():
    escuderia = entryEscuderia.get()
    piloto = entryPiloto.get()
    rendimiento = entryRendimiento.get()
    genero = entryGenero.get()

    if not escuderia or not piloto or not rendimiento or not genero:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return

    try:
        rendimiento = float(rendimiento)
    except ValueError:
        messagebox.showerror("Error", "El rendimiento debe ser un número válido")
        return

    f1 = Formula1(escuderia, piloto, rendimiento, genero)
    messagebox.showinfo("Información de la Formula 1", f1.mostrar_info())

root = tk.Tk()
root.title("Registro de Fórmula 1")
root.geometry("350x350")


tk.Label(root, text="Escudería:").pack(pady=5)
entryEscuderia = tk.Entry(root)
entryEscuderia.pack()
labelvalidacionEscuderia = tk.Label(root, text="", fg="purple")
labelvalidacionEscuderia.pack()


tk.Label(root, text="Piloto:").pack(pady=5)
entryPiloto = tk.Entry(root)
entryPiloto.pack()
labelvalidacionPiloto = tk.Label(root, text="", fg="purple")
labelvalidacionPiloto.pack()


tk.Label(root, text="Rendimiento (min):").pack(pady=5)
entryRendimiento = tk.Entry(root)
entryRendimiento.pack()


tk.Label(root, text="Género:").pack(pady=5)
entryGenero = tk.Entry(root)
entryGenero.pack()
labelvalidacionGenero = tk.Label(root, text="", fg="purple")
labelvalidacionGenero.pack()


btn_mostrar = tk.Button(root, text="Mostrar Información", command=mostrar_informacion)
btn_mostrar.pack(pady=10)

f1 = Formula1("", "", "", "")

entryEscuderia.bind("<KeyRelease>", lambda event: f1.evento_presionar_tecla(event, entryEscuderia, labelvalidacionEscuderia))
entryPiloto.bind("<KeyRelease>", lambda event: f1.evento_presionar_tecla(event, entryPiloto, labelvalidacionPiloto))
entryGenero.bind("<KeyRelease>", lambda event: f1.evento_presionar_tecla(event, entryGenero, labelvalidacionGenero))

root.mainloop()
