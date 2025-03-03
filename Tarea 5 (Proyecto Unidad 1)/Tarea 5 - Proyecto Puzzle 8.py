import time

# Función para calcular la distancia Manhattan mediante la diferencia entre las coord. del tablero actual y el tablero resuelto
def dist_Manhattan(tab, meta):
    dist = 0
    for i in range(1, 9):
        xi, yi = divmod(tab.index(i), 3)    # Usamos divmod para convertir el index en coordenadas
        xr, yr = divmod(meta.index(i), 3)   # Al obtener las coordenadas podemos ver qué tan lejos está del tablero resuelto
        dist += abs(xi - xr) + abs(yi - yr) # Sumamos a la distancia Manhattan restando el tablero actual con el tablero resuelto
    return dist

# Función con diferente fórmula, calcula la distancia en términos de cuántos cuadros están en la posición correcta. Bastante ineficiente en comparación
def dist_Cuadros(tab, meta):
    dist = 0
    for i in range(1, 9):
        xi, yi = divmod(tab.index(i), 3)    # Usamos divmod para convertir el index en coordenadas
        xr, yr = divmod(meta.index(i), 3)   # Al obtener las coordenadas podemos ver qué tan lejos está del tablero resuelto
        if (xi, yi) != (xr, yr):            # Verificamos si el numero está en el mismo lugar que el tablero resuelto
            dist += 1
    return dist


# Función para checar los vecinos, basándose en los movimientos posibles
def ver_Vecinos(tab):
    vecinos = []                # Lista donde se guardarán los vecinos
    cero_Idx = tab.index(0)     # Obtenemos el index del 0, para poder obtener sus coordenadas
    x_Cero, y_Cero = divmod(cero_Idx, 3)
    movms = {'arriba': -3, 'abajo': 3, 'izquierda': -1, 'derecha': 1} # Diccionario para los movimientos

    # Recorremos el diccionario
    for mov, dif in movms.items():
        # Verificamos que el movimiento sea posible
        if mov == 'arriba' and x_Cero > 0 or \
           mov == 'abajo' and x_Cero < 2 or \
           mov == 'izquierda' and y_Cero > 0 or \
           mov == 'derecha' and y_Cero < 2:
            nvo_idx = cero_Idx + dif    # Sumamos el valor del movimiento al index actual
            nvo_tab = list(tab)         # Tablero auxiliar
            nvo_tab[cero_Idx], nvo_tab[nvo_idx] = nvo_tab[nvo_idx], nvo_tab[cero_Idx] # Intercambiamos las posiciones del tablero inicial y el nuevo
            vecinos.append(tuple(nvo_tab))  # Añadimos a la lista vecinos el tablero resultante
    return vecinos

# Algoritmo A*
def a_Estrella(tab, meta, opcion):
    if (opcion == 1):
        opcion_Dist = dist_Manhattan
    elif(opcion == 2):
        opcion_Dist = dist_Cuadros

    # Lista de tuplas para guardar: (costo total, costo para llegar al estado actual, estado actual, camino seguido)
    posibles = [(0 + dist_Manhattan(tab, meta), 0, tab, [])]
    explorados = set()  # Creamos un set para guardar los nodos explorados
    i = 0
    print("Exploración Completa: \n")
    nvo_Costo = 0

    while posibles:
        i += 1
        print('Nodo explorado N° ' + str(i), ' con profundidad de ' + str(nvo_Costo))

        # Encontramos el nodo con el menor costo total de la lista (f(n))
        costo_Actual, costo, estado_Actual, camino = min(posibles, key=lambda x: x[0])
        # Lo removemos de la lista de posibles
        posibles.remove((costo_Actual, costo, estado_Actual, camino))
        print_puzzle(estado_Actual)
        # Si se encontró el estado meta, se retorna el caminito
        if estado_Actual == meta:
            return camino + [estado_Actual]

        # Añadimos el estado actual al set de explorados
        explorados.add(estado_Actual)

        # Vemos cuáles son los vecinos del estado actual
        for vecino in ver_Vecinos(estado_Actual):
            if vecino not in explorados:
                nvo_Costo = costo + 1
                costo_Total = nvo_Costo + opcion_Dist(vecino, meta)                         # Checamos la distancia del vecino
                posibles.append((costo_Total, nvo_Costo, vecino, camino + [estado_Actual])) # Añadimos el vecino a la lista
        
        if(i >= 10000):
            return False

# Función para imprimir el estado del puzzle en 3x3
def print_puzzle(estado):
    for i in range(0, 9, 3):
        print(estado[i:i+3])    # Imprimimos la lista de 3 en 3 para simular un tablero 3x3
    print() 

# Puzzle inicial y objetivo
tab_inicial =   (1, 2, 3,\
                4, 0, 5,\
                6, 7, 8)
tab_resuelto =  (1, 2, 3,\
                4, 5, 6, \
                7, 8, 0)

# Ejecutar el algoritmo A*
opcion = 0
while opcion < 1 or opcion > 2:    
    opcion = int(input('Ingresa la heurística a escoger: \n1. Distancia Manhattan \n2. Distancia Cuadros\n'))
solucion = a_Estrella(tab_inicial, tab_resuelto, opcion)

if (solucion == False):
    print('No se encontró solución')
else:
    print('Camino óptimo: \n')
    # Imprimimos los elementos de la lista de uno en uno
    for step in solucion:
        print_puzzle(step)
        time.sleep(0.5)  # Pausa de medio segundo entre cada paso para que se vea emocionante

