# Usuario.py
# Gestion de los datos del usuario dividendo al saldo

import time   # simula el tiempo 
import math   # libreria matematicas

# TIPOS DE CUENTA DISPONIBLES_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# Diccionario que guarda los tipos de cuenta y el porcentaje del dividendo.

tipos_de_cuenta = {
    
    "joven": 0.002,
    
    "jubilado": 0.002,
    
    "empresa": 0.002,
    
    "ong": 0.002
}

# DATOS DEL USUARIO_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# Pedimos el nombre del usuario.

nombre = input("Escribe tu nombre: ")

# Mostramos los tipos de cuenta.

print("Tipos de cuenta disponibles: joven, jubilado, empresa, ong")

# Pedimos el tipo de cuenta.

tipo = input("Eligue tu tipo de cuenta: ")

# Si el tipo no existe, usamos uno por defecto.

if tipo not in tipos_de_cuenta:
    
    print("Tipo de cuenta no válido. Se usará 'joven'.")
    
    tipo = "joven"

# SALDO INICIAL_ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# El saldo inicial siempre empieza en 100 euros

saldo = 100.0

print("Tu saldo inicial es de 100 €.")

# DIVIDENDO_ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# El dividendo según el tipo de cuenta.

dividendo = tipos_de_cuenta[tipo]

print("Cada 5 segundos se aplicará un dividendo del 0.2%.")

# APLICACIÓN DEL DIVIDENDO_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# Este bucle se limita a 5 repeticiones para evitar un bucle infinito.

for i in range(5):

    # Esperamos 5 segundos
    
    time.sleep(5)

    # Calculamos el incremento del saldo
    
    incremento = saldo * dividendo

    # Redondeamos el incremento a 2 decimales
    
    incremento = round(incremento, 2)

    # Sumamos el incremento al saldo
    
    saldo = saldo + incremento

    # Mostramos la información por pantalla
    
    print("\n DIVIDENDO APLICADO 
    
    print("Usuario:", nombre)
          
    print("Tipo de cuenta:", tipo)
          
    print("Dividendo recibido:", incremento, "€")
          
    print("Saldo actualizado:", saldo, "€")
          
    print("------------------------------")
