# Paradigmi di programmazione

# Paradigma di programmazione procedurale 
'''
def get_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            print(f'Found even number: {num}')
            even_numbers.append(num)
    
    numbers.clear()
    numbers.extend(even_numbers)
    print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
get_even_numbers(numbers)
'''

# Paradigma di programmazione ad oggetti
'''
class NumberProcessor:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def get_even_numbers(self):
        even_numbers = []
        for num in self.numbers:
            if num % 2 == 0:
                even_numbers.append(num)
        self.numbers = even_numbers

processor = NumberProcessor([1, 2, 3, 4, 5, 6, 7, 8, 9])
processor.get_even_numbers()
print(processor.numbers)
'''

# Paradigma di programmazione funzionale

'''
def get_even_numbers(numbers):
    return[num for num in numbers if num % 2 == 0]

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(get_even_numbers(numbers))
'''

# Exceptions - gestione degli errori

# fino a questo momento non abbiamo gestito gli errori
# analizzando questo codice se l'utente 
# inserisce un numero intero come input l'esecuzione termina senza alcun errore
# ma nel caso in cui l'utente inserisce ad esempio caratteri alfabetici
# il programma non è in grado di convertire in intero l'input dell'utente

'''
birth_year = int(input('In che anno sei nato? '))
age = 2024 - birth_year
print(age)
'''

# gestire le eccezioni - costrutto try-expect
'''
try:
    birth_year = int(input('In che anno sei nato? '))
    age = 2024 - birth_year
    print(age)
except:
    print('Per favore, inserisci un numero intero!')
'''

# esistono diversi tipi di eccezioni causate da errori di tipo diverso

'''
car_price = 20_000

# potrebbe generare eccezione di tipo ValueError
months = int(input('In quanti mesi vuoi pagare la macchina? '))

# potrebbe generare eccezione di tipo ZeroDivisionError
monthly_payment = car_price/months

print(monthly_payment)
'''

# il costrutto try-expect consente di gestire
# - più eccezioni
# - indicando anche eccezioni specifiche, ottenendo risposta in base all'eccezione generata

'''
car_price = 20_000

try:

    months = int(input('In quanti mesi vuoi pagare la macchina? '))
    monthly_payment = car_price/months
    print(monthly_payment)

except ValueError:
    print('Per favore, inserisci un numero intero!')
except ZeroDivisionError:
    print('Per favore, inserisci un numero maggiore di 0!')
'''

# è possibile gestire più eccezioni con un unico expect

# è considerata cattiva pratica, in quanto stiamo gestendo
# le varie eccezioni in modo generico

'''
car_price = 20_000

try:

    months = int(input('In quanti mesi vuoi pagare la macchina? '))
    monthly_payment = car_price/months
    print(monthly_payment)

except (ValueError, ZeroDivisionError):
    print('Per favore, inserisci un numero valido!')
'''

# ci sono situazioni in cui non è facile prevedere
# quali e quante eccezioni possano verificarsi

# è buona pratica inserire al fondo della lista di eccezioni specifiche
# un eccezione generica per gestire tutte quelle eccezioni che non abbiamo previsto

'''
car_price = 20_000

try:

    months = int(input('In quanti mesi vuoi pagare la macchina? '))
    monthly_payment = car_price/months
    print(monthly_payment)

except ValueError:
    print('Per favore, inserisci un numero intero!')
except ZeroDivisionError:
    print('Per favore, inserisci un numero maggiore di 0!')
except Exception:
    # questa eccezione "catturerà" tutte 
    # le eccezioni impreviste generate in fase di run-time (esecuzione)
    print('Errore generico!')
'''

# possiamo ottenere informazioni più specifiche 
# riguardo l'errore imprevisto catturato dall'eccezione generica
# accedendo all'oggetto stesso dell'eccezione

'''
# commentiamo car_price per forzare l'errore imprevisto
#car_price = 20_000

try:

    months = int(input('In quanti mesi vuoi pagare la macchina? '))
    monthly_payment = car_price/months
    print(monthly_payment)

except ValueError:
    print('Per favore, inserisci un numero intero!')
except ZeroDivisionError:
    print('Per favore, inserisci un numero maggiore di 0!')
except Exception as e:
    print(f'Errore, {e}', type(e))
'''

# dopo aver gestito tutte le eccezion nel costrutto try-expect si utilizza l'else: 
# viene eseguito soltanto se non è stata generata alcuna eccezione

# nel try inseriamo solo le istruzioni critiche
# che ipotiziamo possano generare eccezioni

'''
car_price = 20_000

try:
	# istruzioni critiche che possono generare eccezioni
    months = int(input('In quanti mesi vuoi pagare la macchina? '))
    monthly_payment = car_price/months
    
except ValueError:
    print('Per favore, inserisci un numero intero!')
except ZeroDivisionError:
    print('Per favore, inserisci un numero maggiore di 0!')
except Exception as e:
    print(f'Errore, {e}', type(e))

else:
	# viene eseguita soltanto se non viene generata alcuna eccezione
    print(monthly_payment)
'''

# per concludere il costrutto try-expect si utilizza il finally
# le istruzioni contenuto dentro il blocco finally
# vengono eseguite in ogni caso

# utilizzato per il rilascio di risorse e chiusura connessioni varie
# fondamentale, in quanto vogliamo chiudere le connessioni a prescindere 
# dell'esito del nostro programma, ci permette di aver maggiore controllo
# in qualsiasi caso

'''
car_price = 20_000

try:
	
    months = int(input('In quanti mesi vuoi pagare la macchina? '))
    monthly_payment = car_price/months
    
except ValueError:
    print('Per favore, inserisci un numero intero!')
except ZeroDivisionError:
    print('Per favore, inserisci un numero maggiore di 0!')
except Exception as e:
    print(f'Errore, {e}', type(e))

else:
    print(monthly_payment)

finally:
    print('Connessione al database chiusa con successo.')
'''

# assert statement

# l'istruzione assert è una keyword utilizzata
# in fase di debugging/test
# letteralmente significa assicurati che questa condizione sia rispettata

# l'istruzione assert non restituisce un errore specifico
# viene gestita dalla classe Exception restituendo un errore generico
# inoltre è utilizzata per test/debug

# NON PUò ESSERE RILASCIATA IN AMBIENTE DI PRODUZIONE

'''
car_price = 20_000

try:
	
    months = int(input('In quanti mesi vuoi pagare la macchina? '))

    assert months > 0

    monthly_payment = car_price/months
    
except ValueError:
    print('Per favore, inserisci un numero intero!')
except ZeroDivisionError:
    print('Per favore, inserisci un numero maggiore di 0!')
except Exception as e:
    print(f'Errore, {e}', type(e))

else:
    print(monthly_payment)

finally:
    print('Connessione al database chiusa con successo.')
'''

# raise statement

# a differenza dell'istruzione assert
# l'istruzuine raise solleva un eccezione

# tramite il costrutto if indichiamo la condizione
# in cui vogliamo che venga generata l'eccezione
# e all'interno del blocco if, utilizziamo l'istruzione raise
# istanziando un oggetto della classe eccezione che vogliamo generare
# passando come argomento al costruttore un messaggio di errore

'''
car_price = 20_000

try:
	
    months = int(input('In quanti mesi vuoi pagare la macchina? '))

    if months < 0:
        # in questo caso stiamo utilizzando la classe generica Exception
        # ma vedremo che è possibile creare classi eccezioni personalizzate
        raise Exception('Il numero di mesi non può essere negativo.')

    monthly_payment = car_price/months
    
except ValueError:
    print('Per favore, inserisci un numero intero!')
except ZeroDivisionError:
    print('Per favore, inserisci un numero maggiore di 0!')
except Exception as e:
    print(f'Errore, {e}', type(e))

else:
    print(monthly_payment)

finally:
    print('Connessione al database chiusa con successo.')
'''

# eccezioni utente - eccezioni personalizzate

# definizione eccezione utente

'''
class NegativeMonthsError(Exception):

    def __init__(self):
        super().__init__('Il numero di mesi non può essere negativo.')

car_price = 20_000

try:
	
    months = int(input('In quanti mesi vuoi pagare la macchina? '))

    if months < 0:
        # utilizzo eccezione utente
        raise NegativeMonthsError

    monthly_payment = car_price/months

except ValueError:
    print('Per favore, inserisci un numero intero!')
except ZeroDivisionError:
    print('Per favore, inserisci un numero maggiore di 0!')
except Exception as e:
    print(f'Errore, {e}', type(e))

else:
    print(monthly_payment)

finally:
    print('Connessione al database chiusa con successo.')
'''

# è anche possibile gestirla con un ramo expect personalizzato

class NegativeMonthsError(Exception):

    def __init__(self):
        super().__init__('Il numero di mesi non può essere negativo.')

car_price = 20_000

try:
	
    months = int(input('In quanti mesi vuoi pagare la macchina? '))

    if months < 0:
        # utilizzo eccezione utente
        raise NegativeMonthsError

    monthly_payment = car_price/months

except NegativeMonthsError as e:
    print(e)
except ValueError:
    print('Per favore, inserisci un numero intero!')
except ZeroDivisionError:
    print('Per favore, inserisci un numero maggiore di 0!')
except Exception as e:
    print(f'Errore, {e}', type(e))

else:
    print(monthly_payment)

finally:
    print('Connessione al database chiusa con successo.')