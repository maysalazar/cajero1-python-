# Cajero Automático en Python con Tkinter
# Este programa simula un cajero automático con interfaz gráfica usando Tkinter.
# Permite iniciar sesión, consultar saldo, retirar y depositar dinero.

import tkinter as tk
from tkinter import messagebox

# Datos de usuario predefinidos
usuario_correcto = "admin"
contrasena_correcta = "1234"
saldo = 1000

def iniciar_sesion():
    global usuario_entry, contrasena_entry, ventana_login
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()
    
    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        ventana_login.destroy()
        mostrar_menu()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def consultar_saldo():
    messagebox.showinfo("Saldo", f"Su saldo actual es: ${saldo}")

def retirar_dinero():
    global saldo
    monto = simpledialog.askinteger("Retirar", "Ingrese el monto a retirar:")
    if monto is None:
        return
    if monto > saldo:
        messagebox.showerror("Error", "Fondos insuficientes.")
    else:
        saldo -= monto
        messagebox.showinfo("Éxito", f"Retiro exitoso. Nuevo saldo: ${saldo}")

def depositar_dinero():
    global saldo
    monto = simpledialog.askinteger("Depositar", "Ingrese el monto a depositar:")
    if monto is None:
        return
    saldo += monto
    messagebox.showinfo("Éxito", f"Depósito exitoso. Nuevo saldo: ${saldo}")

def mostrar_menu():
    ventana_menu = tk.Tk()
    ventana_menu.title("Cajero Automático")
    
    tk.Label(ventana_menu, text="Seleccione una opción").pack()
    tk.Button(ventana_menu, text="Consultar saldo", command=consultar_saldo).pack()
    tk.Button(ventana_menu, text="Retirar dinero", command=retirar_dinero).pack()
    tk.Button(ventana_menu, text="Depositar dinero", command=depositar_dinero).pack()
    tk.Button(ventana_menu, text="Salir", command=ventana_menu.destroy).pack()
    
    ventana_menu.mainloop()

# Ventana de inicio de sesión
ventana_login = tk.Tk()
ventana_login.title("Inicio de Sesión")

tk.Label(ventana_login, text="Usuario:").pack()
usuario_entry = tk.Entry(ventana_login)
usuario_entry.pack()

tk.Label(ventana_login, text="Contraseña:").pack()
contrasena_entry = tk.Entry(ventana_login, show="*")
contrasena_entry.pack()

tk.Button(ventana_login, text="Iniciar Sesión", command=iniciar_sesion).pack()

ventana_login.mainloop()