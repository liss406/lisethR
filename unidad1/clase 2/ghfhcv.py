from tkinter import Frame, Tk
from tkinter.messagebox import askyesno

ventanaPrincipal = Tk()
ventanaPrincipal.title("prueba de eventos")

def action_click(event):
    frame.focus_set()
    print("clicked att", event.x, event.y)
    
def presionar_tecla(event):
    print("pressed", repr(event.char))

def el_ususario_quiere_salir():
    if askyesno("salir de la aplicacion","¿seguro quieres salir de la aplicaccion?"):
        ventanaPrincipal.destroy()

frame = Frame(ventanaPrincipal, width=500, height=500)
frame.bind("<Key>", presionar_tecla)
frame.bind("<Button -1>", action_click)
frame.pack()

ventanaPrincipal.protocol("WM_DELETE_WINDOW",  el_ususario_quiere_salir)
ventanaPrincipal.mainloop()
