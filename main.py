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

#Diccionario de usuarios, con nombre de usuario, contraseña y uid (identificador único)
usuarios = {
    "admin" : {"usuario" : "admin", "contraseña": "admin", "uid": 0},
    "test": {"usuario" : "test", "contraseña": "test", "uid": 1},
}

#Diccionario de productos, con id, marca, nombre, precio, stock y tipo de producto
productos = {
    "1" : {"id":"1",  "marca": "" ,"nombre" : "AZULS - VG24",           "precio" : 125.00,    "stock" : 10,   "tipo": "MONITOR"},
    "2" : {"id":"2",  "marca": "" ,"nombre" : "JAYPEREX - FPS",         "precio" : 60.00,     "stock" : 10,   "tipo": "TECLADO"},
    "3" : {"id":"3",  "marca": "" ,"nombre" : "JAYPEREX - SURGE",       "precio" : 30.00,     "stock" : 10,   "tipo": "MOUSE"},
    "4" : {"id":"4",  "marca": "" ,"nombre" : "INTREL - CORE Y9-20",    "precio" : 150.00,    "stock" : 30,   "tipo": "CPU"},
    "5" : {"id":"5",  "marca": "" ,"nombre" : "NTIVIA - RTK - 4100",    "precio" : 300.00,    "stock" : 23,   "tipo": "GPU"},
    "6" : {"id":"6",  "marca": "" ,"nombre" : "CRUZIAL - VALISTIC",     "precio" : 20.00,     "stock" : 4,    "tipo": "RAM"},
    "7" : {"id":"7",  "marca": "" ,"nombre" : "MSY - M315",             "precio" : 45.00,     "stock" : 1,    "tipo": "GABINETE"},
    "8" : {"id":"8",  "marca": "" ,"nombre" : "YIGABAIT - H312-V",      "precio" : 43.00,     "stock" : 30,   "tipo": "PLACA"},
}

#Usuario en sesión, para saber quien está logueado y poder mostrar su historial de compras.
usuario_sesion = ""

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
        if user =="q" or user == "Q":
            os.system("cls") if os.name == "nt" else os.system("clear")
            main_menu()
        
        if user == "":
            print(bcolors.FAIL+"El nombre de usuario no puede estar vacío.\n")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            register()

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
            time.sleep(0.8)
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
        global usuario_sesion
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
            print(bcolors.OKGREEN+"Inicio de sesión exitoso.\n")
            time.sleep(0.7)
            os.system("cls") if os.name == "nt" else os.system("clear")
            usuario_sesion = user
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

#En este historial se muestra el historial de compras del usuario en sesion
def ver_historial_compras():
    global usuario_sesion
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Historial de compras\n"+bcolors.ENDC)
    print("     Producto\t\t  |    Precio    | Cantidad  |\t  Total     |\t Fecha   /   Hora")
    print("-"*95)
    if usuario_sesion in hist_compras:
        for v in hist_compras[usuario_sesion]:
            print(f" {v['producto']:<25}| ${v['precio']:<6} USD  |    {v['cantidad']:<6} |  ${v['total']:<6} USD |  {v['fecha']}")
    else:
        print("No hay historial de compras para este usuario.")
    print("-"*95 + "\n")
    os.system("pause")
    os.system("cls") if os.name == "nt" else os.system("clear")

#En este historial se puede ver a detealle todas las ventas realizadas en el sistema y su respectivo comprador
def ver_historial_ventas():
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Historial de ventas\n"+bcolors.ENDC)
    print("    Usuario   |        Producto\t\t  |    Precio    | Cantidad  |\t  Total     |\tFecha  /   Hora")
    print("-"*115)
    for v in hist_ventas.values():
        print(f"    {v['usuario']:<10}|  {v['producto']:<25}| ${v['precio']:<6} USD  |    {v['cantidad']:<6} |  ${v['total']:<6} USD |  {v['fecha']}")
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


def agregar_producto():
    ver_productos()
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Agregar productos\n"+bcolors.ENDC)
    print("Para volver al menú principal, escriba 'Q'")
    print(bcolors.HEADER+"(*En casos de agregar un producto ya existente, solo se le sumará el stock*)"+bcolors.ENDC)
    print("(Dejar en blanco para añadir uno nuevo)")
    id = input(bcolors.WARNING+"Ingrese el ID del producto que desea agregar: "+bcolors.ENDC)
    
    if id == "q" or id == "Q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()
    
    if id in productos:
        stock = int(input(bcolors.WARNING+"Ingrese la cantidad de stock que se agregará al producto: "+bcolors.ENDC))
        if stock == "q" or stock == "Q":
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_admin()

        elif stock == "" or stock < 0:
            print(bcolors.FAIL+"El stock no puede estar vacío, ni ser negativo")
            time.sleep(1.5)
            os.system("cls") if os.name == "nt" else os.system("clear")
            agregar_producto()

        productos[id]["stock"] += stock
        print(bcolors.OKGREEN+"Stock agregado exitosamente.")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()

    tipo = input(bcolors.WARNING+"Ingrese el tipo de producto: "+bcolors.ENDC).upper()
    if tipo == "q" or tipo == "Q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()
        
    elif tipo == "": # Validar que el tipo no esté vacío
        print(bcolors.FAIL+"El tipo no puede estar vacío.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        agregar_producto()

    marca = input(bcolors.WARNING+"Ingrese la marca del producto: "+bcolors.ENDC).upper()
    if marca == "q" or marca == "Q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()
    elif marca == "": # Validar que la marca no esté vacía
        print(bcolors.FAIL+"La marca no puede estar vacía.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        agregar_producto()

    nombre = input(bcolors.WARNING+"Ingrese el nombre del producto: "+bcolors.ENDC).upper()
    if nombre == "q" or nombre == "Q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()

    if nombre == "": # Validar que el nombre no esté vacío
        print(bcolors.FAIL+"El nombre no puede estar vacío.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        agregar_producto()
        
    elif nombre in productos: # Validar que el nombre no exista en el diccionario
        print(bcolors.FAIL+"El producto ya existe.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        agregar_producto()


    precio = float(input(bcolors.WARNING+"Ingrese el precio del producto: "+bcolors.ENDC))
    if precio == "q" or precio == "Q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()

    if precio == "" or None: # Validar que el precio no esté vacío
        print(bcolors.FAIL+"El precio no puede estar vacío.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        

    stock = int(input(bcolors.WARNING+"Ingrese la cantidad de stock del producto:  "+bcolors.ENDC))
    if stock == "q" or stock == "Q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()

    if stock == "" or stock < 0: # Validar que el stock no esté vacío
        print(bcolors.FAIL+"El stock no puede estar vacío, ni ser negativo")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")

    #Agregar producto al diccionario
    productos[str(len(productos)+1)] = {"id": len(productos)+1, "marca": marca, "nombre": nombre, "precio": precio, "stock": stock, "tipo": tipo}
    print(bcolors.OKGREEN+"Producto agregado exitosamente.")

    #Mostrar producto recién agregado
    print("\nProducto agregado:")
    print(f"ID: {len(productos)} | Nombre: {nombre} | Precio: ${precio} USD | Stock: {stock} | Tipo: {tipo}")
    time.sleep(5) 
    os.system("cls") if os.name == "nt" else os.system("clear")
    menu_admin()


def modificar_producto():
    os.system("cls") if os.name == "nt" else os.system("clear")
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Modificar producto\n\n"+bcolors.ENDC)
    ver_productos()
    #Crear una funcion para poder modificar el producto seleccionado por ID
    print("Para regresar al menú principal, escriba 'Q'")
    id = input(bcolors.WARNING+"Ingrese el ID del producto que desea modificar: "+bcolors.ENDC)
    if id.lower() == "q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()
    
    if id in productos:
        try:
            os.system("cls") if os.name == "nt" else os.system("clear")
            ver_productos()
            print(f"Producto seleccionado: {productos[id]['nombre']}")
            print("1.- Modificar nombre")
            print("2.- Modificar precio")
            print("3.- Modificar stock")
            print("4.- Modificar tipo")
            print("5.- Volver al menú principal")
            opcion = input(bcolors.WARNING+"Ingrese una opción: "+bcolors.ENDC)

            if opcion == "1":
                os.system("cls") if os.name == "nt" else os.system("clear")
                nuevo_nombre = input(bcolors.WARNING+"Ingrese el nuevo nombre del producto: "+bcolors.ENDC)
                productos[id]["nombre"] = nuevo_nombre
                print(bcolors.OKGREEN+"Nombre modificado exitosamente.")
                time.sleep(1.5)
                os.system("cls") if os.name == "nt" else os.system("clear")
                modificar_producto()

            elif opcion == "2":
                os.system("cls") if os.name == "nt" else os.system("clear")
                nuevo_precio = float(input(bcolors.WARNING+"Ingrese el nuevo precio del producto: "+bcolors.ENDC))
                productos[id]["precio"] = nuevo_precio
                print(bcolors.OKGREEN+"Precio modificado exitosamente.")
                time.sleep(1.5)
                os.system("cls") if os.name == "nt" else os.system("clear")
                modificar_producto()

            elif opcion == "3":
                os.system("cls") if os.name == "nt" else os.system("clear")
                nuevo_stock = int(input(bcolors.WARNING+"Ingrese la nueva cantidad de stock del producto: "+bcolors.ENDC))
                productos[id]["stock"] = nuevo_stock
                print(bcolors.OKGREEN+"Stock modificado exitosamente.")
                time.sleep(1.5)
                os.system("cls") if os.name == "nt" else os.system("clear")
                modificar_producto()

            elif opcion == "4":
                os.system("cls") if os.name == "nt" else os.system("clear")
                nuevo_tipo = input(bcolors.WARNING+"Ingrese el nuevo tipo de producto: "+bcolors.ENDC)
                productos[id]["tipo"] = nuevo_tipo
                print(bcolors.OKGREEN+"Tipo modificado exitosamente.")
                time.sleep(1.5)
                os.system("cls") if os.name == "nt" else os.system("clear")
                modificar_producto()
        except ValueError:
            print(bcolors.FAIL+"Por favor, ingrese un valor válido.")
            time.sleep(1.5)
            os.system("cls") if os.name == "nt" else os.system("clear")
            modificar_producto()
        except KeyboardInterrupt:
            print(bcolors.FAIL+"Por favor, ingrese un valor válido.")
            time.sleep(1.5)
            os.system("cls") if os.name == "nt" else os.system("clear")
            modificar_producto()
        except KeyError:
            print(bcolors.FAIL+"Por favor, ingrese un valor válido.")
            time.sleep(1.5)
            os.system("cls") if os.name == "nt" else os.system("clear")
            modificar_producto()


def eliminar_producto():
    ver_productos()
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Eliminar producto\n"+bcolors.ENDC)
    print("Para regresar al menú principal, escriba 'Q'")
    id = input(bcolors.WARNING+"Ingrese el ID del producto que desea eliminar: "+bcolors.ENDC)
    if id.lower() == "q":
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()

    elif id == "" or None:
        os.system("cls") if os.name == "nt" else os.system("clear")
        print(bcolors.FAIL+"Por favor, ingrese un ID válido.")
        eliminar_producto()

    if id in productos:
        del productos[id] #Eliminar producto
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

#Menú de usuario
def menu_user():
    try:
        print(bcolors.OKCYAN+f"Hola, "+bcolors.HEADER+f"{user}!")
        print(bcolors.OKCYAN+"Bienvenido/a a MyGamingSetup\n"+bcolors.ENDC)
        print("1.- Ver productos disponibles")
        print("2.- Comprar producto")
        print("3.- Ver historial de compras")
        print("4.- Gestionar cuenta")
        print("5.- Salir de la cuenta")
        opcion = input(bcolors.WARNING+"Ingrese una opción: "+bcolors.ENDC)

        if opcion == "1": #Llama la función para ver los productos disponibles, de forma limpia
            os.system("cls") if os.name == "nt" else os.system("clear")
            ver_productos()
            menu_user()

        elif opcion == "2": #Llama la función para comprar un producto 
            os.system("cls") if os.name == "nt" else os.system("clear")
            comprar_producto()
            menu_user()

        elif opcion == "3": #Llama la función para ver el historial de compras del usuario en sesión
            os.system("cls") if os.name == "nt" else os.system("clear")
            ver_historial_compras()
            menu_user()

        elif opcion == "4": #Llama la función para gestionar la cuenta del usuario en sesión
            os.system("cls") if os.name == "nt" else os.system("clear")
            gestionar_cuenta()

        elif opcion == "5": #Salir de la cuenta y volver al menú principal
            os.system("cls") if os.name == "nt" else os.system("clear")
            main_menu()

        else:
            print(bcolors.FAIL+"\nERROR:"+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_user()
    except ValueError: #si el usuario ingresa un valor no valido, se ejecutara el siguiente mensaje y se reiniciara el menu
        print(bcolors.FAIL+"\nERROR:"+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_user()
    except KeyboardInterrupt: #Evitamos que se produzca un crasheo si el usuario presiona Ctrl+C
        print(bcolors.FAIL+"\nERROR:"+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_user()       


def comprar_producto():
    ver_productos()
    try:
        print(bcolors.OKCYAN+bcolors.UNDERLINE+"Comprar producto\n"+bcolors.ENDC)
        print("Para volver, regresar al menú principal, escriba 'Q'")
        producto_comprar = input(bcolors.WARNING+"Seleccione ID del producto: "+bcolors.ENDC)
        time.sleep(0.8)
        if producto_comprar == "q" or producto_comprar == "Q":
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_user()
        elif producto_comprar == "":
            os.system("cls") if os.name == "nt" else os.system("clear")
            comprar_producto()
            print(bcolors.FAIL+"Por favor, ingrese un ID válido.")
            
        

        # Validamos la existencia del producto
        if producto_comprar not in productos:
            print(bcolors.FAIL+"El producto seleccionado no existe.")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            comprar_producto()
        while True:
            cantidad = int(input(bcolors.WARNING+"Ingrese la cantidad: "+bcolors.ENDC))
            if cantidad < 0:
                print(bcolors.FAIL+"Por favor, ingrese un número mayor a 0.")
                time.sleep(1)
                os.system("cls") if os.name == "nt" else os.system("clear")
                comprar_producto()

            if productos[producto_comprar]["stock"] < cantidad:
                print(bcolors.FAIL+"Lo sentimos, no hay suficiente stock del producto seleccionado.\n")
                time.sleep(1)
                os.system("cls") if os.name == "nt" else os.system("clear")
                comprar_producto()

            else:
                productos[producto_comprar]["stock"] -= cantidad
                print(bcolors.OKGREEN+"Total a pagar:"+bcolors.ENDC+f"${productos[producto_comprar]['precio']*cantidad} USD")
                #confirmar compra, ENTER o Q para cancelar
                confirmar = input(bcolors.WARNING+"Presione ENTER para confirmar la compra ( 'Q' para cancelar) : "+bcolors.ENDC)
                if confirmar.lower() == "q":
                    productos[producto_comprar]["stock"] += cantidad
                    print(bcolors.FAIL+"Compra cancelada.")
                    time.sleep(1.5)
                    os.system("cls") if os.name == "nt" else os.system("clear")
                    comprar_producto() 
                #Añadir la compra al historial de compras del usuario en sesion
                if usuario_sesion not in hist_compras:
                    hist_compras[usuario_sesion] = []
                hist_compras[usuario_sesion].append({"producto": productos[producto_comprar]["nombre"], "precio": productos[producto_comprar]["precio"], "cantidad": cantidad, "total": productos[producto_comprar]["precio"]*cantidad, "fecha": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
                #Añadir la compra al historial de ventas
                hist_ventas[len(hist_ventas)+1] = {"usuario": usuario_sesion, "producto": productos[producto_comprar]["nombre"], "precio": productos[producto_comprar]["precio"], "cantidad": cantidad, "total": productos[producto_comprar]["precio"]*cantidad, "fecha": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
                os.system("cls") if os.name == "nt" else os.system("clear")
                print(bcolors.OKGREEN+"Compra exitosa.")
                time.sleep(0.7)
                os.system("cls") if os.name == "nt" else os.system("clear")
                break  # Salir del bucle si la compra es exitosa

    except ValueError:
        print(bcolors.FAIL+"ERROR:"+bcolors.ENDC+"Por favor, ingrese un número válido.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
    except KeyboardInterrupt:
        print(bcolors.FAIL+"ERROR:"+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
    except KeyError:
        print(bcolors.FAIL+"ERROR:"+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")


def gestionar_cuenta():
    try:
        global user
        print(bcolors.OKCYAN+bcolors.UNDERLINE+"Gestionar cuenta"+bcolors.ENDC)
        print("1.- Cambiar contraseña")
        print("2.- Borrar cuenta")
        print("3.- Volver al menú principal")
        opcion = input(bcolors.WARNING+"Ingrese una opción: "+bcolors.ENDC)
        if opcion == "1":
            os.system("cls") if os.name == "nt" else os.system("clear")
            cambiar_contraseña()

        elif opcion == "2": #borrar cuenta del usuario en sesion iniciada
            #borrar cuenta del usuario en sesion iniciada
            if usuario_sesion in usuarios:
                del usuarios[usuario_sesion]
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
    if newpass == usuarios[user]["contraseña"]:
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
        
os.system("cls") if os.name == "nt" else os.system("clear") #Limpiamos un poco la pantalla para ver mejor el programa
main_menu()                                                 #llamamos a la funcion para que se ejecute el programa
