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


eta = 29

print(False)
print(True)

print(type(nome_utente))
print(type(eta))
print(type(PI_GRECO))

upper_name = nome_utente.upper()
print(upper_name)

lower_name = nome_utente.lower()
print(lower_name)

message = f"Mi chiamo{nome_utente} e ho {eta} anni."
print(message)