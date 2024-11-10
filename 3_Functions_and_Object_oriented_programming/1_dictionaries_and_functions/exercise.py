'''
Modifica l'esercizio della lezione precedente,
(vedi codice di partenza in chat)
ma basandolo su un dizionario, invece che su una lista.
Il dizionario iniziale deve contenere
come chiave il prodotto da acquistare
e come valore la sua quantità.
All'utente sarà richiesto di inserire
sia il prodotto che la quantità.
Non è necessario ordinare il dizionario.
BONUS:
Se l'articolo è già presente,
chiedi di inserire la quantità
e aggiornala sul dizionario.
'''

'''
# crea il dizionario contenente la lista della spesa
# key = prodotto da acquistare
# value = quantità
items = {
    'formaggio':3,
    'pasta':2,
    'mozzarella':1,
    'ananas':5
}

# stampa le coppie chiave-valore contenute nel dizionario 
# con un - che precede ogni coppia
for item,quantity in items.items():
    print(f'- {item} - quantità: {quantity}')

# chiedi all'utente di aggiungere un nuovo elemento
# utilizzando il metodo lower per renderlo minuscolo
# e il metodo strip per rimuovere spazi non necessari
user_item = input('Aggiungi un articolo: ').lower().strip()

# se l'utente non inserisce nulla stampa messaggio di errore
if not user_item:
    print('Errore! Non hai inserito nessun elemento.')
# altrimenti verifica se il prodotto è già presente
elif user_item in items:
    # se l'articolo è già presente chiedi la nuova quantità e aggiornala
    print('Articolo già presente')
    user_quantity = int(input('Inserisci la quantità desiderata: ').strip())
    items[user_item] = user_quantity
    print('Articolo aggiornato')
else:
    # altrimenti l'articolo non è presente 
    # quindi aggiungilo al dizionario
    user_quantity = int(input('Inserisci la quantità desiderata: ').strip())
    items[user_item] = user_quantity
    print('Articolo aggiunto')

# stampa tutti gli elementi della lista
for key,value in items.items():
    print(f'- {key} - quantità: {value}')
'''

'''
Definisci due dizionari che rappresentano una persona,
avente il campo nome, ed altri dati a piacere.
Entrambi i dizionari possiedono il campo età
ma non è valorizzato.
Definisci una funzione che prende in input dall'utente
l'anno di nascita,
calcola l'età e la restituisce.
Nel messaggio di input va stampato il nome della persona,
bisogna perciò passarlo alla funzione come argomento.
Per calcolare l'età servirà l'anno attuale,
che deve esser passato anch'esso alla funzione.
Infine, chiama due volte la funzione,
per valorizzare il campo età sui due dizionari.
'''

user_1 = {
    'first_name':'Mario',
    'last_name':'Rossi',
    'email':'mario.rossi@gmail.com',
    'age':None
}

user_2 = {
    'first_name':'Giuseppe',
    'last_name':'Verdi',
    'email':'giuseppe.verdi@gmail.com',
    'age':None
}

def calculate_age(name, current_year):
    birth_year = int(input(f'Ciao {name} inserisci il tuo anno di nascita: '))
    if birth_year:
        age = current_year - birth_year
        return age

users = [user_1, user_2]

for user in users:
    user['age'] = calculate_age(user['first_name'],2024)
    print(f'L\'utente {user['first_name']} ha {user['age']} anni.')