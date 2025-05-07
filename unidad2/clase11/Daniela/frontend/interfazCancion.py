import tkinter as tk
from tkinter.messagebox import askyesno, showinfo, showerror
import requests
import re
from tkinter import *

API_URL = "http://127.0.0.1:8000/api/cancion/"

def el_usuario_quiere_salir():
    if askyesno('Salir', '¿Seguro que quieres cerrar la aplicación?'):
        ventana.destroy()

def evento_precionar_tecla(event, label, variable, tipo):
    texto = ""
    if tipo == "letras" and not re.match("^[A-Za-zñÑ ]*$", variable.get()):
        texto = "Solo letras"
    elif tipo == "numeros" and not re.match("^[0-9.:]*$", variable.get()):
        texto = "Solo números"
    label.config(text=texto)

def limpiar_campos():
    entryID.delete(0, END)
    entryNombre.delete(0, END)
    entryGenero.delete(0, END)
    entryArtista.delete(0, END)
    entryDuracion.delete(0, END)

def buscar():
    id_cancion = entryID.get()
    if id_cancion:
        response = requests.get(API_URL + id_cancion + "/")
        if response.status_code == 200:
            data = response.json()
            entryNombre.delete(0, END)
            entryNombre.insert(0, data['nombre'])
            entryGenero.delete(0, END)
            entryGenero.insert(0, data['genero'])
            entryArtista.delete(0, END)
            entryArtista.insert(0, data['artista'])
            entryDuracion.delete(0, END)
            entryDuracion.insert(0, data['duracion'])
            showinfo("Éxito", "Canción encontrada")
        else:
            showerror("Error", "Canción no encontrada")
            limpiar_campos()

def guardar():
    data = {
        "nombre": entryNombre.get(),
        "genero": entryGenero.get(),
        "artista": entryArtista.get(),
        "duracion": entryDuracion.get()
    }
    response = requests.post(API_URL, json=data)
    if response.status_code in (200, 201):
        showinfo("Éxito", "Canción guardada")
    else:
        showerror("Error", "Error al guardar")
    limpiar_campos()

def actualizar():
    id_cancion = entryID.get()
    if id_cancion:
        data = {
            "nombre": entryNombre.get(),
            "genero": entryGenero.get(),
            "artista": entryArtista.get(),
            "duracion": entryDuracion.get()
        }
        response = requests.put(API_URL + id_cancion + "/", json=data)
        if response.status_code == 200:
            showinfo("Éxito", "Canción actualizada")
        else:
            showerror("Error", "Error al actualizar")
        limpiar_campos()

def eliminar():
    id_cancion = entryID.get()
    if id_cancion:
        response = requests.delete(API_URL + id_cancion + "/")
        if response.status_code == 204:
            showinfo("Éxito", "Canción eliminada")
        else:
            showerror("Error", "Error al eliminar")
        limpiar_campos()


ventana = tk.Tk()
ventana.geometry("450x480")
ventana.title('Gestión de Canciones')

frame = tk.Frame(ventana)
frame.pack(pady=10)


id_cancion = tk.StringVar()
labelID = tk.Label(frame, text="ID")
entryID = tk.Entry(frame, textvariable=id_cancion)
btn_buscar = tk.Button(frame, text="Buscar", width=10, command=buscar)

labelID.grid(row=0, column=0, padx=5, pady=5)
entryID.grid(row=0, column=1, padx=5, pady=5)
btn_buscar.grid(row=0, column=2, padx=5, pady=5)

nombre = tk.StringVar()
labelNombre = tk.Label(frame, text="Nombre")
entryNombre = tk.Entry(frame, textvariable=nombre)
valNombre = tk.Label(frame, text="", fg="red")
entryNombre.bind("<KeyRelease>", lambda e: evento_precionar_tecla(e, valNombre, nombre, "letras"))

labelNombre.grid(row=1, column=0, padx=5, pady=5)
entryNombre.grid(row=1, column=1, padx=5, pady=5)
valNombre.grid(row=2, column=1)


genero = tk.StringVar()
labelGenero = tk.Label(frame, text="Género")
entryGenero = tk.Entry(frame, textvariable=genero)
valGenero = tk.Label(frame, text="", fg="red")
entryGenero.bind("<KeyRelease>", lambda e: evento_precionar_tecla(e, valGenero, genero, "letras"))

labelGenero.grid(row=3, column=0, padx=5, pady=5)
entryGenero.grid(row=3, column=1, padx=5, pady=5)
valGenero.grid(row=4, column=1)


artista = tk.StringVar()
labelArtista = tk.Label(frame, text="Artista")
entryArtista = tk.Entry(frame, textvariable=artista)
valArtista = tk.Label(frame, text="", fg="red")
entryArtista.bind("<KeyRelease>", lambda e: evento_precionar_tecla(e, valArtista, artista, "letras"))

labelArtista.grid(row=5, column=0, padx=5, pady=5)
entryArtista.grid(row=5, column=1, padx=5, pady=5)
valArtista.grid(row=6, column=1)


duracion = tk.StringVar()
labelDuracion = tk.Label(frame, text="Duración")
entryDuracion = tk.Entry(frame, textvariable=duracion)
valDuracion = tk.Label(frame, text="", fg="red")
entryDuracion.bind("<KeyRelease>", lambda e: evento_precionar_tecla(e, valDuracion, duracion, "numeros"))

labelDuracion.grid(row=7, column=0, padx=5, pady=5)
entryDuracion.grid(row=7, column=1, padx=5, pady=5)
valDuracion.grid(row=8, column=1)


frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=15)

btn_guardar = tk.Button(frame_botones, text="Guardar", width=10, command=guardar)
btn_actualizar = tk.Button(frame_botones, text="Actualizar", width=10, command=actualizar)
btn_eliminar = tk.Button(frame_botones, text="Eliminar", width=10, command=eliminar)

btn_guardar.grid(row=0, column=0, padx=5)
btn_actualizar.grid(row=0, column=1, padx=5)
btn_eliminar.grid(row=0, column=2, padx=5)

ventana.protocol('WM_DELETE_WINDOW', el_usuario_quiere_salir)
ventana.mainloop()
