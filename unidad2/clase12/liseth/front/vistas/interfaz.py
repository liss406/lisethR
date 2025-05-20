import tkinter as tk
from controladores.comunicacion import Comunicacion
from modelos.usuario import Usuario
from .tabla import Tabla


class Interfaz:
    
    def __init__(self):
        titulos = ['ID', 'piloto', 'escuderia', 'rendimiento', 'genero']
        columnas = ['id', 'piloto', 'escuderia', 'rendimiento', 'genero']
        data = []
        self.ventanaPrincipal = tk.Tk()
        self.comunicacion = Comunicacion(self.ventanaPrincipal)
        self.tabla = Tabla(self.ventanaPrincipal, titulos, columnas, data)
        pass

    def accion_guardar_boton(self, id, piloto, escuderia, rendimiento, genero):
        if id == '':
            self.comunicacion.guardar(piloto, escuderia, rendimiento, genero)
        else:
            self.comunicacion.actualizar(id, piloto, escuderia, rendimiento, genero)

    # def accion_consultar_boton(self, id):
    #     resultado = self.comunicacion.consultar(id)
    #     data = []
    #     for elemento in resultado:
    #         data.append((
    #             resultado.get('id'),
    #             resultado.get('piloto'),
    #             resultado.get('escuderia'),
    #             resultado.get('rendimiento'),
    #             resultado.get('genero'),
    #         ))
    #         self.tabla.refrescar(data)
    #     else:
    #         self.tabla.refrescar([])
            
    def accion_consultar_boton(self, labelConsulta, id):
        resultado = self.comunicacion.consultar(id)
        
        if resultado:
            texto = "Piloto: " + str(resultado.get('piloto', '')) + \
                ", Escuderia: " + str(resultado.get('escuderia', '')) + \
                ", Rendimiento: " + str(resultado.get('rendimiento', '')) + \
                ", Genero: " + str(resultado.get('genero', ''))
        else:
            texto = "Registro no encontrado"
            
        labelConsulta.config(text=texto)
        
        
    def accion_consultar_todo(self, piloto, escuderia, rendimiento, genero):
        resultado = self.comunicacion.consultar_todo(piloto, escuderia, rendimiento, genero)
        data = []
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('piloto'), elemento.get('escuderia'), elemento.get('rendimiento'), elemento.get('genero')))
        self.tabla.refrescar(data)
        print(data)

    def mostrar_interfaz(self):
        usuario = Usuario(self.ventanaPrincipal)

        labelId = tk.Label(self.ventanaPrincipal, text="Id")
        entryId = tk.Entry(self.ventanaPrincipal, textvariable=usuario.id)
        labelpiloto = tk.Label(self.ventanaPrincipal, text="piloto")
        entrypiloto = tk.Entry(self.ventanaPrincipal, textvariable=usuario.escuderia)
        labelescuderia = tk.Label(self.ventanaPrincipal, text="escuderia")
        entryescuderia = tk.Entry(self.ventanaPrincipal, textvariable=usuario.piloto)
        labelrendimiento = tk.Label(self.ventanaPrincipal, text="rendimiento")
        entryrendimiento = tk.Entry(self.ventanaPrincipal, textvariable=usuario.rendimiento)
        labelGenero = tk.Label(self.ventanaPrincipal, text="Genero")
        entryGenero = tk.Entry(self.ventanaPrincipal, textvariable=usuario.genero)
        labelConsulta = tk.Label(self.ventanaPrincipal, text='')

        boton_guardar = tk.Button(self.ventanaPrincipal,text="Guardar",command=lambda: self.accion_guardar_boton
            (
                entryId.get(),
                entrypiloto.get(),
                entryescuderia.get(),
                entryrendimiento.get(),
                entryGenero.get()
            )
        )

        boton_consultar_1 = tk.Button(self.ventanaPrincipal,text="Consultar 1",command=lambda: self.accion_consultar_boton(labelConsulta, entryId.get())
        )

        boton_consultar_todos = tk.Button(self.ventanaPrincipal,text="Consultar todos",command=lambda: self.accion_consultar_todo
            (
                entryescuderia.get(),
                entrypiloto.get(),
                entryrendimiento.get(),
                entryGenero.get()
            )
        )
        
        self.ventanaPrincipal.title("Gestión de Canciones")
        self.ventanaPrincipal.geometry("800x600")
        labelId.pack()
        entryId.pack()
        labelpiloto.pack()
        entrypiloto.pack()
        labelescuderia.pack()
        entryescuderia.pack()
        labelrendimiento.pack()
        entryrendimiento.pack()
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
                entrypiloto.delete(0, tk.END)
                entrypiloto.insert(0, str(valores[1]))
                entryescuderia.delete(0, tk.END)
                entryescuderia.insert(0, str(valores[2]))
                entryrendimiento.delete(0, tk.END)
                entryrendimiento.insert(0, str(valores[3]))
                entryGenero.delete(0, tk.END)
                entryGenero.insert(0, str(valores[4]))

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicacion.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)

        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)

        self.ventanaPrincipal.mainloop()



