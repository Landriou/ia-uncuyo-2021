class LinkedList:
    head=None

class Node:
    value=None
    nextNode=None

#Añade un elemento a la lista
def add(L, element):
    NodeA = Node()
    NodeA.value = element
    NodeA.nextNode = L.head
    L.head = NodeA
#Devuelve la posicion de un elemento pasado por parametros
def search(L, element):
    currentnode = L.head
    posicion = 0    
    while currentnode != None:
        if currentnode.value == element:
            return posicion
        posicion = posicion + 1
        currentnode = currentnode.nextNode
    return None

#Devuelve la cantidad de elementos en la lista
def length(L):
    currentnode = L.head
    cant = 0
    while currentnode != None:
        cant = cant + 1
        currentnode = currentnode.nextNode
    return cant
#Inserta un elemento en la posicion indicada
def insert(L, element,position):
    flag = True
    contador = 0 
    
    if length(L) < position:
        return None
    if position == 0:
        add(L, element)
        return position
    nodoanterior = 0
    nodoposterior = 0
    Nodo = Node()
    Nodo.value = element
    currentnode = L.head
    while flag: #Copio los punteros de los nodos adyacentes
        contador = contador + 1
        if contador == position:
            flag = False
        if contador == 1:
            nodoanterior = currentnode
            nodoposterior = currentnode.nextNode
        else:
            nodoanterior = nodoposterior
            nodoposterior = nodoposterior.nextNode
    nodoanterior.nextNode = Nodo
    Nodo.nextNode = nodoposterior
    return position
#Elimino un elemento de la lista copiando punteros
#De igual forma q en insert
def delete(L, element):
    if search(L, element) == None:
        return None
    flag = True
    contador = 0 
    nodoanterior = 0
    nodoposterior = 0
    currentnode = L.head
    if search(L,element) == 0:
        for n in range(length(L)-1):
            currentnode.value = currentnode.nextNode.value
            if n != length(L)-2:
                currentnode = currentnode.nextNode
        currentnode.nextNode = None
        return search(L,element)
    while flag:
        contador = contador + 1
        if contador == search(L, element):
            flag = False
        nodoanterior = currentnode
        nodoposterior = currentnode.nextNode.nextNode
        currentnode = currentnode.nextNode
    nodoanterior.nextNode = nodoposterior
    return search(L,element)
#Devuelve el valor de la posicion indicada
def access(L, position):
    flag = True
    contador = 0
    currentnode = L.head
    value = 0
    if length(L) < position:
        return None
    while flag:
        if contador == position:
            flag = False
        value = currentnode.value
        currentnode = currentnode.nextNode
        contador = contador + 1
    return value
#Cambia el valor de la posicion indicada por el elemento indicado
def update(L, element, position):
    flag = True
    contador = 0
    currentnode = L.head
    if position > length(L):
        return None
    
    while flag:
        if contador == position:
            flag = False
            currentnode.value = element
        contador = contador + 1
        currentnode = currentnode.nextNode
    return position


def deleteposition(L, position):
    if position >= length(L):
        return None
    flag = True
    contador = 0 
    nodoanterior = 0
    nodoposterior = 0
    currentnode = L.head
    if position == 0:
        # for n in range(length(L)-1):
        #     currentnode.value = currentnode.nextNode.value
        #     if n != length(L)-2:
        #         currentnode = currentnode.nextNode
        # currentnode.nextNode = None
        # return position
        L.head = currentnode.nextNode
        currentnode.nextNode = None
        currentnode = L.head
        return position
    while flag:
        contador = contador + 1
        if contador == position:
            flag = False
        nodoanterior = currentnode
        nodoposterior = currentnode.nextNode.nextNode
        currentnode = currentnode.nextNode
    nodoanterior.nextNode = nodoposterior
    return position

def switch(L,position1,position2):
    currentnode = L.head
    nodo1 = access(L, position1)
    nodo2 = access(L, position2)
    update(L,nodo2,position1)
    update(L, nodo1, position2)

def imprimirlista(L):
    currentnode = L.head
    while currentnode != None:
        print(currentnode.value, end="  ")
        currentnode = currentnode.nextNode

def inverse(L):
    if length(L) == 0:
        return None
    Linverse = LinkedList()
    Linverse.head = accesposition(L,length(L)-1) #Asigno el head de la otra lista al ultimo nodo
    for n in range(length(L)-1,-1,-1):
        punteroactual = None
        punteroanterior = None
        if n == 0:
            accesposition(L,n).nextNode = None #Al ultimo nodo le pongo none
            return Linverse #Y retorno la lista inversa
        punteroactual = accesposition(L,n) #guardo el puntero de la posicion actual
        punteroanterior = accesposition(L,n-1) #Y el de la anterior
        punteroactual.nextNode = punteroanterior #Conecto el de la derecha al de la izquierda
    
#Funcion que devuelve la puntero donde se encuentra el nodo
def accesposition(L, position):
    flag = True
    contador = 0
    currentnode = L.head
    value = 0
    while flag:
        if contador == position:
            flag = False
        value = currentnode
        currentnode = currentnode.nextNode
        contador = contador + 1
    return value

def Ordenarlista(L,n):
    currentnode = L.head
    mayor = 0
    if n == length(L)-1 :
        return True
    for i in range(length(L)-n):
        if currentnode.value > mayor:
            mayor = currentnode.value
        currentnode = currentnode.nextNode
    move(L,search(L, mayor),length(L)-1-n)
    Ordenarlista(L, n+1)

def move(L,origin, destiny):
    if origin == destiny:
        return None
    punteroorigin = accesposition(L,origin)
    punterodestiny = accesposition(L,destiny)
    antdestiny = accesposition(L,destiny-1)
    nextorigin = punteroorigin.nextNode
    if destiny - origin == 1: #Si los nodos estan al lado
        anteriororigin = accesposition(L,origin-1)

        punteroorigin.nextNode = punterodestiny.nextNode
        punterodestiny.nextNode = nextorigin
        anteriororigin.nextNode = punterodestiny
        nextorigin.nextNode =punteroorigin
        return True
    if destiny == length(L)-1 and origin != 0: #si destino es el final 
        anteriororigin = accesposition(L,origin-1)
        punteroorigin.nextNode = None
        punterodestiny.nextNode = nextorigin
        antdestiny.nextNode = punteroorigin
        anteriororigin.nextNode = punterodestiny
    if origin != 0 and destiny != length(L) -1 : #si el origen es distinto de cero y no es la posicion final
        anteriororigin = accesposition(L,origin-1)

        punteroorigin.nextNode = punterodestiny.nextNode
        punterodestiny.nextNode = nextorigin
        anteriororigin.nextNode = punterodestiny
        antdestiny.nextNode =punteroorigin
    if origin == 0: #Si el origen esta en 0, la logica cambia
        punteroorigin.nextNode = punterodestiny.nextNode
        punterodestiny.nextNode = nextorigin
        antdestiny.nextNode = punteroorigin
        L.head = punterodestiny

#QUEUE
def enqueue(Q, element):
    add(Q,element)

def dequeue(Q):
    if length(Q) == 0:
        return None
    element = access(Q,length(Q)-1)
    deleteposition(Q, length(Q)-1)
    return element

##Stack

def push(S, element):
    add(S, element)

def pop(S):
    if length(S) == 0:
        return None
    element = access(S,0)
    deleteposition(S, 0)
    return element

def imprimirstack(S):
    for n in range(length(S)-1,-1,-1):
        print(access(S,n), end="  ")


#Priority Queue

class PriorityQueue:
    head=None

class PriorityNode:
	value=None
	nextNode=None
	priority=None

def cambiopriori(nodo1, nodo2):
    priori1 = nodo1.priority
    priori2 = nodo2.priority
    nodo2.priority = priori1
    nodo1.priority = priori2

def enqueueWithPriority(Q,element, priority):
    NodeA = PriorityNode()
    NodeA.value = element
    NodeA.priority = priority
    NodeA.nextNode = Q.head
    Q.head = NodeA
    currentnode = Q.head
    position1 = 0
    position2 = 1
    if currentnode.nextNode != None:
        siguiente = currentnode.nextNode
        for n in range(length(Q)-1):
            if currentnode.nextNode != None:
                if currentnode.priority > siguiente.priority:
                    cambiopriori(currentnode,siguiente)
                    switch(Q,position1,position2)
            position1 = position1 + 1
            position2 = position2 + 1
            currentnode = currentnode.nextNode
            if currentnode.nextNode != None:
                siguiente = currentnode.nextNode
    return position1


def dequeueWithPriority(Q):
    if length(Q) == 0:
        return None
    element = access(Q,0)
    deleteposition(Q, 0)
    return element

