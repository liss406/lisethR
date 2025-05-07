import tkinter as tk
from tkinter import messagebox

# Backend simulado en memoria
autores = []
libros = []

# Funciones de autores
def registrar_autor():
    nombre = entry_nombre.get()
    nacionalidad = entry_nacionalidad.get()
    edad = entry_edad.get()

    if not nombre or not nacionalidad or not edad:
        messagebox.showwarning("Atención", "Todos los campos son obligatorios.")
        return

    try:
        edad = int(edad)
    except ValueError:
        messagebox.showerror("Error", "Edad debe ser un número.")
        return

    autores.append({'nombre': nombre, 'nacionalidad': nacionalidad, 'edad': edad})
    messagebox.showinfo("Registro exitoso", "Autor registrado correctamente.")
    entry_nombre.delete(0, tk.END)
    entry_nacionalidad.delete(0, tk.END)
    entry_edad.delete(0, tk.END)

def mostrar_autores():
    if not autores:
        messagebox.showinfo("Autores", "No hay autores registrados.")
        return
    mensaje = "\n".join([f"{a['nombre']} ({a['nacionalidad']}, {a['edad']} años)" for a in autores])
    messagebox.showinfo("Autores Registrados", mensaje)

# Funciones de libros
def registrar_libro():
    titulo = entry_titulo.get()
    genero = entry_genero.get()
    paginas = entry_paginas.get()
    anio = entry_anio.get()

    if not titulo or not genero or not paginas or not anio:
        messagebox.showwarning("Atención", "Todos los campos son obligatorios.")
        return

    try:
        paginas = int(paginas)
        anio = int(anio)
    except ValueError:
        messagebox.showerror("Error", "Páginas y Año deben ser números.")
        return

    libros.append({'titulo': titulo, 'genero': genero, 'paginas': paginas, 'anio': anio})
    messagebox.showinfo("Registro exitoso", "Libro registrado correctamente.")
    entry_titulo.delete(0, tk.END)
    entry_genero.delete(0, tk.END)
    entry_paginas.delete(0, tk.END)
    entry_anio.delete(0, tk.END)

def mostrar_libros():
    if not libros:
        messagebox.showinfo("Libros", "No hay libros registrados.")
        return
    mensaje = "\n".join([f"{l['titulo']} ({l['genero']}, {l['paginas']} pág., {l['anio']})" for l in libros])
    messagebox.showinfo("Libros Registrados", mensaje)

# Interfaz principal
root = tk.Tk()
root.title("Gestión de Autores y Libros")
root.geometry("600x400")

# Sección Autores
frame_autores = tk.LabelFrame(root, text="Autores", padx=10, pady=10)
frame_autores.pack(padx=10, pady=10, fill="both", expand=True)

tk.Label(frame_autores, text="Nombre:").grid(row=0, column=0)
entry_nombre = tk.Entry(frame_autores)
entry_nombre.grid(row=0, column=1)

tk.Label(frame_autores, text="Nacionalidad:").grid(row=1, column=0)
entry_nacionalidad = tk.Entry(frame_autores)
entry_nacionalidad.grid(row=1, column=1)

tk.Label(frame_autores, text="Edad:").grid(row=2, column=0)
entry_edad = tk.Entry(frame_autores)
entry_edad.grid(row=2, column=1)

tk.Button(frame_autores, text="Registrar Autor", command=registrar_autor).grid(row=3, column=0, columnspan=2, pady=5)
tk.Button(frame_autores, text="Mostrar Autores", command=mostrar_autores).grid(row=4, column=0, columnspan=2, pady=5)

# Sección Libros
frame_libros = tk.LabelFrame(root, text="Libros", padx=10, pady=10)
frame_libros.pack(padx=10, pady=10, fill="both", expand=True)

tk.Label(frame_libros, text="Título:").grid(row=0, column=0)
entry_titulo = tk.Entry(frame_libros)
entry_titulo.grid(row=0, column=1)

tk.Label(frame_libros, text="Género:").grid(row=1, column=0)
entry_genero = tk.Entry(frame_libros)
entry_genero.grid(row=1, column=1)

tk.Label(frame_libros, text="Páginas:").grid(row=2, column=0)
entry_paginas = tk.Entry(frame_libros)
entry_paginas.grid(row=2, column=1)

tk.Label(frame_libros, text="Año:").grid(row=3, column=0)
entry_anio = tk.Entry(frame_libros)
entry_anio.grid(row=3, column=1)

tk.Button(frame_libros, text="Registrar Libro", command=registrar_libro).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(frame_libros, text="Mostrar Libros", command=mostrar_libros).grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()

