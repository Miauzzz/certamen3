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
    "1" : {"id":1,  "nombre" : "Monitor - Azuls VG24",         "precio" : 125.00,    "stock" : 10,   "tipo": "monitor"},
    "2" : {"id":2,  "nombre" : "Teclado - Jayperex FPS",       "precio" : 60.00,     "stock" : 10,   "tipo": "teclado"},
    "3" : {"id":3,  "nombre" : "Mouse - Jayperex Surge",       "precio" : 30.00,     "stock" : 10,   "tipo": "mouse"},
    "4" : {"id":4,  "nombre" : "CPU - kore y9-1",              "precio" : 150.00,    "stock" : 30,   "tipo": "cpu"},
    "5" : {"id":5,  "nombre" : "Tarjeta de video - RTK 4100",  "precio" : 300.00,    "stock" : 23,   "tipo": "gpu"},
    "6" : {"id":6,  "nombre" : "RAM - Cruzar Valistic",        "precio" : 20.00,     "stock" : 4,    "tipo": "ram"},
    "7" : {"id":7,  "nombre" : "Gabinete - MSY m315",          "precio" : 45.00,     "stock" : 1,    "tipo": "gabinete"},
    "8" : {"id":8,  "nombre" : "Placa - Yigabait h312-v",      "precio" : 43.00,     "stock" : 30,   "tipo": "placa"},
}

historial_compras = []



#################################
#   #   #   Funciones   #   #   #
#################################
        #   Globales    #

#Registrar usuario
def register():
    print("Registrate\n")
    user = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    if user in usuarios:
        print("El usuario ya existe.")
    else:
        usuarios[user] = {"usuario": user, "contraseña": password}
        print("Usuario registrado exitosamente.")
        
    main_manu()

#Iniciar sesión
def login():
    print("Iniciar sesión\n")
    user = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    if user in usuarios and usuarios[user]["contraseña"] == password:
        os.system("cls")
        print(f"Hola {user}!")
        menu_user() 
    else:
        print("Usuario o contraseña incorrectos.")
        


def ver_productos():
    print("Seleccionar: |   Tipo   |\t\t    Nombre    \t\t|\t   Precio  \t |  Stock")
    print("-"*102)
    for k,v in productos.items():
        print(f"    {v['id']:<4}     | {v['tipo']:<8} | {v['nombre']:<35}   |\t${v['precio']:<10}USD\t |    {v['stock']:<17}\n") #Ajustes de impresión para que se vea bonito
    print("-"*102)



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
        os.system("cls")
        ver_productos()
        

    elif opcion == "2":
        agregar_producto()
        ver_productos()

    elif opcion == "3":
        #modificar_producto()
        pass
    elif opcion == "4":
        #eliminar_producto()
        pass
    elif opcion == "5":
        main_manu()


#Agregar productos
def agregar_producto():
    print("Agregar productos\n")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    tipo = input("Ingrese el tipo de producto: ")
    id = len(productos) + 1
    productos[str(id)] = {"id": id, "nombre": nombre, "precio": precio, "stock": stock, "tipo": tipo}
    print("Producto agregado exitosamente.")

def eliminar_producto():
    print("Eliminar producto\n")
    ver_productos()
    id = input("Ingrese el ID del producto que desea eliminar: ")
    if id in productos:
        del productos[id]
        print("Producto eliminado exitosamente.")
    else:
        print("El producto no existe.")

#####################################
#   #   Funciónes de usuario    #   #
#####################################

#Menú usuario
def menu_user():
    os.system("cls")
    print("Bienvenido/a a MyGamingSetup")
    print("1.- Ver productos disponibles") #Mostrar lista con productos
    print("2.- Comprar producto")          #Seleccionar producto y cantidad
    print("3.- Gestionar cuenta")          #Cambiar contraseña, borrar cuenta.
    print("4.- Salir de la cuenta")        #Salir de la cuenta
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        os.system("cls")
        ver_productos()
        menu_user()

    elif opcion == "2":
        comprar_producto()
        menu_user()

    elif opcion == "3":
        gestionar_cuenta()

    elif opcion == "4":
        main_manu()

#opción 2 : Comprar productos
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

def gestionar_cuenta():
    print("Gestionar cuenta")
    print("1.- Cambiar contraseña")
    print("2.- Borrar cuenta")
    print("3.- Volver al menú principal")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        #cambiar_contraseña()
        pass
    elif opcion == "2":
        pass
    elif opcion == "3":
        menu_user()

def cambiar_contraseña():
    global user #definimos la variable user como global
    print("Cambio de contraseña\n")
    nueva_contraseña = input("Ingrese su nueva contraseña: ")
    usuarios[user]["contraseña"] = nueva_contraseña
    print("Contraseña cambiada exitosamente.")

######################################
#   #   #   Menu principal   #   #   #
######################################
def main_manu():
    try: #aplicamos el try para evitar errores en el programa
        print("Bienvenido/a a MyGamingSetup\n")
        print("1.-Registrate")
        print("2.-Iniciar Sesión")
        print("3.-Salir del programa")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            os.system("cls")
            register()
        elif opcion == "2":
            os.system("cls")
            login()
        elif opcion == "3":
            os.system("cls")
            sys.exit("""
                     
                              .,
                    .      _,'f----.._
                    |\ ,-'"/  |     ,'
                    |,_  ,--.      /
                    /,-. ,'`.     (_
                    f  o|  o|__     "`-.    ~   Nos vemos pronto crack!
                    ,-._.,--'_ `.   _.,-`
                    `"' ___.,'` j,-'
                      `-.__.,--'
                     
""")

    except ValueError: #si el usuario ingresa un valor no valido, se ejecutara el siguiente mensaje
        print("ERROR: porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(2)
        os.system("cls")
        main_manu() #se vuelve a llamar a la funcion para que el usuario pueda ingresar una opcion valida

main_manu() #llamamos a la funcion para que se ejecute el programa