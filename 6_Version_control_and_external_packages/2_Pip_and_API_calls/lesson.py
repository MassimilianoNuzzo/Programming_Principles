# Pip for external packages

# la funzione print() è una funzione che
# fa parte del pacchetto standard di Python
# ed è accessibile senza dover effettuare nessun import

# print()

# abbiamo visto che esistono funzioni
# che dobbiamo importare prima di poter utilizzare
# come ad esempio nel caso delle funzioni dump() e load()

# nel pacchetto standard sono state incluse
# le funzioni considerate più utilizzate
# evitando di appesantire Python
# con funzioni che vengono utilizzate in casi specifici
# ma con la possibilità di essere importate quando necessario

# in questo modo stiamo importando tutto il modulo json
# i vantaggi di questa sintassi sono:
# - avere tutto il modulo a disposizione,
#   specialmente in casi in cui non sappiamo con precisione quale funzione andremo ad utilizzare
# - potrebbe capitare di trovare due funzioni con lo stesso nome provenienti da moduli differenti,
#   con questa sintassi (andando ad indicare il prefisso del modulo di provenienza) stiamo indicando
#   in maniera esplicita quale funzione (da quale modulo) stiamo richiamando
'''
import json
import yaml

json.dump()
json.load()

yaml.dump()
yaml.load()
'''

# ma è possibile anche importare solo le funzioni
# di cui abbiamo strettamente bisogno

# il vantaggio di questa sintassi
# è che ogni volta dobbiamo utilizzare
# le funzioni appartenenti ad un modulo specifico
# non dobbiamo indicarne il prefisso

# questa sintassi ha più senso di essere utilizzata
# in progetti piccoli con pochi import
'''
from json import dump, load

dump()
load()
'''

# sconsigliato ed è anche evidenziato nelle linee guida PEP8
# l'utilizzo di questa sintassi

# from json import *

# Il modulo math

# uno dei moduli più importanti e molto utilizzato in programmi
# che richiedono calcoli matematici

# contiene molte variabili come ad esempio pi greco

'''
import math

print(math.pi)

# inoltre ha molte funzioni tra cui

# coseno
print(math.cos(math.pi))

# seno
print(math.sin(math.pi))

# radice quadrata
print(math.sqrt(16))
'''

# il modulo random
'''
# permette di generare numeri casuali

import random

# la funzione random() genera
# un numero float causale da 0 a 1
print(random.random())

# la funzione randint()
# permette di generare un numero intero
# casuale compreso tra gli int passati come argomento
print(random.randint(1,5))

# la funzione choice() accetta una lista di valori
# e casualmente restituisce un valore contenuto nella lista
print(random.choice([1,2,3,4,5,6,7]))
'''

# il modulo os - operative system

# fornisce funzionalità per interagire con il sistema operativo

'''
import os

# la variabile name contiene il nome del nostro sistema operativo
print(os.name)

# la funzione listdir() restituisce una lista 
# contenente i nomi dei file e directory presenti percorso su cui viene eseguita
print(os.listdir())

# la funzione getcwd() restituisce 
# il percorso in cui l'interprete viene eseguito
print(os.getcwd())

# la funzione mkdir() crea una directory 
# accetta come argomento il nome che vogliamo dare alla cartella
os.mkdir('test')

# la funzione rmdir() rimuove una directory
# accetta come argomento il nome della cartella da rimuovere
os.rmdir('test')
'''

# Pip e virtual environment

'''
# pip (su mac pip3)
# è lo strumento principale che ci permette di scaricare e installare
# moduli e package (package sono insieme di moduli)

# pip - acronimo di Pip Installs Package

# è possibile consultare il repository pypi - https://pypi.org/
# per cercare tutti i package disponibili

# si utilizza dal terminale

# installare nuovo package

# la sintassi per installare un package è

# pip3 install nome_package

# con questa sintassi viene installata 
# l'ultima versione disponibile del package

# è possibile indicare anche la versione desiderata

# pip3 install nome_package==2.3

# su windows su utilizza solo pip
# mentre su mac pip3

# package requests
# il package request permette di gestire richieste HTTP

# pip3 install requests

# disinstallare un package

# è possibile disinstallare un package attraverso il comando uninstall

# pip3 uninstall requests

# ottenere informazioni su un package installato
# come ad esempio versione

# pip show requests

# aggiornare versione di un package

# pip3 install --upgrade requests

# visualizzare la lista completa dei package installati

# pip3 list

# anche il comando freeze permette di visualizzare la lista 
# completa dei packages installati e relative versioni
# ma li mostra in un formato adatto per creare il file requirements.txt 
# necessario per esportare dipendenze e replicare ambiente di sviluppo in altri sistemi

#pip3 freeze

# Virtual Environment - ambienti virutali Python
# tramite pip è possibile installare packages globalmente nella nostra macchina
# ma non è la soluzione migliore, infatti per evitare di creare conflitti tra 
# progetti diversi che potrebbero avere gli stessi package ma con diverse versioni
# è possibile creare degli ambienti virtuali Python.

# Si crea un ambiente virtuale Python per progetto, in modo che ogni progetto
# sia indipendente, inoltre ciò permette la condivisione e la replica di un 
# determinato ambiente in sistemi differenti

# per creare un ambiente virtuale Python si esegue il seguente comando da terminale:

# python3 -m venv <env_name>

# una volta eseguito il comando verrà creata un nuovo folder
# con il nome assegnato all'ambiente virtuale
# questa cartella contiene tutti i file necessari costitutivi
# del nostro ambiente virtuale

# dobbiamo attivarlo per poterlo eseguire
# quindi sempre da terminale ci spostiamo all'interno
# della cartella 

# comando per mac
# source ./api-calls-env/bin/activate

# su windows non dobbiamo utilizzare source 
# e inoltre il percorso risulterà diverso
# ./api-calls-env/Scripts/activate

# una volta attivate l'ambiente virtuale
# è possibile installare i packages necessari
# per questo determinato progetto

# per replicare un ambiente virtuale in altri sistemi
# e ad esempio per lavorare in team 
# possiamo esportare i packages installati e relativa versione
# tramite il comando
# pip3 freeze > requirements.txt

# in un nuovo ambiente virtuale è possibile installare
# tutti i packages contenuti in un determinato file requirements.txt
# tramite il comando
# pip3 install -r ./requirements.txt
 
# per rimuovere un ambiente virtuale 
# si utilizza il comando
# rm -r <env_name>
'''

# il package requests e richieste HTTP tramite API - Application Program Interface

# un API è un protocollo che stabilisce un insieme di regole
# permette a client e server di comunicare tramite richieste HTTP

# un API espone diversi end-point alla quale è possibile effettuare
# delle richieste HTTP per ottenere delle informazioni ad esempio tramite richieste HTTP di tipo GET
# il server elabora le richieste ricevute dal client e se tutto ok fornisce le informazioni richieste
# altrimenti restituisce un messaggio di errore consono all'errore verificato

# il package requests permette di effettuare richieste HTTP


# le richieste HTTP possono gestire diversi metodi
# a seconda di ciò che vogliamo effettuare

# - GET : è utilizzato per ottenere informazioni dal server
# - POST : è utilizzato per inviare informazioni al server
# (ad esempio gestione login o per memorizzare dati in modo permamente su db)

# a seguito di una richiesta http di tipo GET otteniamo un oggetto
# come risposta dal server quindi salviamo l'oggetto in una variabile,
# buona pratica chiamarla response

# se la risposta è andata buon fine otteniamo un oggetto come risposta
# e come status code otteniamo 200 = OK
# altrimenti in caso di errore otteniamo uno status code che indica
# il problema riscontrato
# response = requests.get('https://api.openweathermap.org/data/2.5/weather')
# print(response)

# il server restituisce la risposta in formato JSON che il Python interpreta tramite
# il dizionario come data-type
# è possibile accedere alla risposta in formato str tramite il metodo text
# print(response.text)

# consultando la documentazione ufficiale vediamo
# che oltre a dover passare il parametro appid (API KEY)
# dobbiamo passare il parametro q in cui indichiamo il nome
# della città di cui vogliamo ottenere le informazioni meteo

#import requests

#response = requests.get(
#    'https://api.openweathermap.org/data/2.5/weather',
#    params={
        #'appid': 'a20826c61fc45f9c046856bf342d2c5b',
#        'q': 'Moncalieri',
#        'units':'metric'
#    }
#)
# print(response.text)

# l'attributo content dell'oggetto Response
# restituisce un numero binario
# ed è utile in quei casi in cui riceviamo
# file multimediali come img, video, audio..

# la risposta che otteniamo dal server in caso
# di richiesta OK è in formato JSON

# per ottenere un dizionario partendo dall'oggetto JSON
# ricevuto come risposta dobbiamo utilizzare
# il metodo json()

# print(response.json())
# print(type(response.json()))

# dalla documentazione vediamo l'esempio di risposta
# ricevuto in caso di richiesta effettuata correttamente


# weather_data = response.json()

'''
{
   "coord": {
      "lon": 7.367,
      "lat": 45.133
   },
   "weather": [
      {
         "id": 501,
         "main": "Rain",
         "description": "moderate rain",
         "icon": "10d"
      }
   ],
   "base": "stations",
   "main": {
      "temp": 284.2,
      "feels_like": 282.93,
      "temp_min": 283.06,
      "temp_max": 286.82,
      "pressure": 1021,
      "humidity": 60,
      "sea_level": 1021,
      "grnd_level": 910
   },
   "visibility": 10000,
   "wind": {
      "speed": 4.09,
      "deg": 121,
      "gust": 3.47
   },
   "rain": {
      "1h": 2.73
   },
   "clouds": {
      "all": 83
   },
   "dt": 1726660758,
   "sys": {
      "type": 1,
      "id": 6736,
      "country": "IT",
      "sunrise": 1726636384,
      "sunset": 1726680975
   },
   "timezone": 7200,
   "id": 3165523,
   "name": "Province of Turin",
   "cod": 200
}     
'''

# notiamo che le informazioni riguardo al meteo che
# ci interessano si trovano all'interno della proprietà
# main 

#print(weather_data['main']['feels_like'])

# l'attributo status_code dell'oggetto response
# restituisce lo status code ricevuto come risposta
# ed è possibile eseguire controlli su di esso
# tramite ad esmepio istruzioni condizionali if
# per eseguire determinate istruzioni rispetto ad altre
# banalmente anche solo per verificare che la risposta
# ricevuta sia 200 prima di tentare di accedere ai dati
# evitando di generare eccezioni ad esempio

#print(response.status_code == 200)

# il metodo raise_for_status() dell'oggetto response
# solleva un eccezione se la richiesta non è andata buon fine

# quindi è possibile gestire eventuali errori 
# con il costrutto try-except

import requests

response = requests.get(
    'https://api.openweathermap.org/data/2.5/weather',
    params={
        #'appid': 'a20826c61fc45f9c046856bf342d2c5b',
        'q': 'New York',
        'units':'metric'
    }
)

try:
    
    response.raise_for_status()

except requests.exceptions.HTTPError:
    
    print('Errore nella richiesta Http.') 