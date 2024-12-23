'''
Definisci una lista che contenga 3 mete turistiche.
Stampale tutte a schermo e chiedi all'utente
dove desidera andare.
Per scegliere, dovrà immettere
l'indice dell'elemento della lista,
in questo caso un numero da 0 a 2.
Stampa a schermo un augurio di buon viaggio,
contenente la destinazione scelta.

Lancia il programma e tenta di farlo andare in errore,
così da trovare le eccezioni che potrebbero
verificarsi nel processo.
INDIZIO: Dovresti trovare due principali eccezioni.
Con un blocco try costituito da due rami except,
gestisci le due eccezioni.
'''

'''
travel_spots = ['Bali', 'Bangkok', 'Rome']

for i,spot in enumerate(travel_spots):
    print(i, '-', spot)

try:
    
    user_choice = int(input('Quale metà desideri visitare? '))
    destination = travel_spots[user_choice]

except IndexError:
    print(f'Errore: Destinazione inesistente! Inserisci un numero compreso tra 0 e {len(travel_spots)-1}!')
except ValueError:
    print('Errore: Inserisci un numero intero!')
except Exception as e:
    print(f'Errore: {e}', type(e))
else:
    print(f'La tua destinazione è: {destination}. Buon viaggio!')
finally:
    print('Connessione terminata...')
'''

'''
Aggiungi all'esercizio precedente,
un ulteriore funzionalità di gestione errori.
Se l'utente inserisce un numero negativo, 
il programma deve andare in errore!
Perciò in questo caso, solleva (con il comando raise),
un eccezione ValueError o IndexError, quella che ti sembra più appropriata.
Senza fare nessun altra modifica, prova a lanciare il programma e
inserire un numero negativo, il blocco try-expect dovrebbe gestirlo come atteso.
BONUS: se all'interno del ramo try 
avevi inserito comandi non critici,
spostali su un altro ramo affinche
vengano eseguiti solo se non si presenta
alcun errore nel ramo try
'''

'''
travel_spots = ['Bali', 'Bangkok', 'Rome']

for i,spot in enumerate(travel_spots):
    print(i, '-', spot)

try:
    
    user_choice = int(input('Quale metà desideri visitare? '))

    if user_choice < 0:
        raise IndexError

    destination = travel_spots[user_choice]

except IndexError:
    print(f'Errore: Destinazione inesistente! Inserisci un numero compreso tra 0 e {len(travel_spots)-1}!')
except ValueError:
    print('Errore: Inserisci un numero intero!')
except Exception as e:
    print(f'Errore: {e}', type(e))
else:
    print(f'La tua destinazione è: {destination}. Buon viaggio!')
finally:
    print('Connessione terminata...')
'''

'''
Nell'esercizio precedente,
se il numero inserito è negativo,
solleva un'eccezione più appropriata.
Crea un eccezione utente, con un nome appropriato,
tramite una classe che eredita da Exception
e assegnale un messaggio d'errore personalizzato.
Ora sollevala col comando raise,
al posto di quella precedente.
Infine, gestisci questa nuova eccezione,
con un nuovo ramo except.
'''

class NegativeNumberError(Exception):
    def __init__(self):
        super().__init__('Errore: Non puoi inserire un numero negativo!')

travel_spots = ['Bali', 'Bangkok', 'Rome']

for i,spot in enumerate(travel_spots):
    print(i, '-', spot)

try:
    
    user_choice = int(input('Quale metà desideri visitare? '))
    
    if user_choice < 0:
        raise NegativeNumberError

    destination = travel_spots[user_choice]

except NegativeNumberError as e:
    print(e)
except IndexError:
    print(f'Errore: Destinazione inesistente! Inserisci un numero compreso tra 0 e {len(travel_spots)-1}!')
except ValueError:
    print('Errore: Inserisci un numero intero!')
except Exception as e:
    print(f'Errore: {e}', type(e))
else:
    print(f'La tua destinazione è: {destination}. Buon viaggio!')
finally:
    print('Connessione terminata...')