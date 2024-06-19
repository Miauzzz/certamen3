#probar cosas
def asd():

    def hola():
        print("Hola mundo")

    def sumar():
        print(2+2)

    def restar():
        print(5-2)

    def default():
        print("Opcion incorrecta")
    switch={1:hola,2:sumar,3:restar}
    opcion = int(input("Ingrese una opcion: "))
    switch.get(opcion,default)()