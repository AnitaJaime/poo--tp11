#Ejercicio 4: Diseñar una ventana de ingreso con las siguientes características:
#Una etiqueta con texto “Usuario”
#Un campo de texto
#Una etiqueta con el texto “Contraseña”
#Un campo de texto
#Un botón con el texto “Ingresar”
#Un botón con el texto “Olvide mi usuario y/o contraseña”
import tkinter as tk
ventana = tk.Tk()
#ventana= Tk()
ventana.geometry("300x300")

# Crear un Label (Usuario) en la ventana
label = tk.Label(ventana, text="¡Usuario!", font=("Arial", 20))
label.pack(pady=20)
# Crear campo de texto - Entry
entry=tk.Entry(ventana,width=30)
entry.pack(padx=10, pady=10)

label2 = tk.Label(ventana, text="¡Contraseña!", font=("Arial", 20))
label2.pack(pady=20)
# Crear campo de texto - Entry2
entry2=tk.Entry(ventana,width=30)
entry2.pack(padx=10, pady=10)


# Botónes
btn = tk.Button(ventana, text="Ingresar")
btn.pack(pady=10)
btn2 = tk.Button(ventana, text="olvido la contraseña")
btn2.pack(pady=10)

ventana.mainloop()