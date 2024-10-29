# i nomi delle variabili devono 
# rispettare delle convenzioni
# può contenere soltanto:
# - lettere minuscole
# - lettere maiuscole
# - numeri a patto che non sia il primo carattere (es sbagliato: 1nome_utente)
# - trattino basso _ per separare eventuali parole che costituiscono nome variabile
# si utilizza la convenzione snake_case: solo lettere minuscole e se nome variabile composto da 
# più parole si utilizza il trattino basso _ come separatore
# accenno alla convenzione cammelCase non utilizzata in python ma ad esempio in Java
# in python comunque è possibile utilizzare anche le altre convenzioni di naming
# ma non è buona norma, si usa la convenzione snake_case
# per convenzione anche i file in python vengono nominati con la convenzione snake_case
nome_utente = 'Massimiliano'
# inoltre le variabili sono case sensitive distingue minuscole e maiuscole
#print(Nome_Utente) # causa errore - non esiste variabile Nome_Utente ma nome_utente

# le variabili sono definite appunto variabili 
# perchè durante l'esecuzione del programma
# il loro contenuto può variare

# è quindi possibile ri-assegnare 
# un valore ad una variabile già istanziata

print(nome_utente) # otterrò 'Massimiliano'

nome_utente = 'Mario'

print(nome_utente) # otterò 'Mario'

# anche se in python non esistono
# è possibile comunque definire costanti
# vengono denominate in maiuscolo - ed è più una convenzione 
# per indicare a noi in primis e chi legge il nostro codice
# che quello è un valore che non vogliamo venga mai modificato
# in quanto è possibile assegnare un nuovo valore
# ad una variabile definita come costante
PI_GRECO = 3.14
GRAVITY = 9.81
print(GRAVITY) # otterrò 9.81
GRAVITY = 19.81
print(GRAVITY) # otterrò 19.81 - il valore di GRAVITY è stato ri-assegnato

# Literals

# i literal sono parte della sintassi python
# ci consentono di dichiarare un valore
# con un relativo data-type (tipo di dato)

# Data-Type

# String
# per definire un variabile di tipo string 
# il literal prevede che venga definita tra apici singoli o doppi
nome = 'Mario'

# non è differente se definiamo string
# con apici singoli o doppi - manteniamo una coerenza però

# segna errore in quanto l'apostrofo viene rilevato dall'interprete
# come chiusura della stringa
# titolo_canzone = 'Canzone dell'amore perduto'
# per risolvere possiamo usare apici doppi
titolo_canzone = "Canzone dell'amore perduto"

# anche in questo caso otterrò errore
# quote = "Ho visto al cinema il film "INCEPTION" " 

# python essendo molto flessibile ci consente 
# di utilizzare entrambi per definire stringhe

# esiste anche un carattere speciale
# \ - escape character permette di assegnare 
# funzionalità speciali al carattere che segue

# in questo caso serve a far considerare l'apice singolo
# come carattere facente parte della stringa e non come chiusura
titolo_canzone = 'Canzone dell\'amore perduto'

# è possibile utilizzare l'escape character
# anche con i doppi apici
quote = "Ho visto al cinema il film \"INCEPTION\""
print(quote)

# possiamo definire una stringa multilinea
# tramite il literal a triplo apice
new_quote = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
'''
print(new_quote)

'''
il literal triplo apice
viene utilizzato (in modo inproprio)
anche per realizzare commenti multilinea
è comunque una stringa ma che non essendo dichiarata
non viene presa in considerazione dall'interprete
'''

# int
# per descrivere un numero intero (int) 
# intero perchè non ha parte frazionaria
# scriviamo semplicemente il numero
birth_year = 1994

# le variabili di tipo int
# possono contenere anche valori negativi
temperatura = -3

# per i numeri molto lunghi
# python mette a disposizione una formattazione speciale
# attraverso l'utilizzo del carattere _
print(15_000_000_000)

# ovviamente sono equivalenti
print(15000000000)

# con i numeri interi 
# possiamo esprimre cifre su base decimale 0-9 (10 cifre)
# ma anche su base binaria utilizzata nei linguaggi di basso livello

# per poter definire un numero binario
# devo inserire il prefisso 0b
print(0b010111)

# è possibile definire numeri interi
# anche in base ottale (0-7)
print(0o013546754)

# abbiamo anche la base esadecimale
# prevede numeri da 0 a 9 e 
# le lettere dalla a alla f
# solitamente usato per esprimere i colori
print(0xFFFFFF) # COLORE BIANCO
print(0x000000) # COLORE NERO

# float
# si usano per esprimere numeri con parte frazionaria 
# quando vogliamo rappresentare numeri non interi
# attenzione si usa il punto e non la virgola
print(9.99)

# anche con i float
# possiamo esprimere numeri negativi
print(-9.99)

# se vogliamo esprimere un float
# senza parte frazionaria possiamo
print(19.0) # indicare la parte frazionaria con 0
print(-19.) # indicare all'interprete che è float attraverso il .

# literal per la notazione scientifica
# utilizzata per rappresentare numeri molto grandi
print(15e9) # 15*10^9 = 15000000000 
# o molto piccoli
print(15e-9)

# boolean
# può contenere 2 tipi di valori
# True o False
print(False)
print(True)

# serve per verificare se una determinata
# condizione è vera o falsa
a = 20
b = 10
is_a_greater_than_b = a > b
print(is_a_greater_than_b)

# Funzione type()
# la funzione type() prende come argomento
# una variabile e ne restituisce il data-type

# per visualizzare l'output della funzione type()
# dobbiamo utilizzare la funzione print()
# ottenendo un annidamento di funzioni - nesting
# l'argomento contenuto nella funzione print()
# non è un semplice argomento ma risultato di un altra funzione
# prima di eseguire la funzione print() viene eseguita la funzione type()
# ottenendo cosi l'argomento della funzione print()
print(type(nome_utente))
print(type(birth_year))
print(type(PI_GRECO))
print(type(is_a_greater_than_b))

# è possibile inoltre cambiare il data-type
# di una variabile già dichiarate e istanziata
test_var = 'Andrea'
print(test_var)
test_var = 10
print(test_var)

# metodo
# i metodi differiscono dalle funzioni
# in quanto strettamente legate 
# all'oggetto su cui vengono chiamati

# metodi delle stringhe

# upper() - rende una stringa maiuscola UPPER CASE
# la stringa su cui applichiamo il metodo non viene modificata
# ma ne crea una nuova che assegno ad alla variabile upper_name
upper_name = nome_utente.upper()
print(upper_name)

# lower() - rende una stringa minuscola lower case
# la stringa su cui applichiamo il metodo non viene modificata
# ma ne crea una nuova che assegno ad alla variabile lower_name
lower_name = nome_utente.lower()
print(lower_name)

# strip() - utilizzato per pulire una stringa
# da spazi,\t(tab),\n(new line) eccessivi
# sia ad inzio che a fine stringa
# lasciando solo il contenuto
message = '\t Ciao come stai?    \n'
formatted_message = message.strip()
print(formatted_message)

# replace() - utilizzato per sostituire
# una parte della stringa originale
# con una nuova stringa
# accetta due argomenti
# la stringa da sostituire 
# la nuova stringa con cui sostituire la precedente
new_message = formatted_message.replace('stai','state')
print(new_message)

# islower() - restituisce un booleano
# verifica se la stringa a cui lo applichiamo
# è composta solo da caratteri minuscoli
print(new_message.islower())

# count() - restituisce un intero 
# rappresentante il numero di caratteri
# di una determinata sotto-stringa passata come argomento
# presente nella stringa a cui lo applichiamo
print(new_message.count('a'))


# stringa formattata
# permette di definire 
# delle stringhe contenenti anche valori numerici
# estrae il valore della variabile e in caso di valori numerici
# ne effettua la conversione (esempio da int a string)
formatted_string = f"Mi chiamo {nome_utente} e sono nato nel {birth_year}."
print(formatted_string)