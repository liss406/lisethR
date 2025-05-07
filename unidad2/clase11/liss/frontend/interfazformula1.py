import tkinter as tk
from tkinter.messagebox import askyesno, showinfo, showerror
import requests
import re
from tkinter import *

API_URL = "http://127.0.0.1:8000/api/Formula1/"

def el_usuario_quiere_salir():
    if askyesno('Salir de la aplicación', '¿Seguro que quieres cerrar la aplicación?'):
        ventanaPrincipal.destroy()

def evento_precionar_tecla(event, labelValidacion, entrada, tipo):
    texto_validar = ""
    if tipo == "letras":
        if validar_letras(entrada):
            texto_validar = ""
        else:
            texto_validar = "Solo se permiten letras"
    elif tipo == "numeros":
        if validar_numeros(entrada):
            texto_validar = ""
        else:
            texto_validar = "Solo se permiten números"
    labelValidacion.config(text=texto_validar)

def validar_letras(valor):
    patron = re.compile("^[A-Za-zñÑ ]*$")
    return patron.match(valor.get()) is not None

def validar_numeros(valor):
    patron = re.compile("^[0-9.,]*$")
    return patron.match(valor.get()) is not None

def buscar():
    id_formula1 = entryID.get()
    if id_formula1:
        response = requests.get(API_URL + id_formula1 + "/")
        if response.status_code == 200:
            data = response.json()
            entryPiloto.delete(0, END)
            entryPiloto.insert(0, data['piloto'])
            entryEscuderia.delete(0, END)
            entryEscuderia.insert(0, data['escuderia'])
            entryRendimiento.delete(0, END)
            entryRendimiento.insert(0, str(data['rendimiento']))
            entryGenero.delete(0, END)
            entryGenero.insert(0, data['genero'])
            showinfo("Encontrado", f"Registro con ID {id_formula1} encontrado")
        else:
            showerror("Error", "Registro no encontrado")
            limpiar_campos()

def guardar(piloto, escuderia, rendimiento, genero):
    data = {
        "piloto": piloto,
        "escuderia": escuderia,
        "rendimiento": rendimiento,
        "genero": genero
    }
    response = requests.post(API_URL, json=data)
    if response.status_code in (200, 201):
        showinfo("Éxito", "Registro guardado correctamente")
    else:
        showerror("Error", "No se pudo guardar el registro")
    limpiar_campos()

def actualizar():
    id_formula1 = entryID.get()
    if id_formula1:
        data = {
            "piloto": entryPiloto.get(),
            "escuderia": entryEscuderia.get(),
            "rendimiento": float(entryRendimiento.get()),
            "genero": entryGenero.get()
        }
        response = requests.put(API_URL + id_formula1 + "/", json=data)
        if response.status_code == 200:
            showinfo("Éxito", "Registro actualizado correctamente")
        else:
            showerror("Error", "No se pudo actualizar el registro")
        limpiar_campos()

def eliminar():
    id_formula1 = entryID.get()
    if id_formula1:
        response = requests.delete(API_URL + id_formula1 + "/")
        if response.status_code == 204:
            showinfo("Éxito", "Registro eliminado correctamente")
        else:
            showerror("Error", "No se pudo eliminar el registro")
        limpiar_campos()

def limpiar_campos():
    entryID.delete(0, END)
    entryPiloto.delete(0, END)
    entryEscuderia.delete(0, END)
    entryRendimiento.delete(0, END)
    entryGenero.delete(0, END)

# Ventana principal
ventanaPrincipal = tk.Tk()
ventanaPrincipal.geometry("450x480")
ventanaPrincipal.title('Gestión de Pilotos F1')

frame = tk.Frame(ventanaPrincipal)
frame.pack(pady=10)

# ID + Botón Buscar
id_formula1 = tk.StringVar()
labelID = tk.Label(frame, text="ID")
entryID = tk.Entry(frame, textvariable=id_formula1)
btn_buscar = tk.Button(frame, text="Buscar", width=10, command=buscar)

labelID.grid(row=0, column=0, padx=5, pady=5)
entryID.grid(row=0, column=1, padx=5, pady=5)
btn_buscar.grid(row=0, column=2, padx=5, pady=5)

# Piloto
piloto = tk.StringVar(frame)
labelPiloto = tk.Label(frame, text="Piloto")
entryPiloto = tk.Entry(frame, textvariable=piloto)
labelValidacionPiloto = tk.Label(frame, text="", fg="red")
entryPiloto.bind("<KeyRelease>", lambda event: evento_precionar_tecla(event, labelValidacionPiloto, piloto, "letras"))

labelPiloto.grid(row=1, column=0, padx=5, pady=5)
entryPiloto.grid(row=1, column=1, padx=5, pady=5)
labelValidacionPiloto.grid(row=2, column=1)

# Escudería
escuderia = tk.StringVar(frame)
labelEscuderia = tk.Label(frame, text="Escudería")
entryEscuderia = tk.Entry(frame, textvariable=escuderia)
labelValidacionEscuderia = tk.Label(frame, text="", fg="red")
entryEscuderia.bind("<KeyRelease>", lambda event: evento_precionar_tecla(event, labelValidacionEscuderia, escuderia, "letras"))

labelEscuderia.grid(row=3, column=0, padx=5, pady=5)
entryEscuderia.grid(row=3, column=1, padx=5, pady=5)
labelValidacionEscuderia.grid(row=4, column=1)

# Rendimiento
rendimiento = tk.StringVar(frame)
labelRendimiento = tk.Label(frame, text="Rendimiento")
entryRendimiento = tk.Entry(frame, textvariable=rendimiento)
labelValidacionRendimiento = tk.Label(frame, text="", fg="red")
entryRendimiento.bind("<KeyRelease>", lambda event: evento_precionar_tecla(event, labelValidacionRendimiento, rendimiento, "numeros"))

labelRendimiento.grid(row=5, column=0, padx=5, pady=5)
entryRendimiento.grid(row=5, column=1, padx=5, pady=5)
labelValidacionRendimiento.grid(row=6, column=1)

# Género
genero = tk.StringVar(frame)
labelGenero = tk.Label(frame, text="Género")
entryGenero = tk.Entry(frame, textvariable=genero)
labelValidacionGenero = tk.Label(frame, text="", fg="red")
entryGenero.bind("<KeyRelease>", lambda event: evento_precionar_tecla(event, labelValidacionGenero, genero, "letras"))

labelGenero.grid(row=7, column=0, padx=5, pady=5)
entryGenero.grid(row=7, column=1, padx=5, pady=5)
labelValidacionGenero.grid(row=8, column=1)

# Botones
frame_botones = tk.Frame(ventanaPrincipal)
frame_botones.pack(pady=15)

btn_guardar = tk.Button(frame_botones, text="Guardar", width=10, command=lambda:guardar(
    entryPiloto.get(),
    entryEscuderia.get(),
    entryRendimiento.get(),
    entryGenero.get()
))
btn_actualizar = tk.Button(frame_botones, text="Actualizar", width=10, command=actualizar)
btn_eliminar = tk.Button(frame_botones, text="Eliminar", width=10, command=eliminar)

btn_guardar.grid(row=0, column=0, padx=5)
btn_actualizar.grid(row=0, column=1, padx=5)
btn_eliminar.grid(row=0, column=2, padx=5)

ventanaPrincipal.protocol('WM_DELETE_WINDOW', el_usuario_quiere_salir)
ventanaPrincipal.mainloop()