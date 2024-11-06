# liste

# per creare una lista il literal prevede
# che si utilizzino le [] al cui interno
# inseriamo i valori che vogliamo contenga
# separati da ,

# è buona norma nominare le liste al plurale
clients = ['Lisa', 'Mario', 'Andrea', 'Gino']
#print(type(clients))
#print(clients)

#for client in clients:
#    print(client)

# proprietà
# la lista:
# - accetta valori duplicati
# - accetta valori eterogenei (accetta tutti i data-type in contemporanea, ma non è buona norma)
# - è un insieme di elementi ordinati, grazie all'indice che parte dall'elemento 0
# - è mutabile può variare

# è possibile accedere ad un determinato 
# elemento della lista attraverso il suo indice
#print(clients[1])
# output
#Mario

# se cerco di accedere ad un elemento con un indice non presente nella list
# otteniamo un errore run-time 'Index out of range'
#print(clients[3]) # genera errore

# è possibile accedere ad un elemento della lista 
# utilizzando anche indici negativi
# ad esempio utilizzando -1
# ci si riferisce all'utlimo elemento della lista
#print(clients[-1])
# output
#Gino

# possiamo estrapolare elementi della lista
# indicando un range di valori rappresentanti
# gli indici degli elementi interessati.
# il primo indice è compreso, il secondo escluso
#print(clients[1:3])
# output
#['Mario', 'Andrea']

# indicando solo l'indice di partenza
# estrapoliamo tutti gli elementi a partire
# dall'indice indicato
#print(clients[1:])
# in questo caso prende tutti gli elementi
# partendo dall'indice indicato
#output
#['Mario', 'Andrea', 'Gino']

# indicando l'indice limite del range
# otteniamo tutti gli elementi compresi 
# fino all'indice indicato (indice indicato escluso)
#print(clients[:3])
#output
#['Lisa', 'Mario', 'Andrea']

# accedendo ad un elemento specifico, 
# o estrapolando più elementi
# non stiamo alterando la lista

# mutabilità delle liste
# è possibile modificare un elemento della lista partendo dal suo indice
# assegnando un nuovo valore
#clients[1] = 'Giuseppe'

#for client in clients:
#    print(client)

# metodi delle liste

# append()
# è possibile aggiungere un nuovo elemento nell lista come ultimo
#clients.append('Marco')

#for client in clients:
#	print(client)

# insert() 
# è possibile indicare la posizione in cui vogliamo inserire un nuovo elemento
#clients.insert(1, 'Max')
#print(clients)

# extend()
# permette di aggiungere una lista alla lista origiaria
#clients.extend(['Marco', 'Anna'])
#print(clients)

# è possibile ottenere lo stesso risultato
# utilizzando l'operatore +
# in questo caso l'operatore + serve
# per unire due liste in una nuova lista
#print(clients + ['Marco', 'Anna'])
#print(clients)

# la lista originale clients 
# non è stata modificata in questo modo però
# devo assegnarla ad una nuova variabile
#new_clients = clients + ['Marco', 'Anna']
#print(new_clients)

# remove()
# permette di rimuovere un elemento dalla lista
# accetta come argomento il valore che intendiamo rimuovere
#clients.remove('Mario')
#print(clients)

# pop()
# permette di rimuovere un elemento dalla lista
# accetta come argomento l'indice dell'elemento
# da rimuovere
#clients.pop(1)
#print(clients)

# l'argomento è opzionale
# se omesso viene rimosso l'ultimo elemento della lista
#clients.pop()
#print(clients)

# è possibile utilizzare la parola chiave del
# per rimuovere un elemento dalla lista
# indicando l'indice dell'elemeno che voglio rimuovere
#del clients[1]
#print(clients) 

# la differenza tra il metodo pop() e la keyword del
# risiede nel fatto che il metodo pop() restituisce il valore
# appena rimosso
#deleted_client = clients.pop(1)
#print(deleted_client)
#print(clients)

# clear
# il metodo clear() serve per
# cancellare completamente il contenuto
# di una lista
#clients.clear()
#print(clients)

# è possibile utilizzare del
# per rimuovere completamente la variabile di tipo list
#del clients

# provando a stampare la lista dopo aver utilizzato
# del otteremo errore
#print(clients)

# sort()
# il metodo sort() permette di ordinare gli elementi di una lista
#clients.sort()
#print(clients)

# la funzione sorted
# e differenze con il metodo sort()
#sorted_clients = sorted(clients)
#print(sorted_clients)

# l'operatore in permette di verificare
# se un determinato valore è presente in una lista
# restituisce un valore booleano
#print('Anna' in clients)
#print('Lisa' in clients)

# la funzione len restituisce il numero di elementi
# presenti all'interno di una lista
#print(len(clients))

# assegnare una lista esistente ad una nuova variabile
# entrambe le variabili puntano alla stessa lista 
# qualsiasi modifica fatta tramite una delle due variabili 
# si rifletterà anche sull'altra
#female_clients = clients
#female_clients.remove('Mario')
#female_clients.remove('Andrea')
#female_clients.remove('Gino')

# copy()
#female_clients = clients.copy()
#female_clients.remove('Mario')
#female_clients.remove('Andrea')
#female_clients.remove('Gino')

#print(female_clients)
#print(clients)

# list comprehension
# sintassi breve per creare una nuova lista basata
# su un altra lista

# Creare una copia della lista
#print([client for client in clients])

# Possiamo aggiungere una condizione per includere 
# solo gli elementi che rispettano un certo criterio
#print([client for client in clients if len(client) < 5])

# Applicare una funzione agli elementi
# È possibile applicare funzioni agli elementi 
# mentre vengono aggiunti alla nuova lista
#print([client.upper() for client in clients if len(client) < 5])

# le stringhe sono collezioni di caratteri
# è quindi possibile applicare ciclo for su di esse
name = 'Homer Simpson'
#for char in name:
#    print(char)

# verificare se un determinato carattere è presente 
# in una determinata stringa
#print('H' in name)

# accedere ad un determinato carattere tramite indice
#print(name[2])

# la differenza principle tra string e list
# è che le string non sono mutabili a differenza delle list
#name[2] = 'x' # genera errore! non possiamo mutare una string

#print(sorted(name))
#print(type(sorted(name)))

#print(list(name))
#print(type(list(name)))

# metodi delle string 
# join
# partendo da una list possiamo ottenere
# una string concatenata con un carattere 
# utilizzato come separatore
#ingredients = ['marmellata','pane','burro']
#sandwich = ' & '.join(ingredients)
#print(sandwich)

# split
# partendo da una string possiamo ottenere una list
# indidcando il carattere separatore come argomento
#new_ingredients = sandwich.split(' & ')
#print(new_ingredients)

# la tupla è una lista immutabile e si dichiara con le ()
# è anche possibile omettere le parentesi () 
# ma è buona norma utilizzarle
#days_of_week = ('Lunedi', 'Martedi', 'Mercoledi','Giovedi','Venerdi','Sabato','Domenica')
#days_of_week[0] = 'Monday' # otteniamo errore -> 'tuple' object does not support item assignment

# è possibile dichiarare più variabili contemporaneamente
# attraverso le tuple
a, b = 5, 10

print(a)
print(b)



items = ["fagioli", "noci", "mele"]
split_char = "|"
items.sort()


for item in items:
    print("-", item)


user_item = input("Aggiungi un articolo: ").lower().strip()
if split_char in user_item:
    to_add_items = user_item.split(split_char)
    items.extend(to_add_items)
    print("Articoli aggiunti")
    items.sort()
elif not user_item:
    print("Errore: Non hai inserito alcun articolo")
elif user_item in items:
    print("Errore: Articolo già presente")
    user_answer = input("Vuoi rimuoverlo? In caso affermativo scrivi si: ")
    if user_answer == "si":
        items.remove(user_item)
        print("Articolo rimosso")
    else:
        print("Articolo non rimosso")
else:
    items.append(user_item)
    print("Articolo aggiunto ✅")
    items.sort()


for item in items:
    print("-", item)
