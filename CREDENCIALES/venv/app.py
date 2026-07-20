import tkinter as tk
from dotenv import load_dotenv
import os

#Para caraga archivos desde nuestro env.

load_dotenv()

usuario_correcto = os.getenv("USER_NAME")

clave_correcta = os.getenv("USER_PASSWORD")

#Aqui comprobamos.

def verificar():
    if entry_user.get() == usuario_correcto and entry_password.get() == clave_correcta:
        mensaje.config(text="Acceso correcto")
    else:
        mensaje.config(text="Acceso incorrecto")
        
#Ventana

ventana = tk.Tk()
ventana.title("tarea de credenciales")
ventana.geometry("450x320")

#Aqui es donde vamos a escribir

tk.Label(ventana, text="").pack()

tk.Label(ventana, text="VALIDAR CREDENCIALES").pack()

tk.Label(ventana, text="").pack()

tk.Label(ventana, text="USUARIO").pack()

entry_user = tk.Entry(ventana)
entry_user.pack(pady=9)

tk.Label(ventana, text="CLAVE").pack()

entry_password = tk.Entry(ventana)
entry_password.pack(pady=9)

#Aqui botones y mensajes

tk.Button(ventana,text="Entrar",command = verificar).pack(pady=10)
mensaje = tk.Label(ventana, text="")
mensaje.pack()

#Aqui dejamos la ventana para que no se cierre

ventana.mainloop()

