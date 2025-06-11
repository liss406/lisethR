import threading
import time
import tkinter as tk
from tkinter import messagebox, ttk
import requests

URL_API_AUTORES = 'http://127.0.0.1:8000/api/autor/'
URL_API_LIBROS = 'http://127.0.0.1:8000/api/libro/'


def respaldo_automatico():
    while True:
        try:
            response_autores = requests.get(URL_API_AUTORES)
            if response_autores.status_code == 200:
                with open("respaldo_autores.txt", "w", encoding='utf-8') as f:
                    for autor in response_autores.json():
                        f.write(f"Nombre: {autor['nombre']}\n")
                        f.write(f"Nacionalidad: {autor['nacionalidad']}\n")
                        f.write(f"Edad: {autor['edad']}\n\n")  

            response_libros = requests.get(URL_API_LIBROS)
            if response_libros.status_code == 200:
                with open("respaldo_libros.txt", "w", encoding='utf-8') as f:
                    for libro in response_libros.json():
                        f.write(f"Título: {libro['titulo']}\n")
                        f.write(f"Género: {libro['genero']}\n")
                        f.write(f"Páginas: {libro['paginas']}\n")
                        f.write(f"Año: {libro['año_publicacion']}\n\n") 

            print("Respaldo automático generado.")
        except Exception as e:
            print("Error en respaldo automático:", str(e))
        time.sleep(60)
        
        

def ventana_autores():
    win = tk.Toplevel()
    win.title("Gestión de Autores")
    win.geometry("500x400")

    def cargar_autores():
        for row in tree.get_children():
            tree.delete(row)
        try:
            response = requests.get(URL_API_AUTORES)
            if response.status_code == 200:
                for autor in response.json():
                    tree.insert("", tk.END, values=(autor['id'], autor['nombre'], autor['nacionalidad'], autor['edad']))
            else:
                messagebox.showerror("Error", "No se pudo obtener los autores.")
        except Exception as e:
            messagebox.showerror("Error de red", str(e))

    def registrar_autor():
        nombre = entry_nombre.get()
        nacionalidad = entry_nacionalidad.get()
        edad = entry_edad.get()
        if not nombre or not nacionalidad or not edad:
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return
        try:
            data = {'nombre': nombre, 'nacionalidad': nacionalidad, 'edad': int(edad)}
            response = requests.post(URL_API_AUTORES, json=data)
            if response.status_code in (200, 201):
                cargar_autores()
                entry_nombre.delete(0, tk.END)
                entry_nacionalidad.delete(0, tk.END)
                entry_edad.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Error al registrar autor.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar_autor():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Selecciona", "Selecciona un autor para eliminar.")
            return
        autor_id = tree.item(selected[0])['values'][0]
        response = requests.delete(f"{URL_API_AUTORES}{autor_id}/")
        if response.status_code == 204:
            cargar_autores()
        else:
            messagebox.showerror("Error", "No se pudo eliminar.")

    def actualizar_autor():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Selecciona", "Selecciona un autor para actualizar.")
            return
        autor_id = tree.item(selected[0])['values'][0]
        nombre = entry_nombre.get()
        nacionalidad = entry_nacionalidad.get()
        edad = entry_edad.get()
        if not nombre or not nacionalidad or not edad:
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return
        try:
            data = {'nombre': nombre, 'nacionalidad': nacionalidad, 'edad': int(edad)}
            response = requests.put(f"{URL_API_AUTORES}{autor_id}/", json=data)
            if response.status_code in (200, 204):
                cargar_autores()
            else:
                messagebox.showerror("Error", "Error al actualizar autor.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Label(win, text="Nombre").pack()
    entry_nombre = tk.Entry(win)
    entry_nombre.pack()

    tk.Label(win, text="Nacionalidad").pack()
    entry_nacionalidad = tk.Entry(win)
    entry_nacionalidad.pack()

    tk.Label(win, text="Edad").pack()
    entry_edad = tk.Entry(win)
    entry_edad.pack()

    frame_btn = tk.Frame(win)
    frame_btn.pack(pady=5)

    tk.Button(frame_btn, text="Registrar", command=registrar_autor).grid(row=0, column=0, padx=5)
    tk.Button(frame_btn, text="Actualizar", command=actualizar_autor).grid(row=0, column=1, padx=5)
    tk.Button(frame_btn, text="Eliminar", command=eliminar_autor).grid(row=0, column=2, padx=5)
    tk.Button(frame_btn, text="Consultar Todo", command=cargar_autores).grid(row=0, column=3, padx=5)

    cols = ("ID", "Nombre", "Nacionalidad", "Edad")
    tree = ttk.Treeview(win, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
    tree.pack(expand=True, fill='both')

    cargar_autores()

# Ventana de gestión de libros
def ventana_libros():
    win = tk.Toplevel()
    win.title("Gestión de Libros")
    win.geometry("550x400")

    def cargar_libros():
        for row in tree.get_children():
            tree.delete(row)
        try:
            response = requests.get(URL_API_LIBROS)
            if response.status_code == 200:
                for libro in response.json():
                    tree.insert("", tk.END, values=(libro['id'], libro['titulo'], libro['genero'], libro['paginas'], libro['año_publicacion']))
            else:
                messagebox.showerror("Error", "No se pudo obtener los libros.")
        except Exception as e:
            messagebox.showerror("Error de red", str(e))

    def registrar_libro():
        titulo = entry_titulo.get()
        genero = entry_genero.get()
        paginas = entry_paginas.get()
        año = entry_año.get()
        if not titulo or not genero or not paginas or not año:
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return
        try:
            data = {'titulo': titulo, 'genero': genero, 'paginas': int(paginas), 'año_publicacion': int(año)}
            response = requests.post(URL_API_LIBROS, json=data)
            if response.status_code in (200, 201):
                cargar_libros()
                entry_titulo.delete(0, tk.END)
                entry_genero.delete(0, tk.END)
                entry_paginas.delete(0, tk.END)
                entry_año.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Error al registrar libro.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar_libro():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Selecciona", "Selecciona un libro para eliminar.")
            return
        libro_id = tree.item(selected[0])['values'][0]
        response = requests.delete(f"{URL_API_LIBROS}{libro_id}/")
        if response.status_code == 204:
            cargar_libros()
        else:
            messagebox.showerror("Error", "No se pudo eliminar.")

    def actualizar_libro():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Selecciona", "Selecciona un libro para actualizar.")
            return
        libro_id = tree.item(selected[0])['values'][0]
        titulo = entry_titulo.get()
        genero = entry_genero.get()
        paginas = entry_paginas.get()
        año = entry_año.get()
        if not titulo or not genero or not paginas or not año:
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return
        try:
            data = {'titulo': titulo, 'genero': genero, 'paginas': int(paginas), 'año_publicacion': int(año)}
            response = requests.put(f"{URL_API_LIBROS}{libro_id}/", json=data)
            if response.status_code in (200, 204):
                cargar_libros()
            else:
                messagebox.showerror("Error", "Error al actualizar libro.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Label(win, text="Título").pack()
    entry_titulo = tk.Entry(win)
    entry_titulo.pack()

    tk.Label(win, text="Género").pack()
    entry_genero = tk.Entry(win)
    entry_genero.pack()

    tk.Label(win, text="Páginas").pack()
    entry_paginas = tk.Entry(win)
    entry_paginas.pack()

    tk.Label(win, text="Año de Publicación").pack()
    entry_año = tk.Entry(win)
    entry_año.pack()

    frame_btn = tk.Frame(win)
    frame_btn.pack(pady=5)

    tk.Button(frame_btn, text="Registrar", command=registrar_libro).grid(row=0, column=0, padx=5)
    tk.Button(frame_btn, text="Actualizar", command=actualizar_libro).grid(row=0, column=1, padx=5)
    tk.Button(frame_btn, text="Eliminar", command=eliminar_libro).grid(row=0, column=2, padx=5)
    tk.Button(frame_btn, text="Consultar Todo", command=cargar_libros).grid(row=0, column=3, padx=5)

    cols = ("ID", "Título", "Género", "Páginas", "Año")
    tree = ttk.Treeview(win, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
    tree.pack(expand=True, fill='both')

    cargar_libros()

# Nueva ventana de resumen de datos
def ventana_resumen_datos():
    win = tk.Toplevel()
    win.title("Resumen de Datos")
    win.geometry("900x500")

    tk.Label(win, text="Autores", font=("Arial", 12, "bold")).pack(pady=5)

    cols_autores = ("ID", "Nombre", "Nacionalidad", "Edad")
    tree_autores = ttk.Treeview(win, columns=cols_autores, show='headings')
    for col in cols_autores:
        tree_autores.heading(col, text=col)
    tree_autores.pack(fill='x', padx=10)

    try:
        response_autores = requests.get(URL_API_AUTORES)
        if response_autores.status_code == 200:
            for autor in response_autores.json():
                tree_autores.insert("", tk.END, values=(autor['id'], autor['nombre'], autor['nacionalidad'], autor['edad']))
    except Exception as e:
        messagebox.showerror("Error", f"Error al cargar autores: {str(e)}")

    tk.Label(win, text="Libros", font=("Arial", 12, "bold")).pack(pady=5)

    cols_libros = ("ID", "Título", "Género", "Páginas", "Año")
    tree_libros = ttk.Treeview(win, columns=cols_libros, show='headings')
    for col in cols_libros:
        tree_libros.heading(col, text=col)
    tree_libros.pack(fill='x', padx=10)

    try:
        response_libros = requests.get(URL_API_LIBROS)
        if response_libros.status_code == 200:
            for libro in response_libros.json():
                tree_libros.insert("", tk.END, values=(libro['id'], libro['titulo'], libro['genero'], libro['paginas'], libro['año_publicacion']))
    except Exception as e:
        messagebox.showerror("Error", f"Error al cargar libros: {str(e)}")

# Menú principal
def mostrar_menu():
    threading.Thread(target=respaldo_automatico, daemon=True).start()
    menu = tk.Tk()
    menu.title("Menú Principal")
    menu.geometry("300x220")
    tk.Button(menu, text="Gestionar Autores", command=ventana_autores).pack(pady=10)
    tk.Button(menu, text="Gestionar Libros", command=ventana_libros).pack(pady=10)
    tk.Button(menu, text="Ver Datos Existentes", command=ventana_resumen_datos).pack(pady=10)
    menu.mainloop()

mostrar_menu()
