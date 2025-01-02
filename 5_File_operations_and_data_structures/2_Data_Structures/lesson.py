# Data structures

# Le strutture dati sono progettate per gestire/organizzare i dati 
# in modo da ottimizzare le operazioni comuni: 
# come l’inserimento di nuovi elementi, l’eliminazione di elementi, 
# la ricerca e anche l’ordinamento.

# implementare una queue in python

'''
# dobbiamo importare la classe deque 
# dal modulo collections
from collections import deque

# la deque è una sorta di linked list
# deque significa double ended queue

# istanziamo un oggetto deque
queue = deque()

# la queue segue il principio FIFO
# First In, First Out

# la classe deque fornisce metodi per implementare questo principio

# il metodo append() serve per effettuare l'enque (aggiungere elemento)

queue.append('a')
queue.append('b')
queue.append('c')

#print(queue)

# la classe deque è un implementazione della classica queue
# quindi anche se le code non sono indicizzate
# utillzzando la classe deque è possibile accedere 
# ad un elemento tramite il suo indice

#print(queue[0])

# per effettuare il dequeue (rimuovere un elemento)
# si utilizza il metodo popleft()
# simile al metodo pop() - rimuove l'ultimo elemento
# ma il metodo popleft() rimuove il primo elemento
# rispettando il principio FIFO

# inoltre come il metodo pop()
# oltre a rimuovere l'elemento dalla queue
# il metodo popleft() restituisce l'elemento rimosso

print(queue.popleft())

print(queue)

# aggiungendo un nuovo elemento
# verrà inserito per ultimo

queue.append('d')

# rimuovendo un ulteriore elemento
# verrà rimosso l'elemento b
# in quanto, dopo aver rimosso a
# è diventato primo elemento della lista

queue.popleft()

print(queue)
'''

# implementare uno stack in python

# anche in questo caso dobbiamo importare 
# la classe deque dal modulo collections

# lo stack rispetta il principio 
# LIFO Last In, First Out

from collections import deque

stack = deque()

# utilizziamo sempre il metodo append()
# per aggiungere elementi

stack.append('a')
stack.append('b')
stack.append('c')

print(stack)

# per rimuovere un elemento
# utilizziamo il metodo pop()
# perchè in questo caso
# l'ultimo aggiunto sarà il primo ad essere rimosso

print(stack.pop())

print(stack)

# dopo aver rimosso l'elemento 
# ne aggiungiamo un nuovo
stack.append('d')

# utilizziamo il metodo pop()
# per rimuovere l'ultimo elemento
# quello appena aggiunto
print(stack.pop())

print(stack)



