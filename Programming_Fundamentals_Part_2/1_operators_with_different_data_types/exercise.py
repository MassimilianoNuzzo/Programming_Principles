# scrivi un programma che chiede all'utente
# il suo anno di nascita
# usa il dato per calcolare la sua età
# infine stampa l'età a schermo
#birth_year = int(input('Inserisci il tuo anno di nascita:'))
#current_year = 2024
#age = current_year - birth_year
#print(f'La tua età è {age} anni.')

# all'esercizio precedente
# aggiungi una variabile boolean 
# che rappresenta se l'utente è maggiorenne
# per assegnare il valore alla variabile
# controlla se l'utente ha età uguale o maggiore di 18
# infine stampala sul terminale
 
#birth_year = int(input('Inserisci il tuo anno di nascita:'))
#current_year = 2024
#age = current_year - birth_year
#is_adult = age >= 18 
#print(f'La tua età è {age} anni.')
#print(f'Maggiorenne? {is_adult}')

# all'esercizio precedente aggiungi 
# un altro variabile booleana
# che rappresenta se l'utente ha la patente
# che ha valore false
# ora controlla se l'utente è maggiorenne e 
# se ha la patente salva su una nuova variabile booleana
# e stampala a schermo

birth_year = int(input('Inserisci il tuo anno di nascita:'))
current_year = 2024
age = current_year - birth_year
is_adult = age >= 18
has_driving_license = False 
can_drive = is_adult and has_driving_license
print(f'La tua età è {age} anni.')
print(f'Maggiorenne? {is_adult}')
print(f'Puoi guidare? {can_drive}')
