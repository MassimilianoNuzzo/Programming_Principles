# richiedi un input all'utente
# salvalo su una variabile
# poi stampane il tipo sul terminale

# avvia il programma diverse volte 
# e digita diversi literal 
# osservane il tipo stampato

#input_type = input()
#print('Il tipo dell input è: ', type(input_type))

# pensa ad un oggetto che usi giornalmente
# ora definisci 4 variabili aventi valori di tipo diverso
# che rappresentano l'oggetto
# assegna alle variabili un nome che rispetti le convenzioni
# e scegli un data type appropriato 

# name = 'Book'
# page_number = 300
# price = 10.99
# is_digital = False

# print('Name',type(name))
# print('Page number',type(page_number))
# print('Price',type(price))
# print('Digital version',type(is_digital))

text = '''Harry si sentì leggero mentre saliva sulla scopa volante.
Per la prima volta, Harry provò il brivido del decollo.
Quella del volo, diventò immediatamente la più grande passione di Harry.'''

print('Testo originale:')
print(text)
print()

print('Quale parola vuoi sostituire?')
word_to_replace = input()

print('Con quale parola vuoi sostituirla?')
new_word = input()

replaced_text = text.replace(word_to_replace,new_word)

print('Testo con parola sostituita:',replaced_text)