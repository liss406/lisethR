import threading
import time
import tkinter as tk
from tkinter import messagebox
import requests


URL_API_AUTORES = 'http://127.0.0.1:8000/api/autor/'
URL_API_LIBROS = 'http://127.0.0.1:8000/api/libro/'

autores = []
libros = []


def guardar_respaldo_autores():
    with open("respaldo_autores.txt", "w", encoding="utf-8") as f:
        for a in autores:
            f.write(f"Nombre: {a['nombre']}\n")
            f.write(f"Nacionalidad: {a['nacionalidad']}\n")
            f.write(f"Edad: {a['edad']}\n\n")

def guardar_respaldo_libros():
    with open("respaldo_libros.txt", "w", encoding="utf-8") as f:
        for l in libros:
            f.write(f"Título: {l['titulo']}\n")
            f.write(f"Género: {l['genero']}\n")
            f.write(f"Páginas: {l['paginas']}\n")
            f.write(f"Año: {l['año_publicacion']}\n\n")

def respaldo_periodico():
    while True:
        guardar_respaldo_autores()
        guardar_respaldo_libros()
        time.sleep(60)

# Ventana de autores
def ventana_autores():
    win = tk.Toplevel()
    win.title("Gestión de Autores")
    win.geometry("400x300")

    def registrar_autor():
        nombre = entry_nombre.get()
        nacionalidad = entry_nacionalidad.get()
        edad = entry_edad.get()

        if not nombre or not nacionalidad or not edad:
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return

        try:
            edad_int = int(edad)
        except ValueError:
            messagebox.showerror("Error", "Edad debe ser un número.")
            return

        autor_data = {
            "nombre": nombre,
            "nacionalidad": nacionalidad,
            "edad": edad_int
        }

        try:
            response = requests.post(URL_API_AUTORES, json=autor_data)
            if response.status_code in (200, 201):
                autores.append(autor_data)
                messagebox.showinfo("Éxito", "Autor registrado correctamente en el servidor.")
                entry_nombre.delete(0, tk.END)
                entry_nacionalidad.delete(0, tk.END)
                entry_edad.delete(0, tk.END)
            else:
                messagebox.showerror("Error", f"Error del servidor: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error de red", f"No se pudo conectar con el backend:\n{e}")

    def mostrar_autores():
        try:
            response = requests.get(URL_API_AUTORES)
            if response.status_code == 200:
                data = response.json()
                if not data:
                    messagebox.showinfo("Autores", "No hay autores registrados.")
                    return
                datos = "\n".join([f"{a['nombre']} ({a['nacionalidad']}, {a['edad']} años)" for a in data])
                messagebox.showinfo("Autores Registrados", datos)
            else:
                messagebox.showerror("Error", f"Error al obtener autores: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error de conexión", f"No se pudo conectar con el backend:\n{e}")

    tk.Label(win, text="Nombre:").pack()
    entry_nombre = tk.Entry(win)
    entry_nombre.pack()

    tk.Label(win, text="Nacionalidad:").pack()
    entry_nacionalidad = tk.Entry(win)
    entry_nacionalidad.pack()

    tk.Label(win, text="Edad:").pack()
    entry_edad = tk.Entry(win)
    entry_edad.pack()

    tk.Button(win, text="Registrar Autor", command=registrar_autor).pack(pady=5)
    tk.Button(win, text="Mostrar Autores", command=mostrar_autores).pack(pady=5)

# Ventana de libros
def ventana_libros():
    win = tk.Toplevel()
    win.title("Gestión de Libros")
    win.geometry("400x300")

    def registrar_libro():
        titulo = entry_titulo.get()
        genero = entry_genero.get()
        paginas = entry_paginas.get()
        anio = entry_anio.get()

        if not titulo or not genero or not paginas or not anio:
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return

        try:
            paginas_int = int(paginas)
            anio_int = int(anio)
        except ValueError:
            messagebox.showerror("Error", "Páginas y Año deben ser números.")
            return

        libro_data = {
            "titulo": titulo,
            "genero": genero,
            "paginas": paginas_int,
            "año_publicacion": anio_int
        }

        try:
            response = requests.post(URL_API_LIBROS, json=libro_data)
            if response.status_code in (200, 201):
                libros.append(libro_data)
                messagebox.showinfo("Éxito", "Libro registrado correctamente en el servidor.")
                entry_titulo.delete(0, tk.END)
                entry_genero.delete(0, tk.END)
                entry_paginas.delete(0, tk.END)
                entry_anio.delete(0, tk.END)
            else:
                messagebox.showerror("Error", f"Error del servidor: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error de red", f"No se pudo conectar con el backend:\n{e}")

    def mostrar_libros():
        try:
            response = requests.get(URL_API_LIBROS)
            if response.status_code == 200:
                data = response.json()
                if not data:
                    messagebox.showinfo("Libros", "No hay libros registrados.")
                    return
                datos = "\n".join([
                    f"{l['titulo']} ({l['genero']}, {l['paginas']} pág., {l['año_publicacion']})"
                    for l in data
                ])
                messagebox.showinfo("Libros Registrados", datos)
            else:
                messagebox.showerror("Error", f"Error al obtener libros: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error de conexión", f"No se pudo conectar con el backend:\n{e}")

    tk.Label(win, text="Título:").pack()
    entry_titulo = tk.Entry(win)
    entry_titulo.pack()

    tk.Label(win, text="Género:").pack()
    entry_genero = tk.Entry(win)
    entry_genero.pack()

    tk.Label(win, text="Páginas:").pack()
    entry_paginas = tk.Entry(win)
    entry_paginas.pack()

    tk.Label(win, text="Año de Publicación:").pack()
    entry_anio = tk.Entry(win)
    entry_anio.pack()

    tk.Button(win, text="Registrar Libro", command=registrar_libro).pack(pady=5)
    tk.Button(win, text="Mostrar Libros", command=mostrar_libros).pack(pady=5)

# Menú principal
def mostrar_menu():
    threading.Thread(target=respaldo_periodico, daemon=True).start()

    menu = tk.Tk()
    menu.title("Menú Principal")
    menu.geometry("300x200")

    tk.Label(menu, text="Bienvenido").pack(pady=10)
    tk.Button(menu, text="Gestionar Autores", command=ventana_autores).pack(pady=10)
    tk.Button(menu, text="Gestionar Libros", command=ventana_libros).pack(pady=10)

    menu.mainloop()

mostrar_menu()