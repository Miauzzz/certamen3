# Certamen 3 - 30%
#Idea Crear inventario tipo PC factory

#librerias
import os
import sys
import time
import datetime
import string

#################################
#   #   #   variables   #   #   #
#################################

usuarios = {
    "admin" : {"usuario" : "admin", "contraseña": "admin"},
}

productos = {
    "monitor01" : {"nombre" : "Monitor - Azuls VG24",         "precio" : 125.00,    "stock" : 10,   "tipo": "monitor"},
    "teclado01" : {"nombre" : "Teclado - Jayperex FPS",       "precio" : 60.00,     "stock" : 10,   "tipo": "teclado"},
    "mouse01"   : {"nombre" : "Mouse - Jayperex Surge",       "precio" : 30.00,     "stock" : 10,   "tipo": "mouse"},
    "cpu01"     : {"nombre" : "CPU - kore y9-1",              "precio" : 150.00,    "stock" : 30,   "tipo": "cpu"},
    "gpu01"     : {"nombre" : "Tarjeta de video - RTK 4100",  "precio" : 300.00,    "stock" : 23,   "tipo": "gpu"},
    "ram01"     : {"nombre" : "RAM - Cruzar Valistic",        "precio" : 20.00,     "stock" : 4,    "tipo": "ram"},
    "gabinete01": {"nombre" : "Gabinete - MSY m315",          "precio" : 45.00,     "stock" : 1,    "tipo": "gabinete"},
    "placa01"   : {"nombre" : "Placa - Yigabait h312-v",      "precio" : 43.00,     "stock" : 30,   "tipo": "placa"},
}


#################################
#   #   #   Funciones   #   #   #
#################################
        #   Globales    #

#Registrar usuario
def register():
    print("Registrate\n")
    user = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    usuarios[user] = {"usuario": user, "contraseña": password, "id": len(usuarios)}
    print("Usuario registrado exitosamente.")


#Iniciar sesión
def login():
    print("Iniciar sesión\n")
    user = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    if user in usuarios and usuarios[user]["contraseña"] == password:
        print(f"Bienvenido, {user}!")
    else:
        print("Usuario o contraseña incorrectos.")

        
def ver_productos():
    print("   Tipo   |\t\t    Nombre    \t\t|\t   Precio  \t |  Stock")
    print("-"*85)
    for k,v in productos.items():
        print(f"{v['tipo']:<9} | {v['nombre']:<35} |\t${v['precio']:<10}USD\t |    {v['stock']:<17}")




###########################################
#   #   Funciónes de administrador    #   #
###########################################
#Menú admin
def menu_admin():
    print("Bienvenido/a al menú de administración")
    print("1.- Ver productos disponibles")
    print("2.- Agregar producto")
    print("3.- Modificar producto")
    print("4.- Eliminar producto")
    print("5.- Salir de la cuenta")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        ver_productos()

    elif opcion == "2":
        #agregar_producto()
        pass
    elif opcion == "3":
        #modificar_producto()
        pass
    elif opcion == "4":
        #eliminar_producto()
        pass
    elif opcion == "5":
        main_manu()


#####################################
#   #   Funciónes de usuario    #   #
#####################################

#Menú usuario
def menu_user():
    print("Bienvenido/a a MyGamingSetup")
    print("1.- Ver productos disponibles") #Mostrar lista con productos
    print("2.- Comprar producto")          #Seleccionar producto y cantidad
    print("3.- Gestionar cuenta")          #Cambiar contraseña, borrar cuenta.
    print("4.- Salir de la cuenta")        #Salir de la cuenta
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        ver_productos()
        
    elif opcion == "2":
        #comprar_producto()
        pass
    elif opcion == "3":
        #gestionar_cuenta()
        pass
    elif opcion == "4":
        main_manu()


def comprar_producto():
    producto_comprar = input("\nSeleccione un producto: ")
    
    # Validamos la existencia del producto
    if producto_comprar not in productos:
        print("El producto seleccionado no existe.")
        return # Salir de la función si el producto no existe en el inventario
    
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad <= 0:
                print("Por favor, ingrese un número mayor a 0.")
                continue
            if productos[producto_comprar]["stock"] < cantidad:
                print("Lo sentimos, no hay suficiente stock del producto seleccionado.")
            else:
                productos[producto_comprar]["stock"] -= cantidad
                print(f"Total a pagar: ${productos[producto_comprar]['precio']*cantidad} USD")
                break  # Salir del bucle si la compra es exitosa
        except ValueError:
            print("Por favor, ingrese un número válido.")
    



######################################
#   #   #   Menu principal   #   #   #
######################################
def main_manu():
    try:
        print("Bienvenido")
        print("1.Registrarse-")
        print("2.-Iniciar Sesión")
        print("3.-Salir del programa")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            register()
        elif opcion == "2":
            login()
        elif opcion == "3":
            sys.exit("Gracias por visitarnos, nos vemos pronto!")

    except ValueError:
        print("ERROR: porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(2)
        os.system("cls")
        main_manu()
