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
    "1" : {"id":1,  "nombre" : "AZULS - VG24",           "precio" : 125.00,    "stock" : 10,   "tipo": "MONITOR"},
    "2" : {"id":2,  "nombre" : "JAYPEREX - FPS",         "precio" : 60.00,     "stock" : 10,   "tipo": "TECLADO"},
    "3" : {"id":3,  "nombre" : "JAYPEREX - SURGE",       "precio" : 30.00,     "stock" : 10,   "tipo": "MOUSE"},
    "4" : {"id":4,  "nombre" : "INTREL - CORE Y9-20",    "precio" : 150.00,    "stock" : 30,   "tipo": "CPU"},
    "5" : {"id":5,  "nombre" : "NTIVIA - RTK - 4100",    "precio" : 300.00,    "stock" : 23,   "tipo": "GPU"},
    "6" : {"id":6,  "nombre" : "CRUZIAL - VALISTIC",     "precio" : 20.00,     "stock" : 4,    "tipo": "RAM"},
    "7" : {"id":7,  "nombre" : "MSY - M315",             "precio" : 45.00,     "stock" : 1,    "tipo": "GABINETE"},
    "8" : {"id":8,  "nombre" : "YIGABAIT - H312-V",      "precio" : 43.00,     "stock" : 30,   "tipo": "PLACA"},
}

#Historial de compras que visualiza el usuario (cada usuario tiene su propio historial)
hist_compras = {}

#Historial que visualiza el admin (todas las ventas)
hist_ventas = {}

#################################
#   #   #   Funciones   #   #   #
#################################

#Registrar usuario
def register():
    try:
        print(bcolors.OKCYAN+"Registrarse en MyGamingSetup\n"+bcolors.ENDC)
        print("Para volver al menú principal, escriba 'Q'.")
        user = input(bcolors.WARNING+"Ingrese un nombre de usuario: "+bcolors.ENDC).lower()
        if user =="q":
            os.system("cls") if os.name == "nt" else os.system("clear")
            main_menu()

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
            main_menu()

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
            main_menu()

    except ValueError: #si el usuario ingresa un valor no valido, se ejecutara el siguiente mensaje
        print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        register()
        
    except KeyboardInterrupt:
        print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        register()

    main_menu()

#Iniciar sesión
def login():
    try:
        global user
        print(bcolors.OKCYAN+"Iniciar sesión en MyGamingSetup\n"+bcolors.ENDC)
        print("Para volver al menú principal, escriba 'Q'.")
        user = input(bcolors.WARNING+"Ingrese un nombre de usuario: "+bcolors.ENDC)

        if user == "q" or user == "Q":
            os.system("cls") if os.name == "nt" else os.system("clear")
            main_menu()

        password = input(bcolors.WARNING+"Ingrese su contraseña: "+bcolors.ENDC)

        if password == "q" or password == "Q":
            os.system("cls") if os.name == "nt" else os.system("clear")
            main_menu()

        if user == "admin" and password == "admin":
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_admin()

        elif user in usuarios and usuarios[user]["contraseña"] == password:
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_user()
        else:
            print(bcolors.FAIL+"\nUsuario o contraseña incorrectos.")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            login()
        
    except ValueError: #si el usuario ingresa un valor no valido, se ejecutara el siguiente mensaje
        print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        login()
        
    except KeyboardInterrupt:
        print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
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
    print("      Producto            |    Precio    | Cantidad  |   Total   |\tFecha")
    print("-"*87)
    if len(hist_compras) == 0:
        print(bcolors.HEADER+"No hay compras registradas."+bcolors.ENDC)
        print("-"*87 + "\n")
    for k,v in hist_compras.items():
        #hacer que la separacion, coincida con la cantidad de caracteres
        print(f" {v['producto']}     |    {v['precio']}     |     {v['cantidad']}     |   {v['total']}   | {v['fecha']}")
        print("-"*87)
    os.system("pause")
    os.system("cls") if os.name == "nt" else os.system("clear")
    #Hacer que todo se vea ordenado con | y -
    #Mostrar solo las compras del usuario en sesión
    



def ver_historial_ventas():
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Historial de ventas\n"+bcolors.ENDC)
    print("    Usuario\t|    Producto\t\t\t|    Precio\t|    Cantidad\t|    Total\t|    Fecha")
    print("-"*115)
    for venta in hist_ventas:
        #hacer que la separacion, coincida con la cantidad de caracteres
        print(f"    {venta['usuario']:<10}|  {venta['producto']:<25}|  ${venta['precio']:<5} USD\t|  {venta['cantidad']:<10}|  ${venta['total']:<10} USD|  {venta['fecha']}")
    print("-"*115 + "\n")
    os.system("pause")
    os.system("cls") if os.name == "nt" else os.system("clear")


###########################################
#   #   Funciónes de administrador    #   #
###########################################
#Menú admin
def menu_admin():
    try:
        print(bcolors.OKCYAN+"Bienvenido/a al menú de administración"+bcolors.ENDC)
        print("1.- Ver productos disponibles")
        print("2.- Agregar producto")
        print("3.- Modificar producto") #Esta funcion debe permitir modificar el nombre, el precio, añadir stock(solo sumar) modificar el tipo
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
            main_menu()
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
    print("Para volver, regresar al menú principal, escriba 'Q'")
    print(bcolors.HEADER+"(*En casos de agregar un producto existente se sumará el stock al producto existente*)"+bcolors.ENDC)
    #Preguntar por id, si existe se suma el stock
    id = input(bcolors.WARNING+"Ingrese el ID del producto que desea agregar: "+bcolors.ENDC)
    if id == "q" or id == "Q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()
    
    if id in productos:
        stock = int(input(bcolors.WARNING+"Ingrese la cantidad de stock que se agregará al producto: "+bcolors.ENDC))
        if stock == "q" or stock == "Q":
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_admin()

        productos[id]["stock"] += stock
        print(bcolors.OKGREEN+"Stock agregado exitosamente.")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()

    tipo = input(bcolors.WARNING+"Ingrese el tipo de producto: "+bcolors.ENDC).upper()
    if tipo == "q" or tipo == "Q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()
        
    if tipo == "": # Validar que el tipo no esté vacío
        print(bcolors.FAIL+"El tipo no puede estar vacío.")
        os.system("cls") if os.name == "nt" else os.system("clear")

    marca = input(bcolors.WARNING+"Ingrese la marca del producto: "+bcolors.ENDC).upper()
    if marca == "q" or marca == "Q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()

    nombre = input(bcolors.WARNING+"Ingrese el nombre del producto: "+bcolors.ENDC).upper()
    if nombre == "q" or nombre == "Q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()

    if nombre == "": # Validar que el nombre no esté vacío
        print(bcolors.FAIL+"El nombre no puede estar vacío.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        
    elif nombre in productos: # Validar que el nombre no exista en el diccionario
        print(bcolors.FAIL+"El producto ya existe.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")


    precio = float(input(bcolors.WARNING+"Ingrese el precio del producto: "+bcolors.ENDC))
    if precio == "q" or precio == "Q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()

    if precio == "": # Validar que el precio no esté vacío
        print(bcolors.FAIL+"El precio no puede estar vacío.")
        os.system("cls") if os.name == "nt" else os.system("clear")
        

    stock = int(input(bcolors.WARNING+"Ingrese la cantidad de stock que se agregará al producto: "+bcolors.ENDC))
    if stock == "q" or stock == "Q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()

    if stock == "" or stock < 0: # Validar que el stock no esté vacío
        print(bcolors.FAIL+"El stock no puede estar vacío, ni ser negativo")
        os.system("cls") if os.name == "nt" else os.system("clear")

    #Agregar producto al diccionario
    productos[len(productos)+1] = {"id": len(productos)+1, "nombre": marca+" - "+nombre, "precio": precio, "stock": stock, "tipo": tipo}
    print(bcolors.OKGREEN+"Producto agregado exitosamente.")

    #Mostrar producto recién agregado
    print("\nProducto agregado:")
    print(f"ID: {len(productos)} | Nombre: {nombre} | Precio: ${precio} USD | Stock: {stock} | Tipo: {tipo}")
    time.sleep(1.5) 
    os.system("cls") if os.name == "nt" else os.system("clear")
    menu_admin()


def modificar_producto():
    os.system("cls") if os.name == "nt" else os.system("clear")
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Modificar producto\n\n"+bcolors.ENDC)
    ver_productos()

    id = input(bcolors.WARNING+"Ingrese el ID del producto que desea modificar: "+bcolors.ENDC)
    if id == "q" or id == "Q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()

    if id in productos:
        print(bcolors.HEADER+"Si no desea modificar el nombre, deje el campo vacío y presione 'Enter'.")
        nombre = input(bcolors.WARNING+"Ingrese el nuevo nombre del producto: "+bcolors.ENDC).upper()
        if nombre == "":
            nombre = productos[id]["nombre"]

        print(bcolors.HEADER+"Si no desea modificar el precio, deje el campo vacío y presione 'Enter'.")
        precio = float(input(bcolors.WARNING+"Ingrese el nuevo precio del producto: "+bcolors.ENDC))
        if precio == "":
            precio = productos[id]["precio"]

        print(bcolors.HEADER+"Si no desea modificar el stock, deje el campo vacío y presione 'Enter'.")
        stock = int(input(bcolors.WARNING+"Ingrese el nuevo stock del producto: "+bcolors.ENDC))
        if stock == "":
            stock = productos[id]["stock"]

        print(bcolors.HEADER+"Si no desea modificar el tipo, deje el campo vacío y presione 'Enter'.")
        tipo = input(bcolors.WARNING+"Ingrese el nuevo tipo de producto: "+bcolors.ENDC).upper()
        if tipo == "":
            tipo = productos[id]["tipo"]
        #Modificar producto
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
    id = int(input(bcolors.WARNING+"Ingrese el ID del producto que desea eliminar: "+bcolors.ENDC))
    if id == "q" or id == "Q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()

    elif id == "":
        os.system("cls") if os.name == "nt" else os.system("clear")
        print(bcolors.FAIL+"Por favor, ingrese un ID válido.")
        eliminar_producto()

    if id in productos:
        del productos[id]
        print(bcolors.OKGREEN+"Producto eliminado exitosamente.")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()
    else:
        print(bcolors.FAIL+"El producto no existe.")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
        eliminar_producto()
        

#####################################
#   #   Funciónes de usuario    #   #
#####################################

#Menú usuario
def menu_user():
    try:
        print(bcolors.OKCYAN+f"Hola, "+bcolors.HEADER+f"{user}!")
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
            main_menu()

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
        print("Para volver, regresar al menú principal, escriba 'Q'")
        producto_comprar = input(bcolors.WARNING+"Seleccione ID del producto: "+bcolors.ENDC)

        if producto_comprar == "q" or producto_comprar == "Q":
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_user()

        elif producto_comprar == "":
            os.system("cls") if os.name == "nt" else os.system("clear")
            print(bcolors.FAIL+"Por favor, ingrese un ID válido.")
            comprar_producto()
        
        
    except ValueError:
        print(bcolors.FAIL+"\nERROR:"+bcolors.ENDC+"porfavor, ingrese un valor correcto.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        comprar_producto()
    except KeyboardInterrupt:
        print(bcolors.FAIL+"\nERROR:"+bcolors.ENDC+"porfavor, ingrese un valor correcto.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        comprar_producto()

    # Validamos la existencia del producto
    if producto_comprar not in productos:
        print(bcolors.FAIL+"El producto seleccionado no existe.")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
        comprar_producto()
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
                hist_compras[len(hist_compras)+1] = {"uid": usuarios[user]["uid"], "user": user, "producto": productos[producto_comprar]["nombre"], "precio": productos[producto_comprar]["precio"], "cantidad": cantidad, "total": productos[producto_comprar]["precio"]*cantidad, "fecha": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
                #Agregar solo al historial de ventas, formato de admin
                hist_ventas[len(hist_ventas)+1] = {"usuario": user, "producto": productos[producto_comprar]["nombre"], "precio": productos[producto_comprar]["precio"], "cantidad": cantidad, "total": productos[producto_comprar]["precio"]*cantidad, "fecha": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
            
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
            main_menu()

        elif opcion == "3":
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_user()
        else:
            print(bcolors.FAIL+"\nERROR:"+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            gestionar_cuenta()
            
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
def main_menu():
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
            main_menu() #se vuelve a llamar a la funcion para que el usuario pueda ingresar una opcion valida

    except ValueError: #si el usuario ingresa un valor no valido, se ejecutara el siguiente mensaje
        print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        
    except KeyboardInterrupt:
        print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        main_menu()
        
os.system("cls") if os.name == "nt" else os.system("clear")
main_menu() #llamamos a la funcion para que se ejecute el programa
