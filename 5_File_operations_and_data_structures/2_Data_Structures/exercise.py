'''
Inizializza una struttura dati adatta a gestire,
una collezione di siti web visitati (stringhe).
Ora definisci un ciclo infinito,
in cui viene richiesto all'utente quale sito vuole visitare.
Il sito immesso viene aggiunto alla collezione.
Se però l'utente immette il carattere <
significa che vuole tornare indietro al sito precedente,
rimuovi l'ultimo sito della collezione.
A fine iterazione il ciclo stampa
il sito su cui l'utente si trova attualmente.
'''

'''
from collections import deque

history = deque()

while True:

    user_input = input('Quale nuovo sito vuoi visitare? Digita < per tornare al precedente ').strip()

    if user_input != '<':

        history.append(user_input)
        
    elif len(history) > 1:
        
        history.pop()
        print(f'Attualmente stai visitando {history[-1]}...')
    
    else:
        
        print('Ti trovi sulla homepage')
'''

'''
Crea una classe che implementa la struttura dati Queue.
Possiede un attributo che rappresenta la collezione,
e due metodi, enqueue e dequeue,
che servono rispettivamente per aggiungere e rimuovere 
un elemento dalla collezione
(rispettando i principi della Queue).
Istanzia quindi un oggetto della classe e testalo,
per valutare se funziona come atteso.
'''

'''
from collections import deque

class Queue:
    
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return None

    def __str__(self):
        for item in self.queue:
            print(item)

queue_1 = Queue()

queue_1.enqueue('a')
queue_1.enqueue('b')
queue_1.enqueue('c')

print('After enqueue')
print(queue_1.__str__())

queue_1.dequeue()
queue_1.dequeue()
queue_1.dequeue()
queue_1.dequeue()
queue_1.dequeue()

print('After dequeue')
print(queue_1.__str__())
'''

'''
Come fatto nell'esercizio precedente crea una classe,
ma questa volta implementa la struttura dati Stack.
La classe oltre i metodi/attributi dell'esercizio precedente
deve prevedere altri 3 metodi:
- peek: mostra l'elemento in cima allo stack senza rimuoverlo
- is_empty: restituisce True se lo stack è vuoto
- size: restituisce il numero degli elementi nello stack
'''


from collections import deque

class Stack:

    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    
    def __str__(self):
        for item in self.stack:
            print(item)

stack_1 = Stack()

stack_1.push('a')
stack_1.push('b')
stack_1.push('c')

print('After push')
print(stack_1.__str__())

print(stack_1.peek())
print(stack_1.is_empty())
print(stack_1.size())

stack_1.pop()
stack_1.pop()
stack_1.pop()
stack_1.pop()

print('After pop')
print(stack_1.__str__())

