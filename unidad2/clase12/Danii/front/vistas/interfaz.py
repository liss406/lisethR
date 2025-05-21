import tkinter as tk
from controladores.comunicacion import Comunicacion
from modelos.usuario import Usuario
from .tabla import Tabla

class Interfaz:

    def __init__(self):
        titulos = ["id", "Titulo", "Artista", "Duración", "Genero"]
        columnas = ("id", "Titulo", "Artista", "Duración", "Genero")
        data = []
        self.ventanaPrincipal = tk.Tk()
        self.comunicacion = Comunicacion(self.ventanaPrincipal)
        self.tabla = Tabla(self.ventanaPrincipal, titulos, columnas, data)
        pass

    def accion_guardar_boton(self, id, titulo, artista, duracion, genero):
        if id == '':
            self.comunicacion.guardar(titulo, artista, duracion, genero)
        else:
            self.comunicacion.actualizar(id, titulo, artista, duracion, genero)

    def accion_consultar_boton(self, labelConsulta, id):
        resultado = self.comunicacion.consultar(id)
        if resultado:
            labelConsulta.config(text="Titulo: " + str(resultado.get('titulo')) + " Artista: " + str(resultado.get('artista')) + " Duracion: " + str(resultado.get('duracion')) + " Genero: " + str(resultado.get('genero')))
            data = [(
                resultado.get('id'),
                resultado.get('titulo'),
                resultado.get('artista'),
                resultado.get('duracion'),
                resultado.get('genero')
            )]
            self.tabla.refrescar(data)
        else:
            labelConsulta.config(text="Cancion no encontrada.")
            self.tabla.refrescar([]) 


    def accion_consultar_todo(self, titulo, artista, duracion, genero):
        resultado = self.comunicacion.consultar_todo(titulo, artista, duracion, genero)
        data = []
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('titulo'), elemento.get('artista'), elemento.get('duracion'), elemento.get('genero')))
        self.tabla.refrescar(data)
        print(data)
           
    def mostrar_interfaz(self):
        usuario = Usuario(self.ventanaPrincipal)

        labelId = tk.Label(self.ventanaPrincipal, text="Id")
        entryId = tk.Entry(self.ventanaPrincipal, textvariable=usuario.id)
        labelTitulo = tk.Label(self.ventanaPrincipal, text="Titulo")
        entryTitulo = tk.Entry(self.ventanaPrincipal, textvariable=usuario.titulo)
        labelArtista = tk.Label(self.ventanaPrincipal, text="Artista")
        entryArtista = tk.Entry(self.ventanaPrincipal, textvariable=usuario.artista)
        labelDuracion = tk.Label(self.ventanaPrincipal, text="Duracion")
        entryDuracion = tk.Entry(self.ventanaPrincipal, textvariable=usuario.duracion)
        labelGenero = tk.Label(self.ventanaPrincipal, text="Genero")
        entryGenero = tk.Entry(self.ventanaPrincipal, textvariable=usuario.genero)
        labelConsulta = tk.Label(self.ventanaPrincipal, text='')

        boton_guardar = tk.Button(self.ventanaPrincipal, 
                   text="Guardar", 
                   command=lambda: self.accion_guardar_boton(entryId.get(), entryTitulo.get(), entryArtista.get(), entryDuracion.get(), entryGenero.get()))
        
        boton_consultar_1 = tk.Button(self.ventanaPrincipal, 
                   text="Consultar 1", 
                   command=lambda: self.accion_consultar_boton(labelConsulta, entryId.get()))
        

        boton_consultar_todos = tk.Button(self.ventanaPrincipal, 
                   text="Consultar todos", 
                   command=lambda: self.accion_consultar_todo(entryTitulo.get(), entryArtista.get(), entryDuracion.get(), entryGenero.get()))

        self.ventanaPrincipal.title("Gestión de Canciones")
        self.ventanaPrincipal.geometry("1000x600")
        labelId.pack()
        entryId.pack()
        labelTitulo.pack()
        entryTitulo.pack()
        labelArtista.pack()
        entryArtista.pack()
        labelDuracion.pack()
        entryDuracion.pack()
        labelGenero.pack()
        entryGenero.pack()
        boton_guardar.pack()
        boton_consultar_1.pack()
        boton_consultar_todos.pack()
        labelConsulta.pack()
        self.tabla.tabla.pack()


        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                entryId.delete(0, tk.END)
                entryId.insert(0, str(valores[0]))
                entryTitulo.delete(0, tk.END)
                entryTitulo.insert(0, str(valores[1]))
                entryArtista.delete(0, tk.END)
                entryArtista.insert(0, str(valores[2]))
                entryDuracion.delete(0, tk.END)
                entryDuracion.insert(0, str(valores[3]))
                entryGenero.delete(0, tk.END)
                entryGenero.insert(0, str(valores[4]))

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicacion.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)

        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)

        self.ventanaPrincipal.mainloop()