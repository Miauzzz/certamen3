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
    "monitor" : {"nombre" : "Monitor - Azuls VG24",         "precio" : 125.00,    "stock" : 10,   "tipo": "monitor"},
    "teclado" : {"nombre" : "Teclado - Jayperex FPS",       "precio" : 60.00,     "stock" : 10,   "tipo": "teclado"},
    "mouse"   : {"nombre" : "Mouse - Jayperex Surge",       "precio" : 30.00,     "stock" : 10,   "tipo": "mouse"},
    "cpu"     : {"nombre" : "CPU - kore y9-1",              "precio" : 150.00,    "stock" : 30,   "tipo": "cpu"},
    "gpu"     : {"nombre" : "Tarjeta de video - RTK 4100",  "precio" : 300.00,    "stock" : 23,   "tipo": "gpu"},
    "ram"     : {"nombre" : "RAM - Cruzar Valistic",        "precio" : 20.00,     "stock" : 4,    "tipo": "ram"},
    "gabinete": {"nombre" : "Gabinete - MSY m315",          "precio" : 45.00,     "stock" : 1,    "tipo": "gabinete"},
    "placa"   : {"nombre" : "Placa - Yigabait h312-v",      "precio" : 43.00,     "stock" : 30,   "tipo": "placa"},
}



def ver_productos():
    print("   Tipo   |\t\t    Nombre    \t\t|\t   Precio  \t |  Stock")
    print("-"*85)
    for k,v in productos.items():
        print(f"{v['tipo']:<9} | {v['nombre']:<35} |\t${v['precio']:<10}USD\t |    {v['stock']:<17}\n")

def comprar_producto():
    producto_comprar = input("\nSeleccione un producto: ")
    
    # Validar la existencia del producto
    if producto_comprar not in productos:
        print("El producto seleccionado no existe.")
        return
    
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
    

ver_productos()
comprar_producto()
ver_productos()