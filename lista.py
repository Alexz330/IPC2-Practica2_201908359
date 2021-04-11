from Nodo import Nodo

class doble:
    def __init__(self):
        self.primero =None
        self.ultimo = None
        self.size = 0
    
    def vacia(self):
        return self.primero == None

    def Append(self,nombre,apellido,telefono):
        if self.vacia():
            self.primero = self.ultimo = Nodo(nombre,apellido,telefono)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(nombre,apellido,telefono)
            self.ultimo.anterior = aux
        self.size +=1
    
    def agregar_inicio(self,nombre,apellido,telefono):
        if self.vacia():
            self.primera = self.ultimo = Nodo(nombre,apellido,telefono)
        else:
            aux = Nodo(nombre,apellido,telefono)
            aux.siguiente = self.primero
            self.primero.anterior =aux
            self.primero = aux 
        self.size +=1

    def recorrer_inicio(self):
        aux = self.primero
        print("Agenda\n")
        while aux:
            
            print("Nombre:")
            print(aux.nombre)
            print("Apellido:")
            print(aux.apellido)
            print("Telefono:")
            print(str(aux.telefono) + "\n")
            aux = aux.siguiente 

    def recorrer_fin(self):
        aux = self.ultimo

        while aux:
            print("Agenda\n")
            print("Nombre:")
            print(aux.nombre)
            print("Apellido:")
            print(aux.apellido)
            print("Telefono:")
            print(str(aux.telefono) + "\n")
            aux = aux.anterior

    def iterar(self):
        actual = self.primero

        while actual:
            nombre = actual.nombre
            apellido = actual.apellido
            telefono = actual.telefono
            
            
            actual = actual.siguiente
            yield telefono, nombre,  apellido

    def buscar(self, telefono):

        for d in self.iterar():
            if telefono == d:
                print(d)
                return True
        return False