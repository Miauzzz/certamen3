# Certamen 3 - 30%
#Idea : crear un sistema de inventario/ventas de productos de computación. 

#librerias
import os
import sys
import time
import datetime

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
    print("Registrarse en MyGamingSetup\n")
    user = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")

    if user in usuarios:
        print("El usuario ya existe.\n")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")

    elif len(user) < 5:
        print("El nombre de usuario debe tener mínimo 5 carácteres.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        register()

    if password == "":
        print("La contraseña no puede estar vacía.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        register()

    elif len(password) < 8:
        print("La contraseña debe tener mínimo 8 carácteres.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        register()

    else:
        usuarios[user] = {"usuario": user, "contraseña": password}
        print("\nUsuario registrado exitosamente.\n")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
    main_manu()

#Iniciar sesión
def login():
    global user
    print("Iniciar sesión en MyGamingSetup\n")
    user = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    if user == "admin" and password == "admin":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()
            
    elif user in usuarios and usuarios[user]["contraseña"] == password:
        os.system("cls") if os.name == "nt" else os.system("clear")
        print(f"Hola, {user}!")
        menu_user()
    else:
        print("\nUsuario o contraseña incorrectos.")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
        main_manu()

#Ver productos disponibles
def ver_productos():
    print("    ID\t|      Tipo\t  |\t\tNombre\t\t\t|      Precio\t |   Stock")
    print("-"*95)
    for k,v in productos.items():
        print(f"    {v['id']:<4}|  {v['tipo']:<15}| {v['nombre']:<36}|   ${v['precio']:<5} USD\t |    {v['stock']:<17}\n") #Ajustes de impresión para que se vea bonito
    print("-"*95 + "\n")




###########################################
#   #   Funciónes de administrador    #   #
###########################################
#Menú admin
def menu_admin():
    try:
        print("Bienvenido/a al menú de administración")
        print("1.- Ver productos disponibles")
        print("2.- Agregar producto")
        print("3.- Modificar producto")
        print("4.- Eliminar producto")
        print("5.- Salir de la cuenta")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            os.system("cls") if os.name == "nt" else os.system("clear")
            ver_productos()
            menu_admin()

        elif opcion == "2":
            agregar_producto()
            ver_productos()

        elif opcion == "3":
            os.system("cls") if os.name == "nt" else os.system("clear")
            modificar_producto()

        elif opcion == "4":
            #eliminar_producto()
            pass
        elif opcion == "5":
            os.system("cls") if os.name == "nt" else os.system("clear")
            main_manu()
        else:
            print("ERROR: porfavor, ingrese una de las opciones en pantalla.")
            time.sleep(2)
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_admin()

    except ValueError:
        print("ERROR: porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(2)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()


#Agregar productos
def agregar_producto():
    print("Agregar productos\n")
    nombre = input("Ingrese el nombre del producto: ")       
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    tipo = input("Ingrese el tipo de producto: ")
    id = len(productos) + 1                                                                      # ID único y autoincremental (longitud del diccionario + 1) 
    productos[id] = {"id": id, "nombre": nombre, "precio": precio, "stock": stock, "tipo": tipo} # Agregar producto al diccionario
    print("Producto agregado exitosamente.")
    time.sleep(2) 
    os.system("cls") if os.name == "nt" else os.system("clear")
    menu_admin()


def modificar_producto():
    ver_productos()
    print("Modificar producto\n")
    id = input("Ingrese el ID del producto que desea modificar: ")
    if id in productos:
        nombre = input("Ingrese el nuevo nombre del producto: ")
        if nombre == "":
            nombre = productos[id]["nombre"]
        precio = float(input("Ingrese el nuevo precio del producto: "))
        if precio == "":
            precio = productos[id]["precio"]
        stock = int(input("Ingrese el nuevo stock del producto: "))
        if stock == "":
            stock = productos[id]["stock"]
        tipo = input("Ingrese el nuevo tipo de producto: ")
        if tipo == "":
            tipo = productos[id]["tipo"]
        productos[id] = {"id": id, "nombre": nombre, "precio": precio, "stock": stock, "tipo": tipo}
        print("Producto modificado exitosamente.")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()
    else:
        print("El producto no existe.")


def eliminar_producto():
    print("Eliminar producto\n")
    ver_productos()
    id = input("Ingrese el ID del producto que desea eliminar: ")
    if id in productos:
        del productos[id]
        print("Producto eliminado exitosamente.")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()
    else:
        print("El producto no existe.")

#####################################
#   #   Funciónes de usuario    #   #
#####################################

#Menú usuario
def menu_user():
    try:
        print("Bienvenido/a a MyGamingSetup\n")
        print("1.- Ver productos disponibles") #Mostrar lista con productos
        print("2.- Comprar producto")          #Seleccionar producto y cantidad
        print("3.- Gestionar cuenta")          #Cambiar contraseña, borrar cuenta.
        print("4.- Salir de la cuenta")        #Salir de la cuenta
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            os.system("cls") if os.name == "nt" else os.system("clear")
            ver_productos()
            menu_user()

        elif opcion == "2":
            comprar_producto()
            menu_user()

        elif opcion == "3":
            os.system("cls") if os.name == "nt" else os.system("clear")
            gestionar_cuenta()

        elif opcion == "4":
            main_manu()

        else:
            print("ERROR: porfavor, ingrese una de las opciones en pantalla.")
            time.sleep(2)
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_user()
    except ValueError:
        print("ERROR: porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(2)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_user()
        
#opción 2 : Comprar productos
def comprar_producto():
    producto_comprar = input("\nSeleccione ID del producto: ")

    # Validamos la existencia del producto
    if producto_comprar not in productos:
        print("El producto seleccionado no existe.")
        return # Salir de la función si el producto no existe en el inventario

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad <= 0:
                print("Por favor, ingrese un número mayor a 0.")
                continue    # Vuelve al inicio del bucle while
            if productos[producto_comprar]["stock"] < cantidad:
                print("Lo sentimos, no hay suficiente stock del producto seleccionado.\n")
            else:
                productos[producto_comprar]["stock"] -= cantidad
                print(f"Total a pagar: ${productos[producto_comprar]['precio']*cantidad} USD")
                os.system("pause")
                os.system("cls") if os.name == "nt" else os.system("clear")
                break  # Salir del bucle si la compra es exitosa
        except ValueError:
            print("Por favor, ingrese un número válido.")

def gestionar_cuenta():
    global user
    try:
        print("Gestionar cuenta")
        print("1.- Cambiar contraseña")
        print("2.- Borrar cuenta")
        print("3.- Volver al menú principal")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            cambiar_contraseña()

        elif opcion == "2": #borrar cuenta del usuario en sesion iniciada
            del usuarios[user]
            print("Cuenta eliminada exitosamente.")
            time.sleep(2)
            os.system("cls") if os.name == "nt" else os.system("clear")
            main_manu()

        elif opcion == "3":
            menu_user()
    except ValueError:
        print("ERROR: porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(2)
        os.system("cls") if os.name == "nt" else os.system("clear")
        gestionar_cuenta()

def cambiar_contraseña():
    global user          
    print("Cambio de contraseña\n")
    newpass = input("Ingrese su nueva contraseña: ")
    #La contraseña no puede ser igual a la anterior
    if newpass == usuarios:
        print("La contraseña no puede ser igual a la anterior.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        cambiar_contraseña()
    #La contraseña no puede estar vacía
    elif newpass == "":
        print("La contraseña no puede estar vacía.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        cambiar_contraseña()
    #la contraseña debe tener mínimo 8 carácteres
    elif len(newpass) < 8:
        print("La contraseña debe tener mínimo 8 carácteres.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        cambiar_contraseña()

    usuarios[user]["contraseña"] = newpass
    print("Contraseña cambiada exitosamente.")
    os.system("pause")
    os.system("cls") if os.name == "nt" else os.system("clear")
    menu_user()

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
            os.system("cls") if os.name == "nt" else os.system("clear")
            register()
        elif opcion == "2":
            os.system("cls") if os.name == "nt" else os.system("clear")
            login()
        elif opcion == "3":
            os.system("cls") if os.name == "nt" else os.system("clear")
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
        else:
            print("ERROR: porfavor, ingrese una de las opciones en pantalla.")
            time.sleep(2)
            os.system("cls") if os.name == "nt" else os.system("clear")
            main_manu() #se vuelve a llamar a la funcion para que el usuario pueda ingresar una opcion valida

    except ValueError: #si el usuario ingresa un valor no valido, se ejecutara el siguiente mensaje
        print("ERROR: porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(2)
        os.system("cls") if os.name == "nt" else os.system("clear")
        main_manu() #se vuelve a llamar a la funcion para que el usuario pueda ingresar una opcion valida

os.system("cls") if os.name == "nt" else os.system("clear")
main_manu() #llamamos a la funcion para que se ejecute el programa