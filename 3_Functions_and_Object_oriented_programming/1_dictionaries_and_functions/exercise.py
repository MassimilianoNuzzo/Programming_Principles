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
items = {
    'fagioli':3,
    'noci':2,
    'mele':15
}

for key, value in items.items():
    print(f"- {key} ({value} pezzi)")

user_item = input("Aggiungi un articolo: ").lower().strip()
if not user_item:
    print("Errore: Non hai inserito alcun articolo")
elif user_item in items:
    print("Articolo già presente")
    qta_item = input('Aggiungi quantità: ')
    if not qta_item:
        print("Errore: Non hai inserito la quantità per l'articolo")
    else:
        print(items[user_item])
        items[user_item] = qta_item
        print("Articolo aggiunto ✅")
else:
    qta_item = input('Aggiungi quantità: ')
    if not qta_item:
        print("Errore: Non hai inserito la quantità per l'articolo")
    else:
        items[user_item] = qta_item
        print("Articolo aggiunto ✅")
    
for key, value in items.items():
    print("-", key,value)

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

person_1 = {
    'name':'Mario',
    'age':None
}

person_2 = {
    'name':'Gianni',
    'age':None
}

def calculate_age(name, current_year):
    birth_year = int(input(f'{name} inserisci l\'anno di nascita: '))
    age = current_year - birth_year
    return age

person_1['age'] = calculate_age(person_1['name'], 2024)
person_2['age'] = calculate_age(person_2['name'], 2024)

print(person_1['age'])
print(person_2['age'])
