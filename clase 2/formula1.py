import tkinter as tk
from tkinter import messagebox
import re

class Formula1:
    def __init__(self, escuderia, piloto, rendimiento, genero):
        self.escuderia = escuderia
        self.piloto = piloto
        self.rendimiento = rendimiento
        self.genero = genero

    def validar_letras(self, valor, labelvalidacion):
        patron = re.compile("^[A-Za-zñÑ]*$")
        resultado = patron.match(valor.get()) is not None
        if not resultado:
            labelvalidacion.config(text="Solo se permiten letras", fg="purple")
        else:
            labelvalidacion.config(text="")
    
    def mostrar_info(self):
        return f"Escudería: {self.escuderia}\nPiloto: {self.piloto}\nRendimiento: {self.rendimiento} min\nGénero: {self.genero}"

def mostrar_informacion():
    escuderia = entryEscuderia.get()
    piloto = entry_piloto.get()
    rendimiento = entry_rendimiento.get()
    genero = entry_genero.get()

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
    
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Registro de Formula 1")
ventanaPrincipal.geometry("300x250")


Escuderia = tk.StringVar(ventanaPrincipal)
labelEscuderia = tk.Label(ventanaPrincipal, text="Escudería")
entryEscuderia = tk.Entry(ventanaPrincipal, textvariable=Escuderia)
labelvalidacionescuderia = tk.Label(ventanaPrincipal, text="", fg="purple")
entryEscuderia.bind("<KeyRelease>", lambda event: Formula1.validar_letras(Formula1, Escuderia, labelvalidacionescuderia))


Piloto = tk.StringVar(ventanaPrincipal)
labelPiloto = tk.Label(ventanaPrincipal, text="Piloto")
entry_piloto = tk.Entry(ventanaPrincipal, textvariable=Piloto)
labelvalidacionPiloto = tk.Label(ventanaPrincipal, text="", fg="purple")
entry_piloto.bind("<KeyRelease>", lambda event: Formula1.validar_letras(Formula1, Piloto, labelvalidacionPiloto))


Rendimiento = tk.StringVar(ventanaPrincipal)
labelRendimiento = tk.Label(ventanaPrincipal, text="Rendimiento")
entry_rendimiento = tk.Entry(ventanaPrincipal, textvariable=Rendimiento)
labelvalidacionRendimiento = tk.Label(ventanaPrincipal, text="", fg="purple")
entry_rendimiento.bind("<KeyRelease>", lambda event: Formula1.validar_letras(Formula1, Rendimiento, labelvalidacionRendimiento))


Genero = tk.StringVar(ventanaPrincipal)
labelGenero = tk.Label(ventanaPrincipal, text="Género")
entry_genero = tk.Entry(ventanaPrincipal, textvariable=Genero)


labelEscuderia.grid(row=0, column=0)
entryEscuderia.grid(row=0, column=1)
labelvalidacionescuderia.grid(row=1, column=1)

labelPiloto.grid(row=2, column=0)
entry_piloto.grid(row=2, column=1)
labelvalidacionPiloto.grid(row=3, column=1)

labelRendimiento.grid(row=4, column=0)
entry_rendimiento.grid(row=4, column=1)
labelvalidacionRendimiento.grid(row=5, column=1)

labelGenero.grid(row=6, column=0)
entry_genero.grid(row=6, column=1)

btn_mostrar = tk.Button(ventanaPrincipal, text="Mostrar información", command=mostrar_informacion)
btn_mostrar.grid(row=7, column=2, pady=10)

ventanaPrincipal.mainloop()
