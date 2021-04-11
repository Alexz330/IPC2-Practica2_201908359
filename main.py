from lista import doble

def PantallaInicial():
    print("IPC2, Seccion E, 201908389")
    input("Presiona cualquier boton para continuar: ")
    MenuPrincipal()

lista = doble()


"""def asignar(lista0):
    listas_ordenar = []
    for i in range(0,len(lista)):
    return listas_ordenar"""

def MenuPrincipal():
    print("--------------Bienvenido al menu, ingresa la opcion que desees--------------")
    print("1. Ingrese nuevo contacto")
    print("2. Buscar contacto")
    print("3. visualizar agenda")
    
    print()
    opselect = input()
    if opselect == "1":
        
        ingresar_Contacto()
        
    elif opselect == "2":
        #lista2 = asignar(lista)
        B_contacto(telefono)
    elif opselect == "3":
        visualizar_contacto()
    elif opselect == "4":
        Opcion4(lista)
    else:
        print("Opcion inexistente")
        MenuPrincipal()



def ingresar_Contacto():
    global telefono

    nombre1 = input("Ingrese nombre:")
    apellido1 = input("Ingrese apellido:")
    telefono = input("Ingrese telefono:")

    

    lista.Append(nombre1,apellido1,telefono)
    lista.recorrer_inicio()
    print("Contacto agregado exitoosamente")
    print("")
    MenuPrincipal()

def B_contacto(telefono):

    print("ingrese numero de telefono a buscar:")

    telefono = int(input("No.Telefono: "))
    
    if lista.buscar(telefono):
        print(telefono)
        lista.recorrer_inicio()

        


    




if __name__ == '__main__':
    PantallaInicial()
