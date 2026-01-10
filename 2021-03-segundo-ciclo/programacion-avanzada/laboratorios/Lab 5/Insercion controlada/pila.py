from nodo import Nodo

class Pila:
    def __init__(self, max = -1):
        self.tope = None
        self.tamaño = 0
        self.max = max

    def insertar(self, nombre, editorial, isbn):
        def guardar(self, nombre, editorial, isbn):
            nuevo_libro = Nodo(nombre, editorial, isbn)
            nuevo_libro.siguiente = self.tope
            self.tope = nuevo_libro
            self.tamaño += 1
        # Se hace la verificación de que exista al menos un dato en la pila, entonces cuando el isbn no sea igual a uno que ya esté en la pila se ingresará el dato
        # de lo contrario va a generar un error y se mostrará un mensaje de que no se va a guardar ese libro porque ya existe
        if self.tope != None:
            aux = self.tope
            if aux.isbn != isbn:
                guardar(self, nombre, editorial, isbn)
            else:
                raise Exception('El libro ya existe y no será guardado')
        else:
            guardar(self, nombre, editorial, isbn)
                
    def recorrer(self):
        aux = self.tope
        while True:
            if aux == None:
                break
            else:
                print(aux)
                aux = aux.siguiente
    
    def eliminar(self):
        if self.tope == None:
            raise Exception('ERROR: Subdesbordamiento de pila')
        else:
            aux = self.tope
            self.tope = self.tope.siguiente
            aux.siguiente = None
            self.tamaño -= 1
            return aux