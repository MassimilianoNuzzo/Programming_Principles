'''
Crea una lista della spesa che contenga
alcuni articoli a piacere.
Ordina gli articoli alfabeticamente
e poi stampali tutti a schermo,
ognuno di essi preceduto da un trattino.
Ora chiedi all'utente un nuovo articolo
da aggiungere.
Se l'utente non inserisce nulla,
stampa un messaggio di errore,
Se l'utente inserisce un articolo già presente,
stampa un messaggio di errore.
Se l'utente inserisce correttamente
un nuovo articolo,
aggiungilo alla lista.
In ogni caso, al termine del programma,
stampa nuovamente tutti gli articoli
(sempre ordinati alfabeticamente).
BONUS: attenzione al case!
'''

'''
# crea la lista della spesa
items = ['formaggio','pasta','mozzarella','ananas']
# ordina la lista
items.sort()

# stampa la lista con un - che precede ogni elemento
for item in items:
    print('-', item)

# chiedi all'utente di aggiungere un nuovo elemento
# utilizzando il metodo lower per renderlo minuscolo
# e il metodo strip per rimuovere spazi non necessari
user_item = input('Aggiungi un articolo: ').lower().strip()

# se l'utente non inserisce nulla stampa messaggio di errore
if not user_item:
    print('Errore! Non hai inserito nessun elemento.')
# altrimenti verifica se il prodotto è già presente
elif user_item in items:
    # se è gia presente stampa messaggio di errore
    print('Errore! Articolo già presente')
else:
    # altrimenti l'articolo non è presente 
    # quindi aggiungilo alla lista
    items.append(user_item)
    # ordina la lista dopo aver aggiunto il nuovo articolo
    items.sort()

# stampa tutti gli elementi della lista
for item in items:
    print('-', item)
'''

'''
Modifica l'esercizio precedente
in caso l'utente inserisce un prodotto 
già presente chiedere se vuole rimuoverlo.
In caso affermativo procedi alla rimozione
'''

'''
# crea la lista della spesa
items = ['formaggio','pasta','mozzarella','ananas']

# ordina la lista
items.sort()

# stampa la lista con un - che precede ogni elemento
for item in items:
    print('-', item)

# chiedi all'utente di aggiungere un nuovo elemento
# utilizzando il metodo lower per renderlo minuscolo
# e il metodo strip per rimuovere spazi non necessari
user_item = input('Aggiungi un articolo: ').lower().strip()

# se l'utente non inserisce nulla stampa messaggio di errore
if not user_item:
    print('Errore! Non hai inserito nessun elemento.')
# altrimenti verifica se il prodotto è già presente
elif user_item in items:
    # se è gia presente stampa messaggio di errore
    print('Errore! Articolo già presente')
    # chiedere all'utente se vuole rimuoverlo
    user_answer =input('Vuoi rimuoverlo? In caso affermativo scrivi si: ').lower().strip()
    # controlla se la risposta è == 'si'
    if user_answer == 'si':
        # rimuovo articolo dalla lista
        items.remove(user_item)
        print(f'Articolo {user_item} rimosso.')
    else:
        print(f'Articolo {user_item} non rimosso.')
else:
    # altrimenti l'articolo non è presente 
    # quindi aggiungilo alla lista
    items.append(user_item)
    # ordina la lista dopo aver aggiunto il nuovo articolo
    items.sort()

# stampa tutti gli elementi della lista
for item in items:
    print('-', item)

'''

'''
Modifica il programma precedente:
l'utente deve poter inserire più articoli alla volta,
separandoli col carattere |
In tal caso, il programma converte
tale stringa inserita dall'utente in una lista di articoli,
i quali vengono poi aggiunti alla lista iniziale.
Per semplicità, non controllare se l'utente
inserisce articoli già presenti o stringhe vuote.
'''

# crea la lista della spesa
items = ['formaggio','pasta','mozzarella','ananas']

# salviamo in una variabile il carattere utilizzato per lo split
split_char = '|'

# ordina la lista
items.sort()

# stampa la lista con un - che precede ogni elemento
for item in items:
    print('-', item)

# chiedi all'utente di aggiungere un nuovo elemento
# utilizzando il metodo lower per renderlo minuscolo
# e il metodo strip per rimuovere spazi non necessari
user_item = input('Aggiungi un articolo: ').lower().strip()

# se il carattere di split è presente nell'input dell'utente
# estendiamo la lista item con la nuova lista
if split_char in user_item:
    to_add_items = user_item.split(split_char)
    items.extend(to_add_items)
    print('Articoli aggiunti')
    # ordina la lista dopo aver aggiunti i nuovi articoli
    items.sort()
# se l'utente non inserisce nulla stampa messaggio di errore
elif not user_item:
    print('Errore! Non hai inserito nessun elemento.')
# altrimenti verifica se il prodotto è già presente
elif user_item in items:
    # se è gia presente stampa messaggio di errore
    print('Errore! Articolo già presente')
    # chiedere all'utente se vuole rimuoverlo
    user_answer =input('Vuoi rimuoverlo? In caso affermativo scrivi si: ').lower().strip()
    # controlla se la risposta è == 'si'
    if user_answer == 'si':
        # rimuovo articolo dalla lista
        items.remove(user_item)
        print(f'Articolo {user_item} rimosso.')
else:
    # altrimenti l'articolo non è presente 
    # quindi aggiungilo alla lista
    items.append(user_item)
    # ordina la lista dopo aver aggiunto il nuovo articolo
    items.sort()

# stampa tutti gli elementi della lista
for item in items:
    print('-', item)
