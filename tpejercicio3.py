#Diseñar una ventana de inicio con las siguientes características,
#Una imagen del colegio.
#Un botón con el texto “Ingresar”
#Un botón con el texto “Registrarse”
#Una etiqueta con el nombre de los programadores.
from tkinter import *
import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()
#ventana= Tk()
ventana.geometry("300x300")
#imagen
logo= PhotoImage(file="img/2222.png")
Label(ventana, image=logo).place(x=10, y=40)
# Crear un Label (etiqueta) en la ventana
label = tk.Label(ventana, text="¡tocar boton!", font=("Arial", 14))
label.pack(pady=20)
#botones
def cambiar_texto1():
    label.config(text="INGRESASTE")
def cambiar_texto2():
     label.config(text="REGISTRAR")

button=tk.Button(ventana, text="Ingresar", command= cambiar_texto1)
button.pack(pady=100)

button2=tk.Button(ventana, text="Registrar", command= cambiar_texto2)
button2.pack()
#etiqueta de los progrmadores

label2 = tk.Label(ventana, text="¡Anita,Victoria!", font=("Arial", 14))
label2.pack(pady=20)

ventana.mainloop()