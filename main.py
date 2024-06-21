# Certamen 3 - 30%
#Idea : crear un sistema de inventario/ventas de productos de computación. 
#Testeado en Windows - Linux


#librerias
import os
import sys
import time
import datetime
from colors import bcolors


#################################
#   #   #   variables   #   #   #
#################################

usuarios = {
    "admin" : {"usuario" : "admin", "contraseña": "admin", "uid": 0},
    "test": {"usuario" : "test", "contraseña": "test", "uid": 1},
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

hist_compras = {}

hist_ventas = {}

#################################
#   #   #   Funciones   #   #   #
#################################

#Registrar usuario
def register():
    print(bcolors.OKCYAN+"Registrarse en MyGamingSetup\n"+bcolors.ENDC)
    print("Para volver al menú principal, escriba 'Q'.")
    user = input(bcolors.WARNING+"Ingrese un nombre de usuario: "+bcolors.ENDC).lower()
    if user =="q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        main_manu()

    if user in usuarios:
        print(bcolors.FAIL+"El usuario ya existe.\n")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        register()

    elif len(user) < 5:
        print(bcolors.FAIL+"El nombre de usuario debe tener mínimo 5 carácteres.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        register()

    password = input(bcolors.WARNING+"Ingrese su contraseña: "+bcolors.ENDC)
    if password == "q" or password == "Q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        main_manu()

    if password == "":
        print(bcolors.FAIL+"La contraseña no puede estar vacía.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        register()

    elif len(password) < 8:
        print(bcolors.FAIL+"La contraseña debe tener mínimo 8 carácteres.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        register()

    else:
        usuarios[user] = {"usuario": user, "contraseña": password, "uid": len(usuarios) + 1}
        print(bcolors.OKGREEN+"\nUsuario registrado exitosamente.\n")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
    main_manu()

#Iniciar sesión
def login():
    global user
    print(bcolors.OKCYAN+"Iniciar sesión en MyGamingSetup\n"+bcolors.ENDC)
    print("Para volver al menú principal, escriba 'Q'.")
    user = input(bcolors.WARNING+"Ingrese un nombre de usuario: "+bcolors.ENDC)

    if user == "q" or user == "Q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        main_manu()

    password = input(bcolors.WARNING+"Ingrese su contraseña: "+bcolors.ENDC)
    if password == "q" or password == "Q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        main_manu()

    if user == "admin" and password == "admin":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()
            
    elif user in usuarios and usuarios[user]["contraseña"] == password:
        os.system("cls") if os.name == "nt" else os.system("clear")
        print(bcolors.OKCYAN+f"Hola, "+bcolors.HEADER+f"{user}!")
        menu_user()
    else:
        print(bcolors.FAIL+"\nUsuario o contraseña incorrectos.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        login()

#Ver productos disponibles
def ver_productos():
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Productos disponibles\n"+bcolors.ENDC)
    print("    ID\t|      Tipo\t  |\t\tNombre\t\t\t|      Precio\t |   Stock")
    print("-"*95)
    for k,v in productos.items():
        print(f"    {v['id']:<4}|  {v['tipo']:<15}| {v['nombre']:<36}|   ${v['precio']:<5} USD\t |    {v['stock']:<17}\n") #Ajustes de impresión para que se vea bonito
    print("-"*95 + "\n")


def ver_historial_compras():
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Historial de compras\n"+bcolors.ENDC)
    print("Usuario (id) |      Producto            |    Precio    | Cantidad  |   Total   |  Fecha")
    print("-"*95)
    if len(hist_compras) == 0:
        print(bcolors.HEADER+"No hay compras registradas."+bcolors.ENDC)
        print("-"*95 + "\n")
    for k,v in hist_compras.items():   
        print(f" {v['user']}  ({v['uid']})   | {v['producto']}     |    {v['precio']}     |     {v['cantidad']}     |   {v['total']}   | {v['fecha']}")
        print("-"*95 + "\n")
    os.system("pause")
    os.system("cls") if os.name == "nt" else os.system("clear")



def ver_historial_ventas():
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Historial de ventas\n"+bcolors.ENDC)
    print("    Usuario\t|    Producto\t\t\t|    Precio\t|    Cantidad\t|    Total\t|    Fecha")
    print("-"*115)
    for venta in hist_ventas:
        print(f"    {venta['usuario']:<10}|  {venta['producto']:<25}|  ${venta['precio']:<5} USD\t|  {venta['cantidad']:<10}|  ${venta['total']:<10} USD|  {venta['fecha']}")
    print("-"*115 + "\n")
    os.system("pause")


###########################################
#   #   Funciónes de administrador    #   #
###########################################
#Menú admin
def menu_admin():
    try:
        print(bcolors.OKCYAN+"Bienvenido/a al menú de administración"+bcolors.ENDC)
        print("1.- Ver productos disponibles")
        print("2.- Agregar producto")
        print("3.- Modificar producto")
        print("4.- ver historial de ventas")
        print("5.- Eliminar producto")
        print("6.- Salir de la cuenta")
        opcion = input(bcolors.WARNING+"Ingrese una opción: "+bcolors.ENDC)

        if opcion == "1":
            os.system("cls") if os.name == "nt" else os.system("clear")
            ver_productos()
            menu_admin()

        elif opcion == "2":
            os.system("cls") if os.name == "nt" else os.system("clear")
            ver_productos()
            agregar_producto()

        elif opcion == "3":
            os.system("cls") if os.name == "nt" else os.system("clear")
            ver_productos()
            modificar_producto()

        elif opcion == "4":
            os.system("cls") if os.name == "nt" else os.system("clear")
            ver_historial_ventas()
            menu_admin()

        elif opcion == "5":
            os.system("cls") if os.name == "nt" else os.system("clear")
            ver_productos()
            eliminar_producto()

        elif opcion == "6":
            os.system("cls") if os.name == "nt" else os.system("clear")
            main_manu()
        else:
            print(bcolors.FAIL+"\nERROR:"+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_admin()

    except ValueError:
        print(bcolors.FAIL+"\nERROR:"+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()
    except KeyboardInterrupt:
        print(bcolors.FAIL+"\nERROR:"+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()


#Agregar productos
def agregar_producto():
    ver_productos()
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Agregar productos\n"+bcolors.ENDC)

    nombre = input(bcolors.WARNING+"Ingrese el nombre del producto: "+bcolors.ENDC)
    if nombre == "": # Validar que el nombre no esté vacío
        print(bcolors.FAIL+"El nombre no puede estar vacío.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        
    elif nombre in productos: # Validar que el nombre no exista en el diccionario
        print(bcolors.FAIL+"El producto ya existe.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")


    precio = float(input(bcolors.WARNING+"Ingrese el precio del producto: "+bcolors.ENDC))
    if precio == "": # Validar que el precio no esté vacío
        print(bcolors.FAIL+"El precio no puede estar vacío.")
        os.system("cls") if os.name == "nt" else os.system("clear")
        

    stock = int(input(bcolors.WARNING+"Ingrese la cantidad de stock que se agregará al producto: "+bcolors.ENDC))
    if stock == "" or stock < 0: # Validar que el stock no esté vacío
        print(bcolors.FAIL+"El stock no puede estar vacío, ni ser negativo")
        os.system("cls") if os.name == "nt" else os.system("clear")


    tipo = input(bcolors.WARNING+"Ingrese el tipo de producto: "+bcolors.ENDC)
    if tipo == "": # Validar que el tipo no esté vacío
        print(bcolors.FAIL+"El tipo no puede estar vacío.")
        os.system("cls") if os.name == "nt" else os.system("clear")

    id = len(productos) + 1
    if id in productos: # Validar que el ID no exista en el diccionario
        id += 1
        
    productos[id] = {"id": id, "nombre": nombre, "precio": precio, "stock": stock, "tipo": tipo} # Agregar producto al diccionario
    print(bcolors.OKGREEN+"Producto agregado exitosamente.")
    time.sleep(1.5) 
    os.system("cls") if os.name == "nt" else os.system("clear")
    menu_admin()


def modificar_producto():
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Modificar producto\n"+bcolors.ENDC)
    ver_productos()
    id = input(bcolors.WARNING+"Ingrese el ID del producto que desea modificar: "+bcolors.ENDC)
    if id in productos:
        nombre = input(bcolors.WARNING+"Ingrese el nuevo nombre del producto: "+bcolors.ENDC)
        if nombre == "":
            nombre = productos[id]["nombre"]
        precio = float(input(bcolors.WARNING+"Ingrese el nuevo precio del producto: "+bcolors.ENDC))
        if precio == "":
            precio = productos[id]["precio"]
        stock = int(input(bcolors.WARNING+"Ingrese el nuevo stock del producto: "+bcolors.ENDC))
        if stock == "":
            stock = productos[id]["stock"]
        tipo = input(bcolors.WARNING+"Ingrese el nuevo tipo de producto: "+bcolors.ENDC)
        if tipo == "":
            tipo = productos[id]["tipo"]
        productos[id] = {"id": id, "nombre": nombre, "precio": precio, "stock": stock, "tipo": tipo}
        print(bcolors.OKGREEN+"Producto modificado exitosamente.")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()
    else:
        print(bcolors.FAIL+"El producto no existe.")


def eliminar_producto():
    ver_productos()
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Eliminar producto\n"+bcolors.ENDC)
    id = input(bcolors.WARNING+"Ingrese el ID del producto que desea eliminar: "+bcolors.ENDC)
    if id in productos:
        del productos[id]
        print(bcolors.OKGREEN+"Producto eliminado exitosamente.")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()
    else:
        print("El producto no existe")

#####################################
#   #   Funciónes de usuario    #   #
#####################################

#Menú usuario
def menu_user():
    try:
        print(bcolors.OKCYAN+"Bienvenido/a a MyGamingSetup\n"+bcolors.ENDC)
        print("1.- Ver productos disponibles") #Mostrar lista con productos
        print("2.- Comprar producto")          #Seleccionar producto y cantidad
        print("3.- Ver historial de compras")  #Mostrar historial de compras
        print("4.- Gestionar cuenta")          #Cambiar contraseña, borrar cuenta.
        print("5.- Salir de la cuenta")        #Salir de la cuenta
        opcion = input(bcolors.WARNING+"Ingrese una opción: "+bcolors.ENDC)

        if opcion == "1":
            os.system("cls") if os.name == "nt" else os.system("clear")
            ver_productos()
            menu_user()

        elif opcion == "2":
            os.system("cls") if os.name == "nt" else os.system("clear")
            comprar_producto()
            menu_user()

        elif opcion == "3":
            os.system("cls") if os.name == "nt" else os.system("clear")
            ver_historial_compras()
            menu_user()

        elif opcion == "4":
            os.system("cls") if os.name == "nt" else os.system("clear")
            gestionar_cuenta()

        elif opcion == "5":
            os.system("cls") if os.name == "nt" else os.system("clear")
            main_manu()

        else:
            print(bcolors.FAIL+"\nERROR:"+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_user()
    except ValueError:
        print(bcolors.FAIL+"\nERROR:"+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_user()
    except KeyboardInterrupt:
        print(bcolors.FAIL+"\nERROR:"+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_user()       
        
#opción 2 : Comprar productos
def comprar_producto():
    ver_productos()
    try:
        print(bcolors.OKCYAN+bcolors.UNDERLINE+"Comprar producto\n"+bcolors.ENDC)
        print("Para volver, ingrese 'Q'.")
        producto_comprar = input("Seleccione ID del producto: "+bcolors.ENDC)
        if producto_comprar == "":
            os.system("cls") if os.name == "nt" else os.system("clear")
            return
    except ValueError:
        print(bcolors.FAIL+"\nERROR:"+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        return
    except KeyboardInterrupt:
        print(bcolors.FAIL+"\nERROR:"+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        return 

    # Validamos la existencia del producto
    if producto_comprar not in productos:
        print(bcolors.FAIL+"El producto seleccionado no existe.")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
        return
    while True:
        try:
            cantidad = int(input(bcolors.WARNING+"Ingrese la cantidad: "+bcolors.ENDC))
            if cantidad <= 0:
                print(bcolors.FAIL+"Por favor, ingrese un número mayor a 0.")
                continue    # Vuelve al inicio del bucle while
            if productos[producto_comprar]["stock"] < cantidad:
                print(bcolors.FAIL+"Lo sentimos, no hay suficiente stock del producto seleccionado.\n")
                time.sleep(1.5)
                os.system("cls") if os.name == "nt" else os.system("clear")
                comprar_producto()
            else:
                productos[producto_comprar]["stock"] -= cantidad
                print(bcolors.OKGREEN+"Total a pagar:"+bcolors.ENDC+f"${productos[producto_comprar]['precio']*cantidad} USD")
                #agregar al historial de compras
                hist_ventas[producto_comprar] = {"user": user, "uid": usuarios[user]["uid"], "producto": productos[producto_comprar]["nombre"], "precio": productos[producto_comprar]["precio"], "cantidad": cantidad, "total": productos[producto_comprar]["precio"]*cantidad, "fecha": datetime.datetime.now()}
                os.system("pause")
                os.system("cls") if os.name == "nt" else os.system("clear")
                break  # Salir del bucle si la compra es exitosa
        except ValueError:
            print(bcolors.FAIL+"ERROR:"+bcolors.ENDC+"Por favor, ingrese un número válido.")
        except KeyboardInterrupt:
            print(bcolors.FAIL+"ERROR:"+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
    

def gestionar_cuenta():
    global user
    try:
        print(bcolors.OKCYAN+bcolors.UNDERLINE+"Gestionar cuenta"+bcolors.ENDC)
        print("1.- Cambiar contraseña")
        print("2.- Borrar cuenta")
        print("3.- Volver al menú principal")
        opcion = input(bcolors.WARNING+"Ingrese una opción: "+bcolors.ENDC)
        if opcion == "1":
            os.system("cls") if os.name == "nt" else os.system("clear")
            cambiar_contraseña()

        elif opcion == "2": #borrar cuenta del usuario en sesion iniciada
            del usuarios[user]
            print(bcolors.OKGREEN+"Cuenta eliminada exitosamente.")
            time.sleep(1.5)
            os.system("cls") if os.name == "nt" else os.system("clear")
            main_manu()

        elif opcion == "3":
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_user()
    except ValueError:
        print(bcolors.FAIL+"\nERROR:"+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        gestionar_cuenta()
    except KeyboardInterrupt:
        print(bcolors.FAIL+"\nERROR:"+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        gestionar_cuenta()

def cambiar_contraseña():
    global user          
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Cambiar ontraseña\n"+bcolors.ENDC)
    newpass = input(bcolors.WARNING+"Ingrese su nueva contraseña: "+bcolors.ENDC)
    #La contraseña no puede ser igual a la anterior
    if newpass == usuarios:
        print(bcolors.FAIL+"La contraseña no puede ser igual a la anterior.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        cambiar_contraseña()
    #La contraseña no puede estar vacía
    elif newpass == "":
        print(bcolors.FAIL+"La contraseña no puede estar vacía.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        cambiar_contraseña()
    #la contraseña debe tener mínimo 8 carácteres
    elif len(newpass) < 8:
        print(bcolors.FAIL+"La contraseña debe tener mínimo 8 carácteres.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        cambiar_contraseña()

    usuarios[user]["contraseña"] = newpass
    print(bcolors.OKGREEN+"Contraseña cambiada exitosamente.")
    time.sleep(1.5)
    os.system("cls") if os.name == "nt" else os.system("clear")
    menu_user()

######################################
#   #   #   Menu principal   #   #   #
######################################
def main_manu():
    os.system("cls") if os.name == "nt" else os.system("clear")
    try: #aplicamos el try para evitar errores en el programa
        print(bcolors.OKCYAN+"Bienvenido/a a MyGamingSetup"+bcolors.ENDC)
        print(bcolors.OKGREEN+"*Para poder acceder a nuestro catálogo de productos, porfavor "+bcolors.WARNING+bcolors.UNDERLINE+"registate"+bcolors.ENDC+" o "+bcolors.WARNING+bcolors.UNDERLINE+"inicia sesión.\n"+bcolors.ENDC)
        print("1.-Registrate")
        print("2.-Iniciar Sesión")
        print("3.-Salir del programa")
        opcion = input(bcolors.WARNING+"Ingrese una opción: "+bcolors.ENDC)

        if opcion == "1":
            os.system("cls") if os.name == "nt" else os.system("clear")
            register()
        elif opcion == "2":
            os.system("cls") if os.name == "nt" else os.system("clear")
            login()
        elif opcion == "3":
            os.system("cls") if os.name == "nt" else os.system("clear")
            sys.exit(bcolors.OKBLUE+"""
                     
                              .,
                    .      _,'f----.._
                    |\ ,-'"/  |     ,'
                    |,_  ,--.      /
                    /,-. ,'`.     (_               """+bcolors.OKCYAN+"""MyGamingSetup"""+bcolors.OKBLUE+"""
                    f  o|  o|__     "`-.   """+bcolors.ENDC+"""~   Nos vemos pronto crack! """+bcolors.ENDC+ bcolors.OKBLUE+"""
                    ,-._.,--'_ `.   _.,-`
                    `"' ___.,'` j,-'
                      `-.__.,--'
                     

                     """+bcolors.ENDC)
        else:
            print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            main_manu() #se vuelve a llamar a la funcion para que el usuario pueda ingresar una opcion valida

    except ValueError: #si el usuario ingresa un valor no valido, se ejecutara el siguiente mensaje
        print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        main_manu() #se vuelve a llamar a la funcion para que el usuario pueda ingresar una opcion valida
    except KeyboardInterrupt:
        print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        main_manu()

os.system("cls") if os.name == "nt" else os.system("clear")
main_manu() #llamamos a la funcion para que se ejecute el programa