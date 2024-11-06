# richiedi un input all'utente
# salvalo su una variabile
# poi stampane il tipo sul terminale
# avvia il programma diverse volte 
# e digita diversi literal 
# osservane il tipo stampato
input_type = input()
print('Il tipo dell input è: ', type(input_type)) 

# soluzione
# la funzione input indipendentemente dal data-type 
# della variabile ricevuta come argomento
# restituisce sempre una stringa 

# pensa ad un oggetto che usi giornalmente
# ora definisci 4 variabili aventi valori di tipo diverso
# che rappresentano l'oggetto
# assegna alle variabili un nome che rispetti le convenzioni
# e scegli un data type appropriato 
name = 'Book'
page_number = 300
price = 10.99
is_digital = False

print('Name',type(name))
print('Page number',type(page_number))
print('Price',type(price))
print('Digital version',type(is_digital))


# implementa il trova e sostituisci
# richiedi all'utente quale parola vuole trovare
# e con quale vuole sostituirla
# applica tali sostituzioni al testo fornito
# infine stampa il testo modificato

text = '''Harry si sentì leggero mentre saliva sulla scopa volante.
Per la prima volta, Harry provò il brivido del decollo.
Quella del volo, diventò immediatamente la più grande passione di Harry.'''

# stampa il testo originale
print('Testo originale:')
print(text)
print()

# chiedi all'utente quale parola intende sostituire
print('Quale parola desideri modificare?')
word_to_replace = input()

# chiedi all'utente con quale parola vuole sostituirla
# e salva la nuova parola in una variabile
print('Con quale parola vuoi sostituirla?')
new_word = input()

# applicare il metodo replace() alla variabile text
# a cui passiamo come argomenti le variabili word_to_replace
# e new_word, salvare la stringa restituita in una nuova variabile
modified_text = text.replace(word_to_replace,new_word)

# stampo il nuovo testo
print()
print('Testo modificato:')
print(modified_text)