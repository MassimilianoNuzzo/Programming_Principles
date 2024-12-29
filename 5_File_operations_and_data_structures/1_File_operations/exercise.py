'''
Scrivi un programma che chiede all'utente
il nome di un social network che utilizza abitualmente
e la relativa password di accesso.
Il programma, a questo punto, apre un file
e scrive al suo interno una riga
contenente social e password,
magari separati da un = o un altro carattere a piacere.
Attenzione: ogni volta che il programma viene riavviato,
ed i nuovi social e password vengono inseriti,
la nuova riga che li conterrà dev'essere AGGIUNTA al file.
'''

'''
social_network = input('Inserisci il nome del social network: ')
password = input('Inserisci la password: ')

with open('password_manager.txt','a',encoding='utf-8') as file:
    file.write(f'{social_network}-{password}')

print('Social Network aggiunto!')
'''

'''
Modifica il programma precedente,
aggiungendo la funzionalità di lettura.
All'avvio, il programma chiede all'utente
se desidera aggiungere un nuovo social e password,
o se desidera leggere quelli già presenti.
Se desidera aggiungere, procedi come in precedenza.
Se desidera leggere, apri il file in lettura,
e stampa a schermo ognuna delle righe
contenenti social e password,
precedute da un trattino o un altro carattere a piacere.
'''

'''
FILENAME = 'password_manager.txt'

def write_file():
    social_network = input('Inserisci il nome del social: ')
    password = input(f'Inserisci la password: ')
    with open(FILENAME, 'a', encoding='utf-8') as file:
        file.write(f'{social_network}-{password}\n')
    
    print('Elemento aggiunto!')

def read_file():
    with open(FILENAME, 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())

print('Quale operazione intendi effettuare?\n')
print('1 - per aggiungere un nuovo social;\n')
print('2 - per leggere il file;\n')

user_input = int(input())

print()

if user_input == 1:

    write_file()

elif user_input == 2:

    read_file()

else:
    print('Carattere non consentito!')
'''

'''
Converti in un file json,
il file di testo generato,
negli esercizi precedenti
(non alterare l'originale).
Inizialmente crea un dizionario vuoto,
quindi apri il file di testo in lettura
accedi ciclicamente ad ognuna delle righe,
e dividila (metodo split)
per ottenere chiave (social) e valore (password).
Aggiungi al dizionario ciascuna coppia chiave-valore.
Infine, apri un nuovo file in scrittura,
e scrivi il dizionario su di esso,
serializzandolo col metodo json.dump.
'''

import json

def read_social_from_file():
    social_networks = {}

    with open('password_manager.txt', 'r', encoding='utf-8') as file:
        for line in file:
            social_network_from_file = line.strip().split('-')
            key = social_network_from_file[0]
            value = social_network_from_file[1]
            social_networks[key] = value
            
    return social_networks

social_networks = read_social_from_file()
with open('password_manager.json','a',encoding='utf-8') as json_file:
    json.dump(social_networks, json_file)


        