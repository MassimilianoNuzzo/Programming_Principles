# file I/O operations

# la funzione open() permette di leggere e scrivere file
# è una funzione built-in che accetta due argomenti:
# - percorso del file (assoluto o relativo)
# - modalità di accesso al file (lettura/scrittura)

'''
item_to_buy = input()
# restituisce un oggetto stream rappresentante il file stesso
# può essere istanza della classe TextIOWrapper (se file di testo)
# o istanza della classe BufferedReader (se file binario come immagini, video, audio)
file = open('lista_della_spesa.txt','w')
file.write(item_to_buy)
'''

# una volta effettuate le nostre operazioni sul file
# dobbiamo chiuderlo con il metodo close()
# in questo modo liberiamo la risorsa occupata,
# altrimenti sarebbe impegnata dal nostro processo
# e non accessibile da altri processi

'''
item_to_buy = input()
file = open('lista_della_spesa.txt','w')
file.write(item_to_buy)
# una volta effettuate le operazioni chiudiamo il file
file.close()
'''

# per permettere al file di elaborare caratteri speciali
# dobbiamo indicare nel metodo open() il set di caratteri
# tramite l'argomento encoding (utf-8)

'''
item_to_buy = input()
file = open('lista_della_spesa.txt','w', encoding='utf-8')
file.write(item_to_buy)
# una volta effettuate le operazioni chiudiamo il file
file.close()
'''

# la dichiarazione with
# è un modo più semplice e sicuro per elaborare files in python
# provvede in automatico a chiudere lo stream alla fine di tutte le operazioni

'''
item_to_buy = input()

# dichiarazione with
with open('lista_della_spesa.txt','w', encoding='utf-8') as file:
    file.write(item_to_buy)
'''

# modalità append - a

# la modalità append permette di scrivere nuovo contenuto
# senza che il contenuto precedente venga sovrascritto

'''
item_to_buy = input()

# modalità append - 'a'
with open('lista_della_spesa.txt','a', encoding='utf-8') as file:
    # aggiungiamo carattere nuova linea
    # in modo che il nuovo contenuto venga scritto a capo
    file.write(f'{item_to_buy}\n')
'''

# metodi oggetto stream in modalità reading write'w' 

# writelines()
'''
# accetta una lista di elementi che scrive al fondo del nostro file
with open('lista_della_spesa.txt','a', encoding='utf-8') as file:
    # dobbiamo indicare il carattere \n (new-line) alla fine di ogni elemento
    # in quanto senza, tutta la lista verrebbe scritta sulla stessa linea
    file.writelines(['coca-cola\n','acqua\n'])
'''

# modalità reading - 'r'

# leggere informazioni contenute in un file
# può generare l'eccezzione FileNotFoundError

# il context manager della dichiarazione with non crea uno scope
# è quindi possibile creare una variabile all'interno della dichiarazione with
# per poi utilizzarla al di fuori del blocco stesso
'''
with open('lista_della_spesa.txt','r', encoding='utf-8') as file:
    # dichiarazione variabile all'interno del context manager
    content = file.read()
# utilizzo della variabile al di fuori del context manager
print(content)
'''

# metodi oggetto stream in modalità reading read'r'

# read()
# il metodo read() legge l'intero contenuto del nostro file
# è possibile indicare un argomento opzionale, ovvero un numero intero
# che indica il numero massimo di caratteri che vogliamo leggere
'''
with open('lista_della_spesa.txt','r', encoding='utf-8') as file:
    content = file.read(10)
print(content)
'''

# readline()
# il metodo readline() permette di leggere il file linea per linea
'''
with open('lista_della_spesa.txt','r', encoding='utf-8') as file:
    file.readline()
    file.readline()
    file.readline()
    file.readline()
    file.readline()
    file.readline()
'''    

# readlines()
# il metodo readlines() permette di leggere tutte le linee contenute in un file
# restituisce una lista contenente tutte le linee appena lette
# siccome viene restituita una lista, è possibile iterare ed effettuare operazioni
# su ogni singolo elemento della lista
'''
with open('lista_della_spesa.txt','r', encoding='utf-8') as file:
    for line in file.readlines():
        print('-',line.strip())

'''

# nelle versioni più recenti di Python
# è possibile iterare direttamente l'oggetto file (stream)
# senza utilizzare il metodo readlines()
'''
with open('lista_della_spesa.txt','r', encoding='utf-8') as file:
    for line in file:
        print('-',line.strip())
'''

# accedere ed eseguire operazioni su file binari

# per file binari intendiamo immagini, video o audio
# per accedervi ed eseguire operazioni utilizziamo
# sempre la dichiarazione with che restituisce un oggetto stream
# in questo caso istanza della classe BufferedReader

# per leggere un file binario bisogna indicare la modalità 'rb'
# omettendo l'argomento encoding
'''
with open('python.png','rb') as file:
    print(file)
'''

# metodi disponibili in modalita 'rb'

# readlines()
# questo metodo permette di leggere i bytes contenuti nel file binario

'''
with open('python.png','rb') as file:
    image_data_lines = file.readlines()

print(type(image_data_lines))

#restituisce infatti un oggetto di tipo bytes
print(type(image_data_lines[0]))
'''

# scrittura file binario modalità - 'wb'

'''
# leggiamo dal file python.png
with open('python.png','rb') as file:
    image_data_lines = file.readlines()

# creiamo un nuovo file contenente i byte letti dal file python.png
# utilizzando la modalità wb per scrivere byte
with open('python_2.png','wb') as file:
    for line in image_data_lines:
        file.write(line)
'''

# possiamo anche scegliere di scrivere solo una porzione
# dei byte letti dal file originale

'''
# leggiamo dal file python.png
with open('python.png','rb') as file:
    image_data_lines = file.readlines()

# verifichiamo l'esatta dimensione della lista
print(len(image_data_lines))

with open('python_2.png','wb') as file:
    # iteriamo sulla lista fino all'elemento 6
    for line in image_data_lines[0:6]:
        file.write(line)
'''

# accesso sequenziale e random access
# accesso sequenziale
# permette di elaborare un file in modo sequenziale (dall'alto verso il basso)
# dall'inizio alla fine senza saltare parte del contenuto stesso

# esempio accesso sequenziale
'''
with open('lista_della_spesa.txt','r', encoding='utf-8') as file:
    for line in file:
        print('-',line.strip())
'''

# random access
# permette di processare una porzione specifica di un file
# senza dover leggere tutto il contenuto del file stesso

# per fare ciò si utilizza il metodo seek()
# in cui passiamo un intero che rappresenta l'inizio della porzione di contenuto 
# che ci interessa
'''
with open('lista_della_spesa.txt','r', encoding='utf-8') as file:
    file.seek(3)
    print(file.read(10))
'''

# Serializzazione e deserializzazione

# serializzazione 
# processo per convertire un oggetto o una struttura dati python
# in un formato lineare (ad esempio string) che può essere facilmente 
# memorizzato (ad esempio un file) e trasmesso attraverso la rete

# deserializzazione
# è il processo inverso, converte il formato lineare 
# in oggetti o strutture dati python per poter elaborare
# nuovmanente quei dati

# il formato più comune e utilizzato è il JSON (Javascript Object Notation)

# serializzazione

# per scrivere un file json in python
# dobbiamo effettuare la serializzazione
# dei dati che vogliamo scrivere/trasmettere
# utilizzando la funzione dump() del modulo json

'''
# import modulo json
import json

# possiamo serializzare qualsiasi struttura dati
# ma solitamente quella più utilizzata è il dizionario
# in quanto permette facile accesso per via della sua struttura
# chiave - valore
shopping_list = {
    'pere':1, 
    'arance':2, 
    'mele':5
}

# utilizziamo sempre la dichiarazione with
# impostando come formato del file che vogliamo scrivere .json
with open('lista_della_spesa.json','a', encoding='utf-8') as file:
    # la funzione dump ci permette di effettuare la serializzazione
    # per poterla utilizzare dobbiamo importare il modulo json
    # questa funzione accetta due argomenti:
    # - il dato che vogliamo serializzare
    # - il file su cui vogliamo scrivere
    json.dump(shopping_list,file)
'''

# deserializzazione

# per poter leggere i dati da un json
# e convertire in strutture dati python
# dobbiamo utilizzare la funzione load()
# contenuta sempre nel modulo json

import json

# utilizziamo sempre la dichiarazione with
with open('lista_della_spesa.json','r', encoding='utf-8') as json_file:
    data_from_json = json.load(json_file)

print(data_from_json) 