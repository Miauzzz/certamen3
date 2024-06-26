# Certamen 3 - 30%
#Idea : Crear un sistema de inventario/ventas de productos de computación. 
#Testeado en Windows - Linux (los pause, fallan en linux, pero no afecta el funcionamiento del programa)

#librerias
import os                   #Libreria para poder ejecutar comandos del sistema
import sys                  #Libreria para poder ejecutar comandos del sistema
import getpass              #Libreria para poder ocultar el texto que se escriba (En este caso lo utilizamos para la contraseña)
import time                 #Libreria para poder hacer pausas en el programa
import datetime             #Libreria para obtener la fecha y hora actual
from colors import bcolors  #Se importa clase bcolors del archivo colors.py (Estos varían según la configuración que tenga el usuario en su terminal.)


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
    "1" : {"id":"1",  "marca": "AZULS",     "nombre" : "VG24' 144HZ",     "precio" : 125.00,    "stock" : 10,   "tipo": "MONITOR"},
    "2" : {"id":"2",  "marca": "HYPERZ",    "nombre" : "ALLOY FPS",       "precio" : 60.00,     "stock" : 93,   "tipo": "TECLADO"},
    "3" : {"id":"3",  "marca": "HYPERZ",    "nombre" : "SURGE RGB 360",   "precio" : 30.00,     "stock" : 67,   "tipo": "MOUSE"},
    "4" : {"id":"4",  "marca": "INTREL",    "nombre" : "CORE Y9-8TH",     "precio" : 150.00,    "stock" : 25,   "tipo": "CPU"},
    "5" : {"id":"5",  "marca": "NEVIDIA",   "nombre" : "RTK - 4100",      "precio" : 300.00,    "stock" : 15,   "tipo": "GPU"},
    "6" : {"id":"6",  "marca": "KINSON",    "nombre" : "Furia"       ,    "precio" : 20.00,     "stock" : 85,   "tipo": "RAM"},
    "7" : {"id":"7",  "marca": "KRUSIAL",   "nombre" : "BALLISTICKS",     "precio" : 45.00,     "stock" : 0,    "tipo": "GABINETE"},
    "8" : {"id":"8",  "marca": "GIGABITS",  "nombre" : "H312-V",          "precio" : 43.00,     "stock" : 33,   "tipo": "PLACA"},
}

#Usuario en sesión, para saber quien está logueado y poder mostrar su historial de compras.
usuario_sesion = ""

#Historial de compras que visualiza el usuario (cada usuario tiene su propio historial)
hist_compras = {}

#Historial que visualiza el admin (todas las ventas)
hist_ventas = {}

#Comentario Adicional : Todo texto que contenga "bcolors...." es solo decorativo.
#Se utilizan para darle un toque más visual al programa, y diferenciar los mensajes de error, de los mensajes de información, etc.
#al igual que algunos arreglos de impresión, para que se vea más ordenado (como los historiales de compra/venta).


#################################
#   #   #   Funciones   #   #   #
#################################

#Registrar usuario
def register():
    try:
        print(bcolors.OKCYAN+"Registrarse en MyGamingSetup\n"+bcolors.ENDC)
        print("Para volver al menú principal, escriba 'Q'.\n")
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
        #A la password se le agrega el getpass para que no se vea la contraseña al escribirla
        password = getpass.getpass(bcolors.WARNING+"Ingrese su contraseña: "+bcolors.ENDC)
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
        print("Para volver al menú principal, escriba 'Q'.\n")
        user = input(bcolors.WARNING+"Ingrese un nombre de usuario: "+bcolors.ENDC)

        if user == "q" or user == "Q":
            os.system("cls") if os.name == "nt" else os.system("clear")
            main_menu()
             
        #A la password se le agrega el getpass para que no se vea la contraseña al escribirla
        password = getpass.getpass(bcolors.WARNING+"Ingrese su contraseña: "+bcolors.ENDC)

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

#Ver el catálogo de productos disponibles
def ver_productos():
    os.system("cls") if os.name == "nt" else os.system("clear")
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Productos disponibles\n"+bcolors.ENDC)
    #Se hace print de los productos disponibles, con formato tabla, aplicando algunos colores.
    print(bcolors.OKGREEN+"    ID\t"+bcolors.ENDC+"|"+bcolors.OKGREEN+"      Tipo\t  "+bcolors.ENDC+"|"+bcolors.OKGREEN+"    Marca     /    Nombre\t    "+bcolors.ENDC+"|"+bcolors.OKGREEN+"      Precio\t "+bcolors.ENDC+"|"+bcolors.OKGREEN+"   Stock"+bcolors.ENDC)
    print("-"*95)
    for v in productos.values():                                    #Recorre el diccionario de productos y muestra el valor
        if v["stock"] == 0:                                         #si stock en al lista productos es value 0, esta debe transformarse en "Agotado"
            v["stock"] = bcolors.FAIL+"Agotado"+bcolors.ENDC
        print(bcolors.HEADER+f"    {v['id']:<4}"+bcolors.ENDC+"|"+f"  {v['tipo']:<15}| {v['marca']:<13}- {v['nombre']:<16} |    ${v['precio']:<5} USD\t |    {v['stock']:<17}") #Ajustes de impresión para que se vea bonito
    print("-"*95 + "\n")


###########################################
#   #   Funciónes de administrador    #   #
###########################################

#Menú admin
def menu_admin():
    try:    #Intenta ejecutar el código, si hay un error, se ejecuta el except
        print(bcolors.OKCYAN+"Bienvenido/a al menú de administración\n"+bcolors.ENDC)
        print("1.- Ver productos disponibles")
        print("2.- Agregar producto")
        print("3.- Modificar producto")
        print("4.- ver historial de ventas")
        print("5.- Eliminar producto")
        print("6.- Salir de la cuenta\n")
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
            modificar_productos()
        
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
            print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_admin()

    except KeyboardInterrupt: #Evitamos que se produzca un crasheo si el usuario presiona Ctrl+C
        print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese un valor correcto.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()


def agregar_producto():
    os.system("cls") if os.name == "nt" else os.system("clear")
    ver_productos()
    try:    #Intenta ejecutar el código, si hay un error, se ejecuta el except
        print(bcolors.OKCYAN+bcolors.UNDERLINE+"Agregar productos\n"+bcolors.ENDC)
        print("Para volver al menú principal, escriba 'Q'")
        print(bcolors.HEADER+"(*En casos de agregar un producto ya existente, solo se le sumará el stock*)"+bcolors.ENDC)
        print("(Dejar en blanco para añadir un producto nuevo)")
        id = input(bcolors.WARNING+"Ingrese el ID del producto: "+bcolors.ENDC)
        if id not in '1234567890Qq': #Validar que el ID no sea un número o "q/Q"
            os.system("cls") if os.name == "nt" else os.system("clear")
            print(bcolors.FAIL+"Por favor, ingrese un ID válido.")
            time.sleep(1)
            agregar_producto()
            
        if id == "q" or id == "Q": #si el usuario ingresa "q" o "Q", se regresará al menú principal
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_admin()


        #si el id ya existe, se le sumará el stock
        if id in productos:
            stock = int(input(bcolors.WARNING+"Ingrese la cantidad de stock que se agregará al producto: "+bcolors.ENDC))
            if stock == "q" or stock == "Q": #si el usuario ingresa "q" o "Q", se regresará al menú principal
                os.system("cls") if os.name == "nt" else os.system("clear")
                menu_admin()

            elif stock == "" or stock < 0: #Validar que el stock no esté vacío o sea negativo
                print(bcolors.FAIL+"El stock no puede estar vacío, ni ser negativo")
                time.sleep(1.5)
                os.system("cls") if os.name == "nt" else os.system("clear")
                agregar_producto()

            productos[id]["stock"] += stock #Sumar el stock al producto existente
            print(bcolors.OKGREEN+"Stock agregado exitosamente.")
            time.sleep(1.5)
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_admin()

        
        elif len(str(id)) > 4:  #Validar que el ID no sea mayor a 4 digitos
            print(bcolors.FAIL+"El ID no puede ser mayor a 4 digitos.")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            agregar_producto()

        #tipo de producto
        tipo = input(bcolors.WARNING+"Ingrese el tipo de producto: "+bcolors.ENDC).upper()
        if tipo == "q" or tipo == "Q":  #si el usuario ingresa "q" o "Q", se regresará al menú principal
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_admin()

        elif tipo == "":    #Validar que el tipo no esté vacío
            print(bcolors.FAIL+"El tipo no puede estar vacío.")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            agregar_producto()
        #Marca del producto
        marca = input(bcolors.WARNING+"Ingrese la marca del producto: "+bcolors.ENDC).upper()                                                                    #Agregar un guión al final de la marca
        if marca == "q" or marca == "Q":    #si el usuario ingresa "q" o "Q", se regresará al menú principal
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_admin()

        elif marca == "":   #Validar que la marca no esté vacía
            print(bcolors.FAIL+"La marca no puede estar vacía.")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            agregar_producto()

        #Nombre del producto
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

        #Precio del producto
        precio = float(input(bcolors.WARNING+"Ingrese el precio del producto: "+bcolors.ENDC))
        if precio == "q" or precio == "Q":  #si el usuario ingresa "q" o "Q", se regresará al menú principal
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_admin()

        if precio == "" or None: # Validar que el precio no esté vacío
            print(bcolors.FAIL+"El precio no puede estar vacío.")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            agregar_producto()

        #Stock del producto
        stock = int(input(bcolors.WARNING+"Ingrese la cantidad de stock del producto:  "+bcolors.ENDC))
        if stock == "q" or stock == "Q":
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_admin()

        if stock == "" or stock < 0: # Validar que el input de stock a ingresar no esté vacío o sea negativo
            print(bcolors.FAIL+"El stock no puede estar vacío, ni ser negativo")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            agregar_producto()

        #Agregar producto al diccionario, se suma +1 al id y permite agregar mucho productos
        productos[str(len(productos) + 1)] = {
            "id": str(len(productos) + 1), 
            "marca": marca, 
            "nombre": nombre, 
            "precio": precio, 
            "stock": stock, 
            "tipo": tipo}

        #Mostrar producto recién agregado
        print("\nProducto agregado:")
        print(productos[id]) # Mostrar producto recién agregado en consola para confirmar que se agregó correctamente y visualizarlo de forma cruda
        time.sleep(2.5) 
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_admin()

    except ValueError:          #si el usuario ingresa un valor no valido, se ejecutara el siguiente mensaje
        print(bcolors.FAIL+"\nPorfavor, ingrese un valor válido.")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
        agregar_producto()

    except KeyboardInterrupt:   #si el usuario ingresa un valor no valido, se ejecutara el siguiente mensaje
        print(bcolors.FAIL+"\nPorfavor, ingrese un valor válido.")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
        agregar_producto()
        
    except KeyError:
        os.system("cls") if os.name == "nt" else os.system("clear")
        agregar_producto()


def modificar_productos():
    try:    #Intenta ejecutar el código, si hay un error, se ejecuta el except
        os.system("cls") if os.name == "nt" else os.system("clear")
        print(bcolors.OKCYAN+bcolors.UNDERLINE+"Modificar producto\n\n"+bcolors.ENDC)
        ver_productos()
        print("Para regresar al menú principal, escriba 'Q'")
        id = input(bcolors.WARNING+"Ingrese el ID del producto que desea modificar: "+bcolors.ENDC)
        
        #Validar que el ID no sea un número o "q/Q"
        if id == "q" or id == "Q":
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_admin()
        elif id == "" or None:
            os.system("cls") if os.name == "nt" else os.system("clear")
            print(bcolors.FAIL+"Por favor, ingrese un ID válido.")
            time.sleep(1)
            modificar_productos()
            
        elif id not in productos:   #Validar que el ID ingresado exista en el diccionario
            os.system("cls") if os.name == "nt" else os.system("clear")
            print(bcolors.FAIL+"El producto no existe.")
            time.sleep(1)
            modificar_productos()

    except ValueError:  #si el usuario ingresa un valor no valido, se ejecutara el siguiente mensaje
        print(bcolors.FAIL+"Por favor, ingrese un ID válido.")
        time.sleep(1.5)
        os.system("cls") if os.name == "nt" else os.system("clear")
        modificar_productos()

    if id in productos: #Validar que el ID ingresado exista en el diccionario, para luego ingresar al menú de modificación
        modificar_atributos_producto(id)    #Llama la función para modificar los atributos del producto


def modificar_atributos_producto(id): #Función para modificar los atributos del producto (EL "id" es el ID del producto a modificar) y se ejecuta en la función "modificar_productos"
    try: #Intenta ejecutar el código, si hay un error, se ejecuta el except
        os.system("cls") if os.name == "nt" else os.system("clear")
        ver_productos()
        print(f"Producto seleccionado: "+bcolors.WARNING+f"{productos[id]['marca']}"+bcolors.ENDC+" - "+bcolors.WARNING+f"{productos[id]['nombre']}"+bcolors.ENDC)
        print("1.- Modificar nombre")
        print("2.- Modificar marca")
        print("3.- Modificar precio")
        print("4.- Modificar stock")
        print("5.- Modificar tipo")
        print("6.- Volver")
        opcion = input(bcolors.WARNING+"Ingrese una opción: "+bcolors.ENDC)

        if opcion == "1":
            nuevo_nombre = input(bcolors.WARNING+"Ingrese el nuevo nombre del producto: "+bcolors.ENDC).upper()
            productos[id]["nombre"] = nuevo_nombre  #Modificar el nombre del producto
            print(bcolors.OKGREEN+"Nombre modificado exitosamente.")
            time.sleep(1.5)
            modificar_atributos_producto(id)

        elif opcion == "2":
            nueva_marca = input(bcolors.WARNING+"Ingrese la nueva marca del producto: "+bcolors.ENDC).upper()
            productos[id]["marca"] = nueva_marca    #Se reemplaza la marca del producto, por la nueva marca ingresada
            print(bcolors.OKGREEN+"Marca modificada exitosamente.")
            time.sleep(1.5)
            modificar_atributos_producto(id)

        elif opcion == "3":
            nuevo_precio = float(input(bcolors.WARNING+"Ingrese el nuevo precio del producto: "+bcolors.ENDC))
            productos[id]["precio"] = nuevo_precio  #Se reemplaza el precio del producto, por el nuevo precio ingresado
            print(bcolors.OKGREEN+"Precio modificado exitosamente.")
            time.sleep(1.5)
            modificar_atributos_producto(id)

        elif opcion == "4":
            nuevo_stock = int(input(bcolors.WARNING+"Ingrese la nueva cantidad de stock del producto: "+bcolors.ENDC))
            productos[id]["stock"] = nuevo_stock    #Se reemplaza el stock del producto, por el nuevo stock ingresado
            print(bcolors.OKGREEN+"Stock modificado exitosamente.")
            time.sleep(1.5)
            modificar_atributos_producto(id)

        elif opcion == "5":
            nuevo_tipo = input(bcolors.WARNING+"Ingrese el nuevo tipo de producto: "+bcolors.ENDC).upper()
            productos[id]["tipo"] = nuevo_tipo  #Se reemplaza el tipo del producto, por el nuevo tipo ingresado
            print(bcolors.OKGREEN+"Tipo modificado exitosamente.")
            time.sleep(1.5)
            modificar_atributos_producto(id)

        elif opcion == "6":
            os.system("cls") if os.name == "nt" else os.system("clear")
            modificar_productos()

        else:
            print(bcolors.FAIL+"Por favor, ingrese una opción válida.")
            time.sleep(1.5)
            modificar_atributos_producto(id)

    except ValueError:  #Si el usuario ingresa un valor no valido, se ejecutara el siguiente mensaje
        print(bcolors.FAIL+"Por favor, ingrese un valor válido.")
        time.sleep(1.5)
        modificar_atributos_producto(id)
    except KeyboardInterrupt:   #Si el usuario presiona Ctrl+C, se ejecutara el siguiente mensaje
        print(bcolors.FAIL+"Por favor, ingrese un valor válido.")
        time.sleep(1.5)
        modificar_atributos_producto(id)
    

def eliminar_producto():
    ver_productos() #Mostrar productos disponibles
    print(bcolors.OKCYAN + bcolors.UNDERLINE + "Eliminar producto\n" + bcolors.ENDC)
    print("Para regresar al menú principal, escriba 'Q'")
    
    while True: #Ciclo infinito para que el usuario pueda ingresar un ID válido
        id = input(bcolors.WARNING + "Ingrese el ID del producto que desea eliminar: " + bcolors.ENDC)
        
        if id.lower() == "q":   #Si el usuario ingresa "q" o "Q", se regresará al menú principal
            os.system("cls" if os.name == "nt" else "clear")
            menu_admin()
            break   #Romper el ciclo infinito si el usuario ingresa "q" o "Q"

        if id == "" or id is None:  #Validar que el ID no esté vacío
            os.system("cls" if os.name == "nt" else "clear")
            print(bcolors.FAIL + "Por favor, ingrese un ID válido.")
            continue    #Continuar con el ciclo infinito si el ID está vacío

        if id in productos: #Validar que el ID ingresado exista en el diccionario
            del productos[id]  # Eliminar producto
            print(bcolors.OKGREEN + "Producto eliminado exitosamente.")
            time.sleep(1.5)
            os.system("cls" if os.name == "nt" else "clear")
            menu_admin()
            break   #Romper el ciclo infinito si el producto se eliminó exitosamente

        else:   #Si el ID ingresado no existe en el diccionario, se mostrará un mensaje en pantalla
            print(bcolors.FAIL + "El producto no existe.")
            time.sleep(1.5)
            os.system("cls" if os.name == "nt" else "clear")
        
#En este historial se puede ver a detalle todas las ventas realizadas en el sistema y su respectivo comprador.
def ver_historial_ventas():
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Historial de ventas\n"+bcolors.ENDC)
    #Se imprime el historial de ventas, con formato tabla, aplicando algunos colores.
    print(bcolors.OKGREEN+"    Usuario   "+bcolors.ENDC+"|"+bcolors.OKGREEN+"        Producto\t\t  "+bcolors.ENDC+"|"+bcolors.OKGREEN+"    Precio    "+bcolors.ENDC+"|"+bcolors.OKGREEN+" Cantidad  "+bcolors.ENDC+"|"+bcolors.OKGREEN+"\t  Total     "+bcolors.ENDC+"|"+bcolors.OKGREEN+"\tFecha  /   Hora"+bcolors.ENDC)
    print("-"*115)
    if len(hist_ventas) == 0:   #Si no hay ventas registradas, se mostrará un mensaje en pantalla
        print(bcolors.HEADER+"No hay ventas registradas."+bcolors.ENDC)
    for v in hist_ventas.values():  #Recorre el historial de ventas y muestra los valores del diccionario 
        print(bcolors.HEADER+f"    {v['usuario']:<10}"+bcolors.ENDC+f"|  {v['producto']:<25}| "+bcolors.OKGREEN+"$"+bcolors.ENDC+f"{v['precio']:<6} USD  |    {v['cantidad']:<6} |  "+bcolors.OKGREEN+"$"+bcolors.ENDC+f"{v['total']:<6} USD |  {v['fecha']}")
    print("-"*115 + "\n")
    os.system("pause")
    os.system("cls") if os.name == "nt" else os.system("clear")


#####################################
#   #   Funciónes de usuario    #   #
#####################################

#Menú de usuario
def menu_user():
    try:
        print(bcolors.OKCYAN+f"Hola, "+bcolors.HEADER+f"{user}"+bcolors.OKCYAN+"!")
        print(bcolors.OKCYAN+"Bienvenido/a a MyGamingSetup\n"+bcolors.ENDC)
        print("1.- Ver productos disponibles")
        print("2.- Comprar producto")
        print("3.- Ver historial de compras")
        print("4.- Gestionar cuenta")
        print("5.- Salir de la cuenta\n")
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

        else:   #Si el usuario ingresa un valor no valido, se ejecutara el siguiente mensaje
            print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_user()

    except ValueError: #si el usuario ingresa un valor no valido, se ejecutara el siguiente mensaje y se reiniciara el menu
        print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_user()

    except KeyboardInterrupt: #Evitamos que se produzca un crasheo si el usuario presiona Ctrl+C
        print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        menu_user()       


def comprar_producto():
    ver_productos()
    try:
        print(bcolors.OKCYAN + bcolors.UNDERLINE + "Comprar producto\n" + bcolors.ENDC)
        print("Para volver al menú principal, ingrese 'Q'")
        producto_comprar = input(bcolors.WARNING + "Seleccione ID del producto: " + bcolors.ENDC) #Solicitar al usuario que ingrese el ID del producto a comprar
        if producto_comprar.lower() == "q":
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_user()

        elif producto_comprar == "":    #Validar que el ID no esté vacío
            print(bcolors.FAIL + "Por favor, ingrese un ID válido.")
            comprar_producto()
            
        if producto_comprar not in productos:   #Validar que el ID ingresado exista en el diccionario
            print(bcolors.FAIL + "El producto seleccionado no existe.")
            time.sleep(1)
            comprar_producto()
            

        while True: #Ciclo infinito para que el usuario pueda ingresar una cantidad válida
            try:
                cantidad = int(input(bcolors.WARNING + "Ingrese la cantidad: " + bcolors.ENDC))
                if productos[producto_comprar]["stock"] == 0 or productos[producto_comprar]["stock"] == "Agotado":  #Validar que el producto no esté agotado
                    print(bcolors.FAIL + "Lo sentimos, el producto seleccionado está agotado.\n")
                    time.sleep(1)
                    comprar_producto()
                           
                elif cantidad <= 0:     #Validar que la cantidad no sea menor o igual a 0
                    print(bcolors.FAIL + "Por favor, ingrese un número mayor a 0.")
                    time.sleep(1)
                    comprar_producto()
                    

                elif productos[producto_comprar]["stock"] < cantidad:   #Validar que la cantidad no sea mayor al stock del producto
                    print(bcolors.FAIL + "Lo sentimos, no hay suficiente stock del producto seleccionado.\n")
                    time.sleep(1)
                    comprar_producto()
                    

                productos[producto_comprar]["stock"] -= cantidad    #Restar la cantidad comprada al stock del producto, si la compra es exitosa (de esta forma se actualiza el stock)
                print(bcolors.OKGREEN + "Total a pagar: " + bcolors.ENDC + f"${productos[producto_comprar]['precio'] * cantidad} USD") #Mostrar el total a pagar
                time.sleep(0.5)

                # Confirmar la compra, o cancelarla
                confirmar = input(bcolors.WARNING + "Presione ENTER para confirmar la compra ( 'Q' para cancelar) : " + bcolors.ENDC)
                if confirmar.lower() == "q":
                    productos[producto_comprar]["stock"] += cantidad    #Sumar la cantidad cancelada al stock del producto, si la compra es cancelada (de esta forma se restaura el stock)
                    print(bcolors.FAIL + "Compra cancelada.")
                    time.sleep(0.7)
                    comprar_producto()  # Llamada recursiva para mantener contexto
                    

                elif usuario_sesion not in hist_compras:    #Si el usuario en sesión no tiene compras, se crea una lista vacía
                    hist_compras[usuario_sesion] = []       #Crear una lista vacía para el usuario en sesión

                # Añadir la compra al historial de compras del usuario en sesión (para el usuario en sesión)
                hist_compras[usuario_sesion].append({   
                    "producto": productos[producto_comprar]["marca"] + " - " + productos[producto_comprar]["nombre"],
                    "precio": productos[producto_comprar]["precio"],
                    "cantidad": cantidad,
                    "total": productos[producto_comprar]["precio"] * cantidad,
                    "fecha": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                })

                # Añadir la compra al historial de ventas del sistema (para el administrador)
                hist_ventas[len(hist_ventas) + 1] = {
                    "usuario": usuario_sesion,
                    "producto": productos[producto_comprar]["marca"] + " - " + productos[producto_comprar]["nombre"],
                    "precio": productos[producto_comprar]["precio"],
                    "cantidad": cantidad,
                    "total": productos[producto_comprar]["precio"] * cantidad,
                    "fecha": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                }

                os.system("cls") if os.name == "nt" else os.system("clear")
                print(bcolors.OKGREEN + "Compra exitosa.")
                time.sleep(0.7)
                os.system("cls") if os.name == "nt" else os.system("clear")
                break  # Salir del bucle si la compra es exitosa

            except ValueError:  #Validar que la cantidad ingresada sea un número
                print(bcolors.FAIL + "Por favor, ingrese un número válido.")
                time.sleep(1)
                comprar_producto()

    except TypeError:   
        print(bcolors.FAIL + "Producto agotado.")       #Tuvimos que acudir a una solución rápida para evitar errores, pero no es la mejor forma de hacerlo
        time.sleep(1)
        comprar_producto()


    except KeyboardInterrupt:   #Evitamos que se produzca un crasheo si el usuario presiona Ctrl+C
        print(bcolors.FAIL + "\nERROR: " + bcolors.ENDC + "Por favor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        comprar_producto()  # Llamada recursiva para mantener contexto


def gestionar_cuenta():
    try:    #Intenta ejecutar el código, si hay un error, se ejecuta el except
        global user #Definimos la variable global "user" para poder acceder a ella en la función
        print(bcolors.OKCYAN+bcolors.UNDERLINE+"Gestionar cuenta"+bcolors.ENDC)
        print("1.- Cambiar contraseña")
        print("2.- Borrar cuenta")
        print("3.- Volver al menú principal")
        opcion = input(bcolors.WARNING+"Ingrese una opción: "+bcolors.ENDC)

        if opcion == "1":
            os.system("cls") if os.name == "nt" else os.system("clear")
            cambiar_contraseña()

        elif opcion == "2": #borrar cuenta del usuario en sesion iniciada
            if usuario_sesion in usuarios:  #Validar que el usuario en sesión exista en el diccionario
                del usuarios[usuario_sesion]    #Eliminar el usuario en sesión del diccionario
                print(bcolors.OKGREEN+"Cuenta eliminada exitosamente.")
                time.sleep(1.5)
                os.system("cls") if os.name == "nt" else os.system("clear")
                main_menu()

        elif opcion == "3":
            os.system("cls") if os.name == "nt" else os.system("clear")
            menu_user()
        else:
            print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            gestionar_cuenta()
            
    except ValueError:  #si el usuario ingresa un valor no valido, se ejecutara el siguiente mensaje
        print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        gestionar_cuenta()

    except KeyboardInterrupt:   #Evitamos que se produzca un crasheo si el usuario presiona Ctrl+C
        print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        gestionar_cuenta()


def cambiar_contraseña():
    global user     #Definimos la variable global "user" para poder acceder a ella en la función
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Cambiar ontraseña\n"+bcolors.ENDC)
    print("Para volver, escriba 'Q'")
    oldpass = getpass.getpass(bcolors.WARNING+"Ingrese su contraseña actual: "+bcolors.ENDC)  #Solicitar la contraseña actual del usuario en sesión
    if oldpass == "q" or oldpass == "Q":        #Si el usuario ingresa "q" o "Q", se regresará al menú de gestión de cuenta
        os.system("cls") if os.name == "nt" else os.system("clear")
        gestionar_cuenta()

    if oldpass != usuarios[user]["contraseña"]:     #Validar que la contraseña ingresada sea igual a la contraseña actual del usuario en sesión
        print(bcolors.FAIL+"Contraseña incorrecta.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        cambiar_contraseña()
    
    elif oldpass == "":     #Validar que la contraseña no esté vacía
        print(bcolors.FAIL+"La contraseña no puede estar vacía.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        cambiar_contraseña()
    
    if oldpass == usuarios[user]["contraseña"]:     #Validar que la contraseña ingresada sea igual a la contraseña actual del usuario en sesión
        newpass = getpass.getpass(bcolors.WARNING+"Ingrese su nueva contraseña: "+bcolors.ENDC)


    if newpass == "q" or newpass == "Q":        #Si el usuario ingresa "q" o "Q", se regresará al menú de gestión de cuenta
        os.system("cls") if os.name == "nt" else os.system("clear")
        gestionar_cuenta()

    if newpass == usuarios[user]["contraseña"]:     #Validar que la nueva contraseña no sea igual a la contraseña actual del usuario en sesión
        print(bcolors.FAIL+"La contraseña no puede ser igual a la anterior.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        cambiar_contraseña()

    elif newpass == "":     #Validar que la nueva contraseña no esté vacía
        print(bcolors.FAIL+"La contraseña no puede estar vacía.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        cambiar_contraseña()

    elif len(newpass) < 8:  #Validar que la nueva contraseña tenga mínimo 8 carácteres
        print(bcolors.FAIL+"La contraseña debe tener mínimo 8 carácteres.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        cambiar_contraseña()

    usuarios[user]["contraseña"] = newpass      #Cambiar la contraseña del usuario en sesión por la nueva contraseña ingresada
    print(bcolors.OKGREEN+"Contraseña cambiada exitosamente.")
    time.sleep(1.5)
    os.system("cls") if os.name == "nt" else os.system("clear")
    menu_user()

#En este historial de compras se puede ver a detalle todas las compras realizadas por el usuario en sesion.
def ver_historial_compras():
    global usuario_sesion   #Se declara la variable global para poder usarla en la función
    print(bcolors.OKCYAN+bcolors.UNDERLINE+"Historial de compras\n"+bcolors.ENDC)
    #Se imprime el historial de compras del usuario en sesión, con formato tabla, aplicando algunos colores.
    print(bcolors.OKGREEN+"     Producto\t\t   "+bcolors.ENDC+"|"+bcolors.OKGREEN+"    Precio     "+bcolors.ENDC+"|"+bcolors.OKGREEN+" Cantidad  "+bcolors.ENDC+"|"+bcolors.OKGREEN+"     Total      "+bcolors.ENDC+"|"+bcolors.OKGREEN+"   Fecha   /   Hora"+bcolors.ENDC)
    print("-"*95)
    if usuario_sesion in hist_compras: #Si el usuario en sesión tiene compras, se mostrarán en pantalla
        for v in hist_compras[usuario_sesion]: #Recorre el historial de compras del usuario en sesión y muestra el valor
            print(f"  {v['producto']:<25}| "+bcolors.OKGREEN+"$"+bcolors.ENDC+f"{v['precio']:<6}  USD  |    {v['cantidad']:<6} |  "+bcolors.OKGREEN+"$"+bcolors.ENDC+f"{v['total']:<6}  USD  |  {v['fecha']}")
    else:   #Si el usuario en sesión no tiene compras, se mostrará un mensaje en pantalla
        print(bcolors.HEADER+"Haz una compra y podrás ver el registro de tus compras aquí."+bcolors.ENDC)
    print("-"*95 + "\n")
    os.system("pause")
    os.system("cls") if os.name == "nt" else os.system("clear")
######################################
#   #   #   Menu principal   #   #   #
######################################

def main_menu():
    os.system("cls") if os.name == "nt" else os.system("clear")
    try: #aplicamos el try para evitar errores en el programa
        print(bcolors.OKCYAN+"Bienvenido/a a MyGamingSetup"+bcolors.ENDC)
        print(bcolors.OKGREEN+"*Para poder acceder a nuestro catálogo de productos, porfavor "+bcolors.WARNING+bcolors.UNDERLINE+"Registrate"+bcolors.ENDC+bcolors.OKGREEN+" o "+bcolors.WARNING+bcolors.UNDERLINE+"Inicia sesión.\n"+bcolors.ENDC)
        print("1.-Registrate")
        print("2.-Iniciar Sesión")
        print("3.-Salir del programa\n")
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
                    f  """+bcolors.ENDC+"o"+bcolors.ENDC+bcolors.OKBLUE+"""|  """+bcolors.ENDC+"o"+bcolors.OKBLUE+"""|__     "`-.   """+bcolors.ENDC+"""~   Nos vemos pronto crack! """+bcolors.ENDC+ bcolors.OKBLUE+"""
                    ,-._.,--'_ `.   _.,-`
                    `"' ___.,'` j,-'
                      `-.__.,--'
                     

                    """+bcolors.ENDC) #Mensajito de despedida
        else:
            print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
            time.sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            main_menu() #se vuelve a llamar a la funcion para que el usuario pueda ingresar una opcion valida

    except ValueError: #si el usuario ingresa un valor no valido, se ejecutara el siguiente mensaje
        print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        main_menu()
        
    except KeyboardInterrupt:   #Evitamos que se produzca un crasheo si el usuario presiona Ctrl+C
        print(bcolors.FAIL+"\nERROR: "+bcolors.ENDC+"porfavor, ingrese una de las opciones en pantalla.")
        time.sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        main_menu()
        
os.system("cls") if os.name == "nt" else os.system("clear") #Limpiamos un poco la pantalla para ver mejor el programa
main_menu()                                                 #llamamos a la funcion para que se ejecute el programa
