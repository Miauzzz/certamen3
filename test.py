# Certamen 3 - 30%

#Archivo .py para testear funciones y practicar con listas.

#librerias
import os
import sys
import time
import datetime


#################################
#   #   #   variables   #   #   #
#################################
usuarios = {
    "admin" : {"usuario" : "admin", "contraseña": "admin", id: 0},
    "test": {"usuario" : "test", "contraseña": "test", "id": 1},
}

productos = {
    "1" : {"id":1,"nombre" : "Monitor - Azuls VG24",         "precio" : 125.0,    "stock" : 10,   "tipo": "monitor"},
    "2" : {"id":2,"nombre" : "Teclado - Jayperex FPS",       "precio" : 60.0,     "stock" : 10,   "tipo": "teclado"},
    "3" : {"id":3,"nombre" : "Mouse - Jayperex Surge",       "precio" : 30.0,     "stock" : 10,   "tipo": "mouse"},
    "4" : {"id":4,"nombre" : "CPU - kore y9-1",              "precio" : 150.0,    "stock" : 30,   "tipo": "cpu"},
    "5" : {"id":5,"nombre" : "Tarjeta de video - RTK 4100",  "precio" : 300.0,    "stock" : 23,   "tipo": "gpu"},
    "6" : {"id":6,"nombre" : "RAM - Cruzar Valistic",        "precio" : 20.0,     "stock" : 4,    "tipo": "ram"},
    "7" : {"id":7,"nombre" : "Gabinete - MSY m315",          "precio" : 45.0,     "stock" : 1,    "tipo": "gabinete"},
    "8" : {"id":8,"nombre" : "Placa - Yigabait h312-v",      "precio" : 43.0,     "stock" : 30,   "tipo": "placa"},
}

historial_compras = {
    "Historial": {"user": "test", "id":"1", "producto": "Monitor - Azuls VG24", "precio": 125.00, "cantidad": 1, "total": 125.00, "fecha": "2021-06-01"}}


for k,v in historial_compras.items():
    print("Historial de compras\n")
    print("Usuario (id) |      Producto            |    Precio    | Cantidad  |   Total   |  Fecha")
    print("-"*95)
    print(f" {v['user']}  ({v['id']})   | {v['producto']}     |    {v['precio']}     |     {v['cantidad']}     |   {v['total']}   | {v['fecha']}")
    print("-"*95 + "\n")








def ver_productos():
    print("    ID\t|      Tipo\t  |\t\tNombre\t\t\t|      Precio\t |   Stock")

    print("-"*95)
    for k,v in productos.items():
        print(f"    {v['id']:<4}|  {v['tipo']:<15}| {v['nombre']:<36}|   ${v['precio']:<5} USD\t |    {v['stock']:<17}\n") #Ajustes de impresión para que se vea bonito
    print("-"*95 + "\n")


def agregar_productos():
    print("Agregar productos\n")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    tipo = input("Ingrese el tipo de producto: ")
    id = len(productos) + 1
    productos[str(id)] = {"id": id, "nombre": nombre, "precio": precio, "stock": stock, "tipo": tipo}
    print("Producto agregado exitosamente.")
    ver_productos()








#Registrar usuario
# def register():
#     print("Registrate\n")
#     user = input("Ingrese un nombre de usuario: ")
#     password = input("Ingrese una contraseña: ")
#     if user in usuarios:
#         print("El usuario ya existe.")
#     else:
#         usuarios[user] = {"usuario": user, "contraseña": password}
#         print("Usuario registrado exitosamente.")
        


#Iniciar sesión
# def login():
#     print("Iniciar sesión\n")
#     user = input("Ingrese su nombre de usuario: ")
#     password = input("Ingrese su contraseña: ")
#     if user in usuarios and usuarios[user]["contraseña"] == password:
#         print(f"Bienvenido, {user}!")
#     else:
#         print("Usuario o contraseña incorrectos.")

# def cambiar_contraseña(user):
#     print("Cambio de contraseña\n")
#     nueva_contraseña = input("Ingrese su nueva contraseña: ")
#     usuarios[user]["contraseña"] = nueva_contraseña
#     print("Contraseña cambiada exitosamente.")


# register()
# login()
# print(usuarios)
# cambiar_contraseña(user="")
# print(usuarios)






# def comprar_producto():
#     producto_comprar = input("\nSeleccione un producto: ")
    
#     # Validar la existencia del producto
#     if producto_comprar not in productos:
#         print("El producto seleccionado no existe.")
#         return
    
#     while True:
#         try:
#             cantidad = int(input("Ingrese la cantidad: "))
#             if cantidad <= 0:
#                 print("Por favor, ingrese un número mayor a 0.")
#                 continue
#             if productos[producto_comprar]["stock"] < cantidad:
#                 print("Lo sentimos, no hay suficiente stock del producto seleccionado.")
#             else:
#                 productos[producto_comprar]["stock"] -= cantidad
#                 print(f"Total a pagar: ${productos[producto_comprar]['precio']*cantidad} USD")
#                 break  # Salir del bucle si la compra es exitosa
#         except ValueError:
#             print("Por favor, ingrese un número válido.")
    

# ver_productos()
# comprar_producto()
# ver_productos()
