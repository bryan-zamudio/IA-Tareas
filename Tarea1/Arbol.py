from bigtree import *

# Declaramos los nodos
raiz = BinaryNode("a", valor=60)
b = BinaryNode("b", valor=50)
c = BinaryNode("c", valor=30)
d = BinaryNode("d", valor=23)
e = BinaryNode("e", valor=77)
f = BinaryNode("f", valor=69)
g = BinaryNode("g", valor=55)
h = BinaryNode("h", valor=10)
i = BinaryNode("i", valor=44)

# Establecemos la jerarquía
raiz.children = [b, c]
b.children = [d, e]
d.children = [f, g]
c.children = [h, i]



while True:
    print('\n1. Mostrar árbol \n2. Buscar un valor \n3. Salir')
    opcion = input('Opción: ')

    if opcion == '1': 
        raiz.show()     # Imprimimos el arbol en la consola con el método show
    elif opcion == '2':
        valor = int(input('Ingresa el valor a buscar: '))
        valor_busqueda = find(raiz, lambda node: node.valor == valor)  # Buscamos el valor ingresado utilizando el método find

        if(valor_busqueda):
            print(f"\nNodo encontrado: {valor_busqueda.node_name}, con valor {valor_busqueda.valor}") # Imprimimos el nombre del nodo y el valor                                                                                      
        else:
            print("No se encontro el nodo")

    elif opcion == '3':
        break
    else:
        print('\nIngresa un número válido')
    
