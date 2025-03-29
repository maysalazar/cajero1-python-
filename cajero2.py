# Cajero Automático en Python con Sistema de Logueo
# Este programa simula un cajero automático básico que permite al usuario:
# 1. Iniciar sesión con un usuario y contraseña predefinidos.
# 2. Consultar su saldo actual.
# 3. Retirar dinero de su cuenta.
# 4. Depositar dinero en su cuenta.
# 5. Salir del programa.
# 
# El programa usa solo variables y estructuras de control if-elif-else para la lógica de decisiones.

# Datos de usuario predefinidos
usuario_correcto = "admin"
contrasena_correcta = "1234"

# Solicitar credenciales al usuario
usuario = input("Ingrese su usuario: ")
contrasena = input("Ingrese su contraseña: ")

# Verificar credenciales
if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Inicio de sesión exitoso. Bienvenido al Cajero Automático.")
    
    saldo = 1000  # Saldo inicial del usuario
    
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        print(f"Su saldo actual es: ${saldo}")
    elif opcion == 2:
        retiro = int(input("Ingrese el monto a retirar: "))
        if retiro > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= retiro
            print(f"Retiro exitoso. Su nuevo saldo es: ${saldo}")
    elif opcion == 3:
        deposito = int(input("Ingrese el monto a depositar: "))
        saldo += deposito
        print(f"Depósito exitoso. Su nuevo saldo es: ${saldo}")
    elif opcion == 4:
        print("Gracias por usar el cajero automático.")
    else:
        print("Opción no válida. Intente de nuevo.")
else:
    print("Usuario o contraseña incorrectos. Acceso denegado.")