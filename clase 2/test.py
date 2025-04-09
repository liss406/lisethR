import tkinter as tk
import re

texto_validar_nombre = ""


ventanaPrincipal = tk.Tk()
nombre = tk.StringVar(ventanaPrincipal)
labelNombre = tk.Label(ventanaPrincipal, text="nombre")
entrynombre = tk.Entry(ventanaPrincipal, textvariable=nombre)
labelvalidacionombre = tk.Label(ventanaPrincipal, text="")

def validar_letras(valor):
    patron = re.compile("^[A-Za-zñÑ]*$")
    resultado = patron.match(valor.get()) is not None
    if not resultado:
        return False
    return True

def evento_presionar_tecla(event):
    global texto_validar_nombre
    global nombre
    if validar_letras(nombre):
        texto_validar_nombre = ""
    else:
        texto_validar_nombre = "solo se permiten letras"
    labelvalidacionombre.config(text = texto_validar_nombre)
    
ventanaPrincipal.title("ventana Pricipal")
ventanaPrincipal.geometry("300x300")
labelNombre.pack()
entrynombre.bind("<KeyRelease>", evento_presionar_tecla)
entrynombre.pack()
labelvalidacionombre.pack()

ventanaPrincipal.mainloop()