# Cajero Automático en Python con Tkinter mejorado
# Este programa simula un cajero automático con interfaz gráfica usando Tkinter.
# Permite iniciar sesión, consultar saldo, retirar y depositar dinero sin problemas.

import tkinter as tk
from tkinter import messagebox, simpledialog

# Datos de usuario predefinidos
usuario_correcto = "admin"
contrasena_correcta = "1234"
saldo = 1000

def iniciar_sesion():
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
    try:
        monto = simpledialog.askinteger("Retirar", "Ingrese el monto a retirar:")
        if monto is None:
            return
        if monto <= 0:
            messagebox.showerror("Error", "Ingrese un monto válido.")
        elif monto > saldo:
            messagebox.showerror("Error", "Fondos insuficientes.")
        else:
            saldo -= monto
            messagebox.showinfo("\u00c9xito", f"Retiro exitoso. Nuevo saldo: ${saldo}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor numérico válido.")

def depositar_dinero():
    global saldo
    try:
        monto = simpledialog.askinteger("Depositar", "Ingrese el monto a depositar:")
        if monto is None:
            return
        if monto <= 0:
            messagebox.showerror("Error", "Ingrese un monto válido.")
        else:
            saldo += monto
            messagebox.showinfo("\u00c9xito", f"Depósito exitoso. Nuevo saldo: ${saldo}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor numérico válido.")

def mostrar_menu():
    ventana_menu = tk.Tk()
    ventana_menu.title("Cajero Automático")
    ventana_menu.geometry("300x250")
    
    tk.Label(ventana_menu, text="Seleccione una opción", font=("Arial", 12)).pack(pady=10)
    tk.Button(ventana_menu, text="Consultar saldo", command=consultar_saldo, width=20).pack(pady=5)
    tk.Button(ventana_menu, text="Retirar dinero", command=retirar_dinero, width=20).pack(pady=5)
    tk.Button(ventana_menu, text="Depositar dinero", command=depositar_dinero, width=20).pack(pady=5)
    tk.Button(ventana_menu, text="Salir", command=ventana_menu.destroy, width=20, bg="red", fg="white").pack(pady=5)
    
    ventana_menu.mainloop()

# Ventana de inicio de sesión
ventana_login = tk.Tk()
ventana_login.title("Inicio de Sesión")
ventana_login.geometry("300x200")

tk.Label(ventana_login, text="Usuario:").pack(pady=5)
usuario_entry = tk.Entry(ventana_login)
usuario_entry.pack(pady=5)

tk.Label(ventana_login, text="Contraseña:").pack(pady=5)
contrasena_entry = tk.Entry(ventana_login, show="*")
contrasena_entry.pack(pady=5)

tk.Button(ventana_login, text="Iniciar Sesión", command=iniciar_sesion, width=20).pack(pady=10)

ventana_login.mainloop()