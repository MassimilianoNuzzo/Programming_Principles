# scrivi un programma che richiede all'utente il suo anno di nascita.
# usa l'anno di nascita per calcolare la sua età
# infine stampa l'età a schermo
birth_year = int(input('Inserisci il tuo anno di nascita: '))
current_year = 2024
age = current_year - birth_year
print(f'La tua età è {age} anni.')

# all'esercizio precedente
# aggiungi una variabile booleana
# che rappresenta se l'utente è maggiorenne.
# per assegnare il valore alla variabile
# controlla se l'utente ha età uguale o maggiore di 18,
# infine stampala sul terminale 
birth_year = int(input('Inserisci il tuo anno di nascita: '))
current_year = 2024
age = current_year - birth_year
print(f'La tua età è {age} anni.')
is_adult = age >= 18 
print('Sei Maggiorenne?', is_adult)

# all'esercizio precedente aggiungi 
# un altra variabile booleana
# che rappresenta se l'utente ha la patente
# che ha valore False.
# ora controlla se l'utente è maggiorenne e 
# se ha la patente.
# salva il risultato su una nuova variabile booleana
# e stampala a schermo
birth_year = int(input('Inserisci il tuo anno di nascita: '))
current_year = 2024
age = current_year - birth_year
print(f'La tua età è {age} anni.')
is_adult = age >= 18
print('Sei Maggiorenne?', is_adult)
has_driving_license = False 
can_drive = is_adult and has_driving_license
print('Puoi guidare?',can_drive)

'''
Hai i seguenti numeri binari
0b1011
0b0101
Utilizza fra loro un operatore bitwise
affinche il risultato sia un numero binario
con tutti i bit settati a 1
eccetto l'ultimo bit (quello più a destra)
'''
binary_1 = 0b1011
binary_2 = 0b0101
print(bin(binary_1 ^ binary_2))
 
