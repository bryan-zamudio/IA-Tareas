class Nodo:
    def __init__(self,data): # Creamos el constructor para el nodo
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data: # Verificamos si el nodo ya tiene un valor
            if data < self.data:
                if self.left is None:
                    self.left = Nodo(data) # Si el dato a ingresar es menor, se ingresa a la izquierda
                else:
                    self.left.insert(data) # Si ya hay valor a la izquierda llamamos de nuevo al método
            elif data > self.data:
                if self.right is None:
                    self.right = Nodo(data) # Si el dato a ingresar es mayor, se ingresa a la derecha
                else:
                    self.right.insert(data) # Si ya hay valor a la derecha llamamos de nuevo al método
        else:
            self.data = data   # Si el nodo está vacío, se inserta el valor     

    def recInorden(self, raiz): # Método para recorrer el árbol en inorden
        Res = []  # Creamos una lista vaciae n donde guardar los valores
        if(raiz):
            Res = Res + self.recInorden(raiz.left) # Pasamos al nodo izquierdo
            Res.append(raiz.data) # Si ya no hay nodo izquierdo, añadimos el valor a la lista
            Res = Res + self.recInorden(raiz.right) # Pasamos al nodo derecho
        return Res # Se van añadiendo los nodos de uno en uno a la lista por la recursividad
    
    def recPreorden(self, raiz): # Método para recorrer el árbol en preorden
        Res = []
        if(raiz):
            Res.append(raiz.data) # Añadimos la raiz a la lista
            Res = Res + self.recPreorden(raiz.left) # Después recorremos a la izquierda
            Res = Res + self.recPreorden(raiz.right) # Después a la derecha
        return Res
    
    def recPostorden(self, raiz): # Método para recorrer el árbol en postorden
        Res = []
        if(raiz): # Vamos añadiendo los nodos a la lista, de izquierda a derecha a la raiz
            Res = Res + self.recPostorden(raiz.left)
            Res = Res + self.recPostorden(raiz.right)
            Res.append(raiz.data)
        return Res
    def busquedaArbol(self, valor): # Método para buscar un valor
        if self.data == valor:
            return True
        elif valor < self.data:
            if self.left:
                return self.left.busquedaArbol(valor)
        elif valor > self.data:
            if self.right:
                return self.right.busquedaArbol(valor)
        return False

# Insertamos los valores al árbol
raiz = Nodo(50)
raiz.insert(15)
raiz.insert(17)
raiz.insert(89)
raiz.insert(22)
raiz.insert(44)
raiz.insert(33)
raiz.insert(65)
raiz.insert(94)    

# Menú para elegir el recorrido
while True:
    print('\n1. Recorrido Inorden \n2. Recorrido Preorden \n3. Recorrido Postorden \n4. Buscar un valor \n5. Insertar valor al árbol \n6. Salir')
    opcion = input('\nOpción: ')
    if( opcion == '1'):
        print(raiz.recInorden(raiz))
    elif(opcion == '2'):
        print(raiz.recPreorden(raiz))
    elif(opcion == '3'):
        print(raiz.recPostorden(raiz))
    elif(opcion == '4'):
        valor = (int(input('\nIngresa el valor a buscar: ')))
        if(raiz.busquedaArbol(valor)):
            print('\nEl valor se encuentra en el árbol')
        else:
            print('\nEl valor no se encuentra en el árbol')
    elif(opcion == '5'):
        insertar = int(input('\nValor a insertar: '))
        raiz.insert(insertar)
    elif(opcion == '6'):
        break
    else:
        print('\nOpción invalida')