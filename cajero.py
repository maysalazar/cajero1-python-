# Cajero automático en Python usando solo variables e if-elif-else

saldo = 1000  # Saldo inicial del usuario

print("Bienvenido al Cajero Automático")
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
1
