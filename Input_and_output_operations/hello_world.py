# in Python il flusso di esecuzione predefinito è sequenziale 
# il che significa che il programma legge ed esegue le istruzioni nell'ordine in cui sono scritte dall'alto verso il basso

# l'istruzione print è una funzione
# una funzione è un elemento costituito da una serie di istruzioni
# che svolgono un'azione ben precisa

# print è una funzione built-in del linguaggio Python 
# ovvero già presente nel pacchetto standard quando effettuiamo l'installazione 

# per poter eseguire le istruzioni contenute nella funzione
# bisogna necessariamente aggiungere () utilizzate per richiamare la funzione
# senza la funzione non verrebbe presa in considerazione

# all'interno delle parentesi tonde posso specificare opzionalmente degli argomenti
# per argomenti si intende uno o più valori che forniamo in input alla funzione
# in questo caso una stringa 'hello world'

# una funzione può accettare degli argomenti in input esegue delle istruzioni e restituisce un risultato come output
print('hello world')


# in questo esempio stiamo passando due argomenti alla funzione print
# ovvero due stringhe 'hello world' e 'sono vivo' - tutti gli argomenti sono separati da una virgola
# gli argomenti sono posizionali in quanto la funzione print produce un output differente a seconda della loro posizione
print('hello world', 'sono vivo')
print('sono vivo', 'hello world')

# le funzioni possono avere anche dei keywords argument - argomenti chiave
# gli argomenti chiave vanno inseriti necessariamente dopo gli argomenti posizionali

# nella funzione print uno di questi è sep 
# permette di indicare un carattere o una serie di caratteri (string) da utilizzare come separatore
# tra un argomento posizionale e l'altro - di default se non inseriamo l'argomento chiave sep il separatore sarà uno spazio
print('ciao', 'mi chiamo', 'Mario', sep='*')

# con l'argomento chiave end è possibile indicare un carattere o una serie di caratteri (string) da utilizzare 
# alla fine della stampa degli argomenti posizionali - di default se non inserito ha valore '\n' che significa new line
print('ciao', 'mi chiamo', 'Mario', end='\n')

print('ciao', 'mi chiamo', 'Mario', end='END', sep='-')

# il carattere speciale '\n' (new line) usato per andare a capo
# può anche essere utilizzato senza l'argomento chiave end
print('\nciao', 'mi chiamo', 'Mario')

# un ulteriore carattere speciale è '\t'
# rappresenta un tabulatore orizzontale cioè un'indentazione o spostamento verso destra all'interno di una stringa 
# questo carattere viene spesso utilizzato per allineare testi in colonne o per separare dati in modo più leggibile
print('testo\tindentato')


# gestione errori
# errori di sintassi vengono generati prima dell'esecuzione del programma
# print("ciao"
# errori di run-time vengono generati duranti l'esecuzione del programma
# print("ciao")
# saluta("Mario")

# funzione input() per ricevere informazioni da tastiera
# le variabili per salvare informazioni
print('Ciao come ti chiami?')
name = input()

print('Il tuo nome è :', name)

# la funzione input può ricevere un solo argomento
years = input('Quanti anni hai?\n')
print(years)
